import requests
from bs4 import BeautifulSoup
import json
import random

class appInfo(object):

    def __init__(self):
        self.url = ""
        self.fn = ""
        self.dev = ""
        self.ca = ""
        self.sp = ""
        self.avs = ""
        self.cn = ""
        self.size = ""
        self.v = ""
        self.ut = ""
        self.pn = ""
        self.id = ""
        self.pm = ""
        self.intro = ""
        self.new = ""

    def __str__(self):
        s = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            self.url, self.fn, self.dev, self.ca, self.sp, self.avs, self.cn,
            self.size, self.v, self.ut, self.pn, self.id, self.pm, self.intro, self.new
        )
        return s

def spider(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Upgrade-Insecure-Requests': '1'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200: # this means that this category has spider over
        return False, None
    app_list = ""
    try:
        app_list = response.json()['data']
    except:
        raise Exception(url + response.text)
    app_result = []
    for app in app_list:
        app_info = appInfo()
        packageName = app["packageName"]
        app_info.pn = packageName
        app_info.id = app["appId"]
        app_info.url = "http://app.mi.com/details?id={}".format(packageName)
        response = requests.get(app_info.url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        intro_titles = soup.find('div', class_='intro-titles')
        try:
            app_info.dev = intro_titles.find('p').text
        except:
            pass
        try:
            app_info.fn = intro_titles.find('h3').text
        except:
            pass
        try:
            special_font = intro_titles.find('p', class_='sepcial-font').text
            special_font = special_font.split('|')
            app_info.ca, app_info.sp = special_font[0][3:], special_font[1][3:]
        except:
            pass
        try:
            star1 = intro_titles.find('div', class_='star1-empty').find('div')['class'][1]
            app_info.avs = star1.split('-')[-1]
            app_intro_comments = intro_titles.find('span', class_='app-intro-comment').text
            app_info.cn = ''.join([c for c in app_intro_comments if str(c).isdigit()])
        except:
            pass

        look_detail = soup.find('div', class_='look-detail')
        try:
            cf = look_detail.find('ul', class_='cf')
            which = ""
            for li in cf.children:
                if li is None:
                    continue
                if '软件大小' in li.text:
                    which = "size"
                elif '版本' in li.text:
                    which = "version"
                elif '更新' in li.text:
                    which = "update"
                elif which == "size":
                    app_info.size = li.text
                    which = ""
                elif which == "version":
                    app_info.v = li.text
                    which = ""
                elif which == "update":
                    which = ""
                    app_info.ut = li.text
        except:
            pass

        permissions = []
        try:
            for li in look_detail.find('ul', class_='second-ul').children:
                permissions.append(li.text[1:].strip())
        except:
            pass
        app_info.pm = '-'.join(permissions)
        app_text = soup.find('div', class_='app-text')
        if app_text is not None:
            app_text = app_text.find_all('p', class_='pslide')
            if app_text is not None and len(app_text) > 0:
                app_info.intro = app_text[0].text.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
            if len(app_text) > 1:
                app_info.new = app_text[1].text.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
        app_result.append(app_info)

    return True, app_result


if __name__ == '__main__':
    categorys = [5, 27, 2, 7, 12, 10, 9, 4, 3, 6, 14, 8, 11, 13, 1, 15]
    data_file = "/home/lmy/Project/CornJobs/serviceknowledgespider/data/mi_appstore.entities"
    n = random.randint(1, 5)
    for i in range(n):
        lines = open('/home/lmy/Project/CornJobs/serviceknowledgespider/mi_appstore.cfg', 'r').readlines()
        lines = [int(line.strip()) for line in lines]
        if lines[0] >= len(categorys):
            exit(-1)
        page, cid = lines[1], categorys[lines[0]]
        url = 'http://app.mi.com/categotyAllListApi?page={:d}&categoryId={:d}&pageSize=30'.format(page, cid)
        ok, res = spider(url)
        with open('/home/lmy/Project/CornJobs/serviceknowledgespider/mi_appstore.cfg', 'w') as w:
            if len(res) > 0:
                w.write("{:d}\n".format(lines[0]))
                w.write("{:d}\n".format(page+1))
            else:
                w.write("{:d}\n".format(lines[0]+1))
                w.write("{:d}\n".format(0))
        if len(res) == 0:
            continue
        with open(data_file, 'a') as w:
            w.writelines([r.__str__() for r in res])
