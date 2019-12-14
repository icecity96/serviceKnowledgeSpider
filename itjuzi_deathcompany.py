import requests
import random

if __name__ == '__main__':
    output = "/home/lmy/Project/CornJobs/serviceknowledgespider/data/itjuzi_deathcompany.entities"
    cfg = '/home/lmy/Project/CornJobs/serviceknowledgespider/itjuziDeathcompany.cfg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Upgrade-Insecure-Requests': '1'
    }
    proxies = requests.get("http://192.168.1.118:18899/api/v1/proxies").json()
    proxies = proxies["proxies"]
    random.shuffle(proxies)
    for i in range(10):
        page = open(cfg, 'r').readlines()[0]
        page = page.strip()
        url = 'https://www.itjuzi.com/api/closure?com_prov=&sort=&page={}&keyword=&cat_id='.format(page)
        proxy = proxies[i % len(proxies)]
        http_s ="https" if proxy["is_https"] else "http"
        proxy = { http_s: "{}://{}:{:d}".format(http_s, proxy["ip"], proxy["port"])}
        response = requests.get(url, headers=headers, proxies=proxy).json()
        data = response["data"]["info"]
        with open(output, 'a') as f:
            f.writelines([str(line)+'\n' for line in data])
        with open(cfg, 'w') as w:
            w.write("{:d}\n".format(int(page)+1))
