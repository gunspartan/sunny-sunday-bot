from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import json

PATCH_URL = 'https://maplestory.nexon.net/news/73909/updated-april-27-v-232-blooming-forest-patch-notes'

uClient = uReq(PATCH_URL)
page_html = uClient.read()
uClient.close()

soup = BeautifulSoup(page_html, "html.parser")

sunnySunday = soup.find('p', text="Log in each Sunday during the event period to enjoy various perks.")
sunnySundayList = sunnySunday.find_next_siblings('ul')[0].findAll("li")

allEvents = {}
for sundayEvent in sunnySundayList:
  eventTitle = sundayEvent.strong
  if eventTitle is not None:
    eventTitle = eventTitle.get_text()

  eventDescipriton = sundayEvent.ul
  if eventDescipriton is not None:
    eventDescipriton = eventDescipriton.get_text()
  if eventTitle and eventDescipriton:
    allEvents[eventTitle] = eventDescipriton

sunnySundayJSON = json.dumps(allEvents)

print(sunnySundayJSON)

with open('sunny_sunday.json', 'w') as f:
    json.dump(allEvents, f)