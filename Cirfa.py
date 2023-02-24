from Toolkit import Toolkit
from CirfaEntry import CirfaEntry
class Cirfa:
    def __init__(self, baseUrl, uri, nbPage):
        self.baseUrl = baseUrl
        self.uri = uri
        self.setPageMax(nbPage)
        self.urls = []
        self.endpoints = []
        self.result = []
        self.finalFileNameFields = ["name","address","phone", "description"]

    def setPageMax(self, pageMax):
        self.nbPage = pageMax + 1
        return self
    
    def getLinks(self):
        for i in range(self.nbPage):
            self.urls.append(self.baseUrl + self.uri + str(i))
        return self.urls

    def setEndpoints(self,soup):

        ul = soup.find('ul', { "class": "ListCirfa-list"})
        lis = ul.findAll('li')
        links = []
        for li in lis:
            a = li.find('a')
            try: 
                links.append(a['href'])
            except:
                pass
        self.endpoints.extend(Toolkit.addBaseUrl(self.baseUrl, links))
        return self.endpoints

    def getEndpoints(self):
        return self.endpoints

    def getFinalFieldNames(self):
        return self.finalFileNameFields

    def getInfoByPage(self, soup):
        fiches = []
        name = Toolkit.tryToCleanOrReturnBlank(soup.find("div", {"class" : "field--name-node-title"}))
        address = Toolkit.tryToCleanOrReturnBlank(soup.find("div", {"class" : "ListAccess--address"})).replace("\n", " ")
        phone = Toolkit.tryToCleanOrReturnBlank(soup.find("div", {"class" : "BlockHighlight-contact"}).find("a")).replace(" ", "").replace(".", "")[0:10]
        description = Toolkit.tryToCleanOrReturnBlank(soup.find("div", {"class" : "field--name-field-cirfa-description"})).replace("\n", " ")
        fiche = CirfaEntry(name, address, phone, description)
        fiches.append(fiche)
        self.result.extend(fiches)
        return fiches

        
    def getResult(self):
        return self.result

    def getDictResult(self):
        result = []
        for res in self.getResult():
            result.append(res.getDictEntry())
        return result