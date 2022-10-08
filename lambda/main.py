import requests
from bs4 import BeautifulSoup
import slackweb
import os
from dotenv import load_dotenv


def main():

    load_dotenv()

    slack = slackweb.Slack(
        url=os.environ["SLACK_WEBHOOK_URL"]
    )

    url = 'https://kinesis-ergo.com/keyboards/advantage360/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    element = soup.select(
        '#main > div.fg-inner-page-nav.tk-proxima-nova > div > div > div > div > a.fg-inner-page-nav__list-item.fg-inner-page-nav__list-item--alt-color'
    )

    if element[0].text == 'Sold out':
        # slack.notify(text='Advantage 360 is sold out now: ' + url)
        print('Advantage 360 is sold out now')
    else:
        slack.notify(
            text='💖💖💖💖 Advantage 360 is maybe available now !! check it out: ' + url + ' 💖💖💖💖')


if __name__ == '__main__':
    main()
