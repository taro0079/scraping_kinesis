import requests
from bs4 import BeautifulSoup
import slackweb

slack = slackweb.Slack(
    url="https://hooks.slack.com/services/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"
)

url = 'https://kinesis-ergo.com/keyboards/advantage360/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
element = soup.select(
    '#main > div.fg-inner-page-nav.tk-proxima-nova > div > div > div > div > a.fg-inner-page-nav__list-item.fg-inner-page-nav__list-item--alt-color'
)

if element[0].text == 'Sold out':
    slack.notify(text='Advantage 360 is sold out now: ' + url)
else:
    slack.notify(
        text='💖💖💖💖 Advantage 360 is maybe available now !! check it out: ' + url + ' 💖💖💖💖')
