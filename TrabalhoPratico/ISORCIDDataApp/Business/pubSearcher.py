import requests

from Business.Command import Command
from Persistence.dbConnection import userscol, pubscol


class PubSearcher(Command):

    def __init__(self) :
        self.MY_API_KEY = "90d8a7452d4e9c32bc2e0611c9db8160"

    def get_info_publicacao(self,ORCID_ID_, nomeautor):
        resp = requests.get("https://pub.orcid.org/v3.0/" + ORCID_ID_ + "/works", headers={'Accept': 'application/json'})
        results = resp.json()

        autor = {"id": ORCID_ID_, "nome": nomeautor}

        for r in results['group']:

            title = r['work-summary'][0]['title']['title']['value']

            external = r['external-ids']['external-id']

            doi = self.get_external_doi(external)

            eid = self.get_external_eid(external)

            wos = self.get_external_wos(external)

            newid = 'None'

            numero_citacoes = 'None'
            issn = 'None'

            source_id_issn = 'None'

            sjr = 'None'

            if (eid != 'None'):
                newid = eid
                resp = requests.get("http://api.elsevier.com/content/abstract/scopus_id/"+eid+"?field=issn,citedby-count"
                                    ,  headers={'Accept': 'application/json', 'X-ELS-APIKey': self.MY_API_KEY})
                results = resp.json()

                numero_citacoes = self.get_numero_citacoes(results)

                try:
                    issn = results["abstracts-retrieval-response"]["coredata"]["prism:issn"]
                    try:
                        resp = requests.get("https://api.elsevier.com/content/serial/title/issn/"+issn+"?apiKey="+ self.MY_API_KEY)
                        results = resp.json()
                        source_id_issn = results["serial-metadata-response"]["entry"][0]["source-id"]
                        sjr = results["serial-metadata-response"]["entry"][0]["SJRList"]["SJR"][0]["$"]
                    except:
                        sjr = 'None'
                        source_id_issn = 'None'
                except:
                    issn = 'None'
            else:
                if (wos != 'None'):
                    newid = wos
                else:
                    if (doi != 'None'):
                        newid = doi

            if (newid == 'None'):
                break

            summary = r['work-summary']

            local_de_publicacao = self.get_journal_title(summary)

            year = self.get_ano(summary)

            try:
                pubscol.insert_one(
                    {"_id": newid, "titulo": title, "eid": eid, "doi": doi, "wos": wos, "issn": issn, "local_de_publicacao": local_de_publicacao,
                     "ano": year, "autores": [autor], "numero_citacoes": numero_citacoes, "SJR": sjr, "source-id-issn": source_id_issn})
            except:
                pubscol.update_one({"$and": [{"_id": newid}, {'autores.id':{"$nin": [ORCID_ID_]}}]}, {"$push": {"autores": autor}})
            finally:
                pub = {"id": newid, "titulo": title, "ano": year}
                userscol.update_one({"$and": [{"_id": ORCID_ID_}, {'publicacoes.id':{"$nin": [newid]}}]} , {"$push": {"publicacoes": pub}})

    def get_numero_citacoes(self, results):
        try:
            numero_citacoes = results["abstracts-retrieval-response"]["coredata"]["citedby-count"]
        except:
            numero_citacoes = '0'

        return numero_citacoes

    def get_external_doi(self, external):
        doi = 'None'
        for extid in external:
            if extid['external-id-type'] == 'doi':
                doi = extid['external-id-value']
        return doi

    def get_external_eid(self, external):
        eid = 'None'
        for extid in external:
            if extid['external-id-type'] == 'eid':
                eid = extid['external-id-value'][0 + 7:]
        return eid

    def get_external_wos(self, external):
        wos = 'None'
        for extid in external:
            if extid['external-id-type'] == 'wosuid':
                wos = extid['external-id-value']
        return wos

    def get_journal_title(self, summary):
        local_de_publicacao = 'None'
        for journaltitle in summary:
            if journaltitle['journal-title'] is not None:
                local_de_publicacao = journaltitle['journal-title']['value']
                break
        return local_de_publicacao

    def get_ano(self, summary):
        year = 'None'
        for ano in summary:
            if ano['publication-date'] is not None:
                if ano['publication-date']['year'] is not None:
                    year = ano['publication-date']['year']['value']
                    break
        return year

    def complete_info(self):
        for x in userscol.find({}, {"_id": 1, "nome": 1}):
            self.get_info_publicacao(x['_id'], x['nome'])


    def execute(self) -> None:
        print("A actualizar as publicações")
        self.complete_info()


if __name__ == '__main__':
    pubs = PubSearcher()
    pubs.complete_info()
    #get_scopus_info("85045332393") # 85016006344 85057139340 85047267736 85045332393
    # readfile("../ORCIDscraper/orcids.txt")
