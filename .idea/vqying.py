
import codecs
import requests
from bs4 import BeautifulSoup



DOWNLOAD_URL = 'http://v.iqying.com/lib/1-1---0-0---.html/'
True_URL='http://v.iqying.com'


def download_page(url):
    return requests.get(url).content

def parse_html(html):
    soup = BeautifulSoup(html,"html.parser")
    movie_list_soup = soup.find('div',attrs={'class':'wrap_d list_d'})
    movie_name_list = []
    for movie_li in movie_list_soup.find_all('li'):
        movie_name = movie_li.find('a',attrs={'class':'v_title'}).getText()
        movie_name_list.append(movie_name)
    next_page = soup.find('div', attrs={'class': 'pages'})
    a = next_page.find_all('a',attrs={'class':'pagelink_a'})
    if  a[-2]:
        return movie_name_list, True_URL + a[-2]['href']
    return movie_name_list,None

def main():
    url = DOWNLOAD_URL
    with codecs.open('movies', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))

if __name__ == '__main__':
    main()