import test_markup
from bs4 import BeautifulSoup

website = test_markup.html_doc

# Parse the website
soup = BeautifulSoup(website, 'html.parser')

# Direct 
#print(soup.body)
#print(soup.head)
#print(soup.head.title)

# find()
#el = soup.find('div')

# find_all() or findAll()
#el = soup.find_all('div')
#el = soup.find_all('div')[1]  # Get the second div found

# find() by id or by 'class_' use the underscore to avoid a syntax error
#el = soup.find(class_='headline')
#el = soup.find_all(class_='headline')
#el = soup.find(attrs={"data-hello": "hi"})

# select
#el = soup.select('#section-1')
#el = soup.select('#section-1')[0] 
#el = soup.select('.item')[0]

# get_text()

# el = soup.find(class_='headline').get_text()

# for headline in soup.select('.headline'):
#     print(headline.get_text())


# Navigation

#el = soup.body.contents[1].contents[1].next_sibling
#el = soup.body.contents[1].contents[1].find_next_sibling
# el = soup.find(id='section-2').find_previous_sibling()
# el = soup.find(class_='item').find_parent()
# el = soup.find('h3').find_next_sibling('p')
el = soup.body.contents


print(el)

















