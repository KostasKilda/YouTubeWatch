import webbrowser
import requests
from bs4 import BeautifulSoup

# open a new browser window and navigate to a webpage
url = 'https://kostaskilda.github.io/YouTubeWatch/'
webbrowser.open_new(url)

# response = requests.get(url)
# html = response.content
# soup = BeautifulSoup(html, 'html.parser')
# button = soup.find('button', {'class': 'my-button-class'})
# if button:
#     button_url = button.get('href')
#     button_data = {'button_param': 'value'}
#     response = requests.post(button_url, data=button_data)
