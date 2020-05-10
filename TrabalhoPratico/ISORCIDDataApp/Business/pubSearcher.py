import requests
from Persistence.dbConnection import userscol, pubscol
import hashlib
import json

MY_API_KEY = "90d8a7452d4e9c32bc2e0611c9db8160"

def get_info_publicacao(ORCID_ID_, nomeautor):
    resp = requests.get("https://pub.orcid.org/v3.0/" + ORCID_ID_ + "/works", headers={'Accept': 'application/json'})
    results = resp.json()

    autor = {"id": ORCID_ID_, "nome": nomeautor}

    for r in results['group']:

        title = r['work-summary'][0]['title']['title']['value']

        year = 'None'
        doi = 'None'
        eid = 'None'
        wos = 'None'
        local_de_publicacao = 'None'
        for extid in r['external-ids']['external-id']:
            if extid['external-id-type'] == 'doi':
                    doi = extid['external-id-value']
            if extid['external-id-type'] == 'eid':
                    eid = extid['external-id-value'][0 + 7:]
            if extid['external-id-type'] == 'wosuid':
                wos = extid['external-id-value']

        for journaltitle in r['work-summary']:
            if journaltitle['journal-title'] is not None:
                local_de_publicacao = journaltitle['journal-title']['value']
                break

        for ano in r['work-summary']:
            if ano['publication-date'] is not None:
                if ano['publication-date']['year'] is not None:
                    year = ano['publication-date']['year']['value']
                    break

        str2encode = title + year + eid + doi + wos
        tid = hashlib.md5(str2encode.encode())
        newid = tid.hexdigest()

        try:
            pubscol.insert_one(
                {"_id": newid, "titulo": title, "eid": eid, "doi": doi, "wos": wos, "local_de_publicacao": local_de_publicacao,
                 "ano": year, "autores": [autor], "numero_citacoes": '', "numero_citacoes_ultimos_3_anos": '', "SJR": ''})
        except:
            pubscol.update_one({"$and": [{"_id": newid}, {'autores.id':{"$nin": [ORCID_ID_]}}]}, {"$push": {"autores": autor}})
        finally:
            pub = {"id": newid, "titulo": title, "ano": year}
            userscol.update_one({"$and": [{"_id": ORCID_ID_}, {'publicacoes.id':{"$nin": [newid]}}]} , {"$push": {"publicacoes": pub}})


def get_scopus_info(SCOPUS_ID):
    url = ("http://api.elsevier.com/content/abstract/scopus_id/"+ SCOPUS_ID
           + "?field=authors,title,publicationName,volume,issueIdentifier,"
           + "prism:pageRange,coverDate,article-number,doi,issn,citedby-count,prism:aggregationType")

    resp = requests.get(url,headers={'Accept':'application/json','X-ELS-APIKey': MY_API_KEY})

    print(json.loads(resp.text.encode('utf-8')))
    """f = open("da.json", "w")
    f.write(str(json.loads(resp.text.encode('utf-8'))))
    f.close()"""

    # https://api.elsevier.com/content/abstract/citations?scopus_id=38349047757&apiKey=xxxxxxxxxxx&httpAccept=application%2Fjson

    url2 = ("https://api.elsevier.com/content/abstract/citations?scopus_id=" + SCOPUS_ID
           + "&apiKey="+MY_API_KEY+"&httpAccept=application%2Fjson")

    resp2 = requests.get(url2)

    print(json.loads(resp2.text.encode('utf-8')))

def readfile(path):
    f = open(path, "r")

    while True:
        line = f.readline()
        line = line.replace("\n", "")
        if not line:
            break
        get_info_publicacao(line)


def complete_info():
    for x in userscol.find({}, {"_id": 1, "nome": 1}):
        get_info_publicacao(x['_id'], x['nome'])


if __name__ == '__main__':
    #complete_info()
    get_scopus_info("85045332393") # 85016006344 85057139340 85047267736 85045332393
    # readfile("../ORCIDscraper/orcids.txt")
