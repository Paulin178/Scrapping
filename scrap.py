from Scraper import Scraper
from Cirfa import Cirfa

# L'url du site que je souhaite Scraper
#site s'engager.fr : je souhaite récupérer les infos des 102 Cirfas français
baseUrl = 'https://www.sengager.fr'
uri = "/ou-nous-rencontrer?geoloc_lat=&geoloc_lng=&sort_by=created&sort_order=ASC&page="

cirfaInstance = Cirfa(baseUrl, uri, 8)

scraper = Scraper(cirfaInstance, "linksList.csv", "infos.csv")

scraper.exec()

print("Done")