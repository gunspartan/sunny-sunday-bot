from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import json

def getSunnySundays(patchNotesURL):
  SUNNY_SUNDAY_HEADER_STRING = "Log in each Sunday during the event period to enjoy various perks."
  uClient = uReq(patchNotesURL)
  page_html = uClient.read()
  uClient.close()
  soup = BeautifulSoup(page_html, "html.parser")
  sunnySunday = soup.find('p', text=SUNNY_SUNDAY_HEADER_STRING)
  sunnySundayList = sunnySunday.find_next_siblings('ul')[0].findAll("li")
  return sunnySundayList

def formatSunnySundays(sunnySundayArray):
  allEvents = {}
  for sundayEvent in sunnySundayArray:
    eventTitle = sundayEvent.strong
    if eventTitle is not None:
      eventTitle = eventTitle.get_text()
    eventDescription = sundayEvent.ul
    if eventDescription is not None:
      eventDescription = eventDescription.get_text()
    if eventTitle and eventDescription:
      allEvents[eventTitle] = eventDescription
  return allEvents

def exportJSON(sunnySundaysObject):
  sunnySundayJSON = json.dumps(sunnySundaysObject)
  print(sunnySundayJSON)
  with open('sunny_sunday.json', 'w') as f:
      json.dump(sunnySundaysObject, f)

PATCH_URL = 'https://maplestory.nexon.net/news/73909/updated-april-27-v-232-blooming-forest-patch-notes'
myList = getSunnySundays(PATCH_URL)
myEvents = formatSunnySundays(myList)
exportJSON(myEvents)