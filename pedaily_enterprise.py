import requests
from bs4 import BeautifulSoup


class enterpriseInfor(object):

    def __init__(self):
        self.enterprise_full_name = ""
        self.enterprise_short_name = ""
        self.enterprise_location = ""
        self.enterprise_registration = ""
        self.enterprise_created_at = ""
        self.enterprise_domain = ""
        self.enterprise_website = ""
        self.enterprise_introduction = ""

    def __str__(self):
        return "full_name: {}\nshort_name: {}\nlocation: {}\nregistration: {}\ncreated_at: {}\nwebsite: {" \
               "}\nintroduction: {}".format(self.enterprise_full_name, self.enterprise_short_name,
                                            self.enterprise_location, self.enterprise_registration,
                                            self.enterprise_created_at, self.enterprise_website,
                                            self.enterprise_introduction)



def _spider(url):
    enterprise = enterpriseInfor()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Upgrade-Insecure-Requests': '1'
    }
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    h1_title = soup.find('h1')
    full_name, short_name = h1_title.text, h1_title.find('em').text
    full_name = full_name[:-len(short_name)]
    enterprise.enterprise_full_name = full_name
    enterprise.enterprise_short_name = short_name
    info = soup.find('div', class_="info")
    lis = info.find('ul').find_all('li')
    for li in lis:
        li_text = li.text
        if li_text.startswith('机构总部'):
            enterprise.enterprise_location = li_text[5:]
        elif li_text.startswith('注册地点'):
            enterprise.enterprise_registration = li_text[5:]
        elif li_text.startswith('成立时间'):
            enterprise.enterprise_created_at = li_text[5:]
        elif li_text.startswith('所属行业'):
            enterprise.enterprise_domain = li_text[5:]
        elif li_text.startswith('官方网站'):
            enterprise.enterprise_website = li_text[5:]
    introduction = soup.find('div', class_='detail').find('div', class_='box-fix-l')
    for child in introduction.children:
        if child.name == 'p':
            if len(child.text) > 0:
                enterprise.enterprise_introduction = child.text
                break
    return enterprise


if __name__ == '__main__':
    config = "/home/ubuntu/Project/CornJobs/serviceknowledgespider/pedaily.cfg"
    data_file = "/home/ubuntu/Project/CornJobs/serviceknowledgespider/data/pedaily_enterprise.entities"
    for number in range(30):
        page_number = open(config, 'r').readlines()[0].strip()
        page_number = int(page_number)
        try:
            enterprise = _spider('https://zdb.pedaily.cn/enterprise/show{:d}/'.format(page_number))
        except:
            page_number += 1
            with open(config, 'w') as w:
                w.write('{:d}\n'.format(page_number))
        page_number += 1
        with open(config, 'w') as w:
            w.write('{:d}\n'.format(page_number))
        with open(data_file, 'a') as w:
            w.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
                enterprise.enterprise_full_name, enterprise.enterprise_short_name,
                enterprise.enterprise_location, enterprise.enterprise_registration,
                enterprise.enterprise_created_at, enterprise.enterprise_domain,
                enterprise.enterprise_website, enterprise.enterprise_introduction))
