import requests
import json
import textwrap

def get_info_publicacao(ORCID_ID_):
    resp = requests.get("https://pub.orcid.org/v3.0/"+ORCID_ID_+"/works", headers={'Accept': 'application/json'})
    results = resp.json()
    my_list = []
    for r in results['group']:
        for r2 in r['work-summary']:
            title = r2['title']['title']['value']
            try:
                orcid = r2['url']['value']
                if orcid.find('eid=') > 0:
                    k1 = orcid.find('eid=')
                    k2 = orcid.find('&', k1)
                    if orcid[k1 + 11:k2] not in my_list:
                        my_list.append((title,orcid[k1 + 11:k2]))
            except:
                my_list.append((title, 'None'))

    print(my_list)

def readfile(path):
    f = open(path, "r")

    while True:
        line = f.readline()
        line = line.replace("\n", "")
        if not line:
            break
        get_info_publicacao(line)

if __name__ == '__main__':
    readfile("../ORCIDscraper/orcids.txt")
