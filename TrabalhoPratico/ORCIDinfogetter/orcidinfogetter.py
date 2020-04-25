import requests
import json
import textwrap

def get_orcid_ids(ORCID_ID_):
    resp = requests.get("https://pub.orcid.org/v3.0/"+ORCID_ID_+"/works", headers={'Accept':'application/json'})
    results = resp.json()
    my_list = []
    for r in results['group']:
        for r2 in r['work-summary']:
            try:
                orcid = r2['url']['value']
                if orcid.find('eid=') > 0:
                    k1 = orcid.find('eid=')
                    k2 = orcid.find('&', k1)
                    if orcid[k1 + 11:k2] not in my_list:
                        my_list.append(orcid[k1 + 11:k2])
            except:
                my_list.append('None')

    print(my_list)
    #return my_list2

def readfile(path):
    f = open(path, "r")

    while True:
        line = f.readline()
        line = line.replace("\n", "")
        if not line:
            break
        get_orcid_ids(line)

if __name__ == '__main__':
    readfile("../ORCIDscraper/orcids.txt")
    #get_orcid_ids("0000-0001-6018-7346")