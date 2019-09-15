import webbrowser as wb
import requests, random
keywords = ['mqtt', 'iot', 'internet of things', 'mqtt python', 'what is mqtt', 'mqtt open source', 'mqtt essentials', 'mqtt using flask']
base_url = "https://www.google.com/search?q="
while True:
    gen_urls = base_url + str(keywords[random.randint(0,5)]) # generating urls
    #list_urls = base_url + str(random.choice(keywords))
    wb.open(list_urls[random.randint(0,5)])