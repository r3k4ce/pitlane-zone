# openai api test
from bs4 import BeautifulSoup
from openai import OpenAI
import sumy
import requests

# authenticate with API key stored locally
client = OpenAI()

sources = ["https://www.autosport.com/rss/f1/news/", "https://www.motorsport.com/rss/f1/news/", "https://www.planetf1.com/ps-rss", "https://www.gpblog.com/en/rss/index.xml"]

# store extracted titles and links in dictionary
extracted_data = {}

# iterate through each source
for source in sources:
    # fetch data from source
    response = requests.get(source)

    soup = BeautifulSoup(response.content, 'xml')

    title = soup.find_all('title')
    link = soup.find_all('link')

    extracted_data['title'] = title
    extracted_data['link'] = link

print(extracted_data)


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about recursion in programming."}
    ]
)

# print(completion.choices[0].message)