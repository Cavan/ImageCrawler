import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.cbc.ca/news')

soup = BeautifulSoup(response.text, 'html.parser')

# We want to grab the Headlines, excerpt, and links to article.

articles = soup.find_all(class_='contentWrapper')

with open('cbc_news.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Excerpt']
    csv_writer.writerow(headers)


    for article in articles:
        title = article.find(class_='headline').get_text().replace('\n', '')
        # Not all the headlines have an excerpt so we need to handle the 
        # out of range exception.    
        try:
            excerpt = article.select('.description')[0].get_text()
        except IndexError:
            excerpt = "No excerpt found"
        csv_writer.writerow([title, excerpt])
   
    
