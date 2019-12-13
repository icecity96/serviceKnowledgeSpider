import requests
from bs4 import BeautifulSoup, element

def spider(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Upgrade-Insecure-Requests': '1'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'gb2312'
    soup = BeautifulSoup(response.text, 'lxml')
    soup = soup.find('div', class_='main')
    category, subcategory, name, url = "", "", "", ""
    result = []
    for child in soup.children:
        if not isinstance(child, element.Tag):
            continue
        if child['class'][0] == 'dh':
            category = child.find('div', class_='dh_l').text.strip()
        if child['class'][0] == 'left':
            subcategory = child.text.strip()
        if child['class'][0] == 'right':
            for href in child.find_all('a'):
                name, url = href.text.strip(), href['href'].strip()
                result.append(list([category, subcategory, name, url]))
    return result

if __name__ == '__main__':
    output =  "/home/lmy/Project/CornJobs/serviceknowledgespider/data/100ec.entities"
    url = 'http://www.100ec.cn/zt/qyk/'
    enterprises = spider(url)
    with open(output, 'w') as w:
        w.write("category\tsubcategory\tname\turl\n")
        w.writelines(['\t'.join(line)+'\n' for line in enterprises])