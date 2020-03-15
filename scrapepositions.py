# Description: scrape the wikipedia page of democratic primary candidate positions to
#              determine what topics are being recorded and print out the headings from
#              each table.
# Purpose:     to learn a bit about how BeautifulSoup works, and associated bits of Python

# Adapted from https://medium.com/analytics-vidhya/web-scraping-wiki-tables-using-beautifulsoup-and-python-6b9ea26d8722
import requests
website_url = requests.get('https://en.wikipedia.org/wiki/Political_positions_of_the_2020_Democratic_Party_presidential_primary_candidates').text
#print(website_url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
#print(soup.prettify())

##########################################################################################
# Get a list of the table names
##########################################################################################

list_of_tables = []
all_toclevel2_li_s = soup.find_all('li',{'class':'toclevel-2'})
for toclevel2_li in all_toclevel2_li_s:
  toc_text = toclevel2_li.find('span',{'class':'toctext'})
  list_of_tables.append(toc_text.string)

print(list_of_tables)

##########################################################################################
# Get headings from each table
##########################################################################################

all_tables = soup.find_all('table',{'class':'wikitable sortable'})
for a_table in all_tables:
  #print(a_table.prettify())
  firstrow = a_table.find('tr')
  tableheaders = firstrow.find_all('th')
  #print(tableheaders)
  
  for headerText in tableheaders:
    #print(headerText.contents)
    elementConcatText = ""
    for element in headerText.stripped_strings:
      elementConcatText += element + " "
    # 'Still running' and 'Candidate headers' are not interesting; exclude them
    if not( "Still running" in element or "Candidate" in element ):
      print( elementConcatText )
  # print a blank line between each table
  print("")
