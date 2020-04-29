import requests
from dbConnection import userscol, pubscol
import hashlib


def get_info_publicacao(ORCID_ID_):
    resp = requests.get("https://pub.orcid.org/v3.0/" + ORCID_ID_ + "/works", headers={'Accept': 'application/json'})
    results = resp.json()

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
                 "ano": year, "autores": [ORCID_ID_], "numero_citacoes": '', "numero_citacoes_ultimos_3_anos": '', "SJR": ''})
        except:
            pubscol.update_one({"$and": [{"_id": newid}, {'autores':{"$nin": [ORCID_ID_]}}]}, {"$push": {"autores": ORCID_ID_}})
        finally:
            userscol.update_one({"$and": [{"_id": ORCID_ID_}, {'publicacoes':{"$nin": [newid]}}]} , {"$push": {"publicacoes": newid}})
            #userscol.update_one({"_id": ORCID_ID_}, {"$push": {"publicacoes": newid}})

        #print(id.hexdigest(), ' ', doi, ' ', title, ' ', eid, ' ', wos, ' ', year, ' ', local_de_publicacao)



def readfile(path):
    f = open(path, "r")

    while True:
        line = f.readline()
        line = line.replace("\n", "")
        if not line:
            break
        get_info_publicacao(line)


def complete_info():
    for x in userscol.find({}, {"_id": 1}):
        get_info_publicacao(x['_id'])


if __name__ == '__main__':
    complete_info()
    # readfile("../ORCIDscraper/orcids.txt")
