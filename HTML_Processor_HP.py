import csv
from bs4 import BeautifulSoup


filename = 'HUSH-US-20181211-TuesdayShoeday1.html'

#INITIALIZE HTML FILE
html = open(filename, 'r+')
soup = BeautifulSoup(html, 'html.parser')

# WRAP ROWS IN TABLES
for i in soup.find_all('tr'):
    i.wrap(soup.new_tag('table'))

# DECLARE VARIABLES
urls = {}
hrefs = {}
doubleclick = '$clickthrough(Hero1,myURL=https://ad.doubleclick.net/ddm/trackclk/N800582.3336694HUSHPUPPIES/B21328916.223583574;dc_trk_aid=421618454;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
tmemail = '&tmemail=)$'

#READ CSV TO LIST
with open('links.csv', 'r') as link_csv:
    csv_reader = csv.reader(link_csv)
    hrefs = list(csv_reader)
    linknum = len(hrefs)
    for i in range(0, linknum):
        urls["link" + str(i + 1)] = hrefs[i]
    for i in range(0, linknum):
        hrefs[i] = doubleclick + str(urls.get('link' + str(i + 1))).strip("['").strip("']") + tmemail


#WRAP TAGGED IMAGES IN LINKS
counter = 0
for i in soup.find_all('img'):
    linkareas = soup.find_all(id="link" + str(counter))
    for img in linkareas:
       img.wrap(soup.new_tag('a', href=(hrefs[counter - 1])))
    counter += 1


#FORMAT A TAGS
for i in soup.find_all('a'):
    i['style'] = 'text-decoration:none;color:#707072;'
    i['target'] = '_blank'

#displayblock images
for i in soup.find_all('img'):
    i['style'] = 'display:block;'

# TABLE FORMATTING
for i in soup.find_all('table'):
    i['border'] = '0'
    i['cellpadding'] = '0'
    i['cellborder'] = '0'
    i['align'] = 'center'
    i['valign'] = 'top'
    i['style'] = 'border-collapse:collapse;font-family:arial,helvetica,sans-serif;font-weight:bold;color:#000001;'
    i['cellpadding'] = '0'

# CELL FORMATTING
for i in soup.find_all('td'):
    i['height'] = i.img['height']
    i['width'] = i.img['width']
    i['border'] = '0'
    i['cellpadding'] = '0'
    i['cellborder'] = '0'
    i['align'] = 'center'
    i['valign'] = 'top'
    i['bgcolor'] = 'ffffff'
    i['style'] = 'border-collapse:collapse;font-size:16px;'
    i['cellpadding'] = '0'

# CTA FORMATTING
for i in soup.find_all(id="CTA"):
    i['bgcolor'] = 'FFFFFF'
    i['valign'] = 'middle'
    i.img.replace_with('SHOP NOW')
    i['style'] = 'color:#707072;font-size:16px;'

# TEXT AREA FORMATTING
for i in soup.find_all(id="TEXT"):
    i['bgcolor'] = 'FFFFFF'


print(soup.prettify())

html.close()

html = soup.prettify("utf-8")
with open(filename, 'wb') as file:
   file.write(html)