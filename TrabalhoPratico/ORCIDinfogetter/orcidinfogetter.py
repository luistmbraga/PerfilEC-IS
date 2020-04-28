import requests
from dbConnection import userscol, pubscol


def get_info_publicacao(ORCID_ID_):
    resp = requests.get("https://pub.orcid.org/v3.0/" + ORCID_ID_ + "/works", headers={'Accept': 'application/json'})
    results = resp.json()

    contador = 0
    for r in results['group']:

        title = r['work-summary'][0]['title']['title']['value']

        doi = 'None'

        for extid in r['external-ids']['external-id']:
            if extid['external-id-type'] == 'doi':
                    doi = extid['external-id-value']

        print(doi, ' ', title)
        contador += 1
        """for r2 in r['work-summary']:
            title = r2['title']['title']['value']
            eid = 'None'
            doi = 'None'
            wos = 'None'
            local_de_publicacao = 'None'

            # eid
            try:
                orcid = r2['url']['value']
                if orcid.find('eid=') > 0:
                    k1 = orcid.find('eid=')
                    k2 = orcid.find('&', k1)
                    if orcid[k1 + 11:k2] not in my_list:
                        eid = orcid[k1 + 11:k2]
            except:
                eid = 'None'

            # ano
            try:
                ano = r2['publication-date']['year']['value']
            except:
                ano = 'None'

            # doi
            try:
                for extid in r2['external-ids']['external-id']:
                    if extid['external-id-type'] == 'doi':
                        doi = extid['external-id-value']
            except:
                doi = 'None'

            # wos
            try:
                for extid in r2['external-ids']['external-id']:
                    if extid['external-id-type'] == 'wosuid':
                        wos = extid['external-id-value']
            except:
                wos = 'None'

            # local_de_publicacao
            try:
                local_de_publicacao = r2['journal-title']['value']
            except:
                local_de_publicacao = 'None'

             my_list.append((title, eid, ano, doi, wos, local_de_publicacao))
            try:
                pubscol.insert_one({"_id": title, "eid": eid, "doi": doi, "wos": wos, "local_de_publicacao": local_de_publicacao,
                                    "autores": [ORCID_ID_], "numero_citacoes": '', "numero_citacoes_ultimos_3_anos": '', "SJR": ''})
            except:
                pubscol.update_one({"_id": title}, {"$push": {"autores": ORCID_ID_}})
            finally:
                userscol.update_one({"_id": ORCID_ID_}, {"$push": {"publicacoes": title}})"""
    print(contador)
    # print(my_list)


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
