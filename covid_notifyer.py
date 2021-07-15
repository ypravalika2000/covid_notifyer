from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\Praneet\\PycharmProjects\\covid_notify\\icon.ico",
        timeout=10)


def getdata(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":

    myhtmldata = getdata("https://www.worldometers.info/coronavirus/#countries")


    soup = BeautifulSoup(myhtmldata, "html.parser")

    india=""
    ind=[]

    for tr in soup.find('tbody').find_all('tr')[9].get_text():
        india+=tr

    ind.append(india.split())

    total_cases=ind[0][2]
    new_cases=ind[0][3]
    deaths=ind[0][4]
    today_deaths=ind[0][5]

    ntitle='covid cases of india'
    ntext=f"total cases={total_cases}\ntoday cases={new_cases}\ndeaths={deaths}\ntoday deaths={today_deaths}"
    notifyme(ntitle, ntext)

