from selenium import webdriver

class ORCIDAlgoritmiBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://algoritmi.uminho.pt/members/")
        self.links = []
        self.orcids = []

    def getLinks(self):
        elementos = self.driver.find_element_by_xpath('//*[@id="result-result"]')
        linhas = elementos.find_elements_by_class_name('ResearcherResults-Avatar')

        for id in linhas:
            self.links.append(id.get_attribute('href'))

        print('Encontrados ' , len(linhas), ' elementos na equipa.')


    def getOrcid(self):

        for link in self.links:
            self.driver.get(str(link))

            try:
                self.orcids.append(self.driver.find_element_by_xpath("//a[contains(@href,'http://orcid.org/')]").text)
            except:
                print(self.driver.find_element_by_class_name('Profile-ResearcherName'). text, ' não possui orcid')

    def writetofile(self):
        f = open("orcids.json", "a")
        f.write("[\n")
        for orcid in self.orcids:
            f.write("{\"id\": \"" + orcid  +"\"},\n")
        f.write("]")
        f.close()


    def main(self, bot):
        bot.getLinks()
        bot.getOrcid()
        self.driver.close()
        self.writetofile()

if __name__ == "__main__":
    my_bot = ORCIDAlgoritmiBot()
    my_bot.main(my_bot)
