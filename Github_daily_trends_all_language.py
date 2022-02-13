import requests
from bs4 import BeautifulSoup
import pprint
from pandas import read_csv

PATH_TO_DATA = 'Fonti_github.csv'

def get_trading_repositories():
    lista = read_csv(PATH_TO_DATA).url.tolist()
    for url in lista:
        url_to_call = url
        print("Linguage " + str(url_to_call[28:-12])+ "\n")
        response = requests.get(url_to_call, headers={'User-Agent': "Mozilla/5.0"})
        response_code = response.status_code
        if response_code != 200:
            print("errore")
            return
        html_content = response.content
        dom = BeautifulSoup(html_content, 'html.parser')
        all_tranding_repos = dom.select("article.Box-row")
        trending_repositories =[]
        for each_trending_repo in all_tranding_repos:
            try:
                titolo = each_trending_repo.find('p','col-9 color-fg-muted my-1 pr-4').text.strip()
            except Exception as e: 
                titolo1 = each_trending_repo.find('p','col-9 color-fg-muted my-1 pr-4')
                titolo = str(titolo1)
            href_link = each_trending_repo.h1.a.attrs["href"]
            name = href_link[1:]
            repo = {"label": name,
                    "Description": titolo,
                    "link": "https://github.com{}".format(href_link)
                    }
            trending_repositories.append(repo)
            pprint.pprint(repo)
            print("\n")
    #return trending_repositories
    print(" #### END !! #### ")




if __name__ == "__main__":
    print("Scrapy daily trends 4 all lenguage .. ")
    trending_repos = get_trading_repositories()
    #pprint.pprint(trending_repos)

get_trading_repositories()
