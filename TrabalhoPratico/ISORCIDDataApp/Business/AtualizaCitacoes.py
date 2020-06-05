import requests

from Business.Command import Command
from Persistence.dbConnection import pubscol


class AtualizaCitacoes(Command):

    def __init__(self):
        self.MY_API_KEY = "90d8a7452d4e9c32bc2e0611c9db8160"

    def atualizarCitacoes(self):
        for x in pubscol.find({"eid": { "$ne": "None" }}, {"_id": 1}):

            eid = x["_id"]

            resp = requests.get("http://api.elsevier.com/content/abstract/scopus_id/" + eid + "?field=issn,citedby-count"
                , headers={'Accept': 'application/json', 'X-ELS-APIKey': self.MY_API_KEY})
            results = resp.json()

            try:
                numero_citacoes = results["abstracts-retrieval-response"]["coredata"]["citedby-count"]
                pubscol.update_one({"_id": eid}, {"$set": {"numero_citacoes": numero_citacoes}})
            except:
                print(eid + " ainda não possui citações.")

            try:
                issn = results["abstracts-retrieval-response"]["coredata"]["prism:issn"]
                try:
                    resp = requests.get(
                        "https://api.elsevier.com/content/serial/title/issn/" + issn + "?apiKey=" + self.MY_API_KEY)
                    results = resp.json()
                    source_id_issn = results["serial-metadata-response"]["entry"][0]["source-id"]
                    sjr = results["serial-metadata-response"]["entry"][0]["SJRList"]["SJR"][0]["$"]
                    pubscol.update_one({"_id": eid}, {"$set": {"source-id-issn": source_id_issn, "SJR": sjr}})
                except:
                    print(eid + " ainda não possui cotação válida.")
            except:
                print(eid + " ainda não possui issn.")


    def execute(self) -> None:
        self.atualizarCitacoes()
