import requests
from bs4 import BeautifulSoup
url = input("Enter the url: ")
response = requests.get(url)
if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')
    article_titles = soup.find_all('a', class_='storylink')
    with open('article_titles.txt', 'w') as file:
        for title in article_titles:
            file.write(title.text + '\n')
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
