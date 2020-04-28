from selenium import webdriver
import time
from dbConnection import userscol

class ORCIDAlgoritmiBot:
    def __init__(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                            'notifications': 2, 'auto_select_certificate': 2,
                                                            'fullscreen': 2,
                                                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                            'media_stream_mic': 2, 'media_stream_camera': 2,
                                                            'protocol_handlers': 2,
                                                            'ppapi_broker': 2, 'automatic_downloads': 2,
                                                            'midi_sysex': 2,
                                                            'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                            'metro_switch_to_desktop': 2,
                                                            'protected_media_identifier': 2, 'app_banner': 2,
                                                            'site_engagement': 2,
                                                            'durable_storage': 2, 'profile.managed_default_content_settings.images': 2}}
        chromeOptions.add_experimental_option('prefs', prefs)
        chromeOptions.add_argument("start-maximized")
        chromeOptions.add_argument("disable-infobars")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--headless")
        chromeOptions.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=chromeOptions)
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
            name = self.driver.find_element_by_class_name('Profile-ResearcherName').text

            try:
                id = self.driver.find_element_by_xpath("//a[contains(@href,'http://orcid.org/')]").text
                userscol.insert_one({"_id": id, "nome": name, "publicacoes": []})
            except:
                print(name, ' não possui orcid')


    def writetofile(self):
        f = open("orcids.txt", "a")
        for orcid in self.orcids:
            f.write(orcid + "\n")
        f.close()


    def main(self, bot):
        bot.getLinks()
        bot.getOrcid()
        self.driver.close()


if __name__ == "__main__":
    start = time.time()
    my_bot = ORCIDAlgoritmiBot()
    end = time.time()
    print("tempo demorado ", end - start)
    my_bot.main(my_bot)
