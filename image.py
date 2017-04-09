import dryscrape
from bs4 import BeautifulSoup
session = dryscrape.Session()
session.visit("http://charts.londonstockexchange.com/chart/CompanySummaryChart2_image.aspx?code=15.UKX&imageFormat=png")
response = session.body()
#soup = BeautifulSoup(response)
print response
#soup.find(id="intro-text")
