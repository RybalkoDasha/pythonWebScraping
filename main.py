import requests as requests
import bs4



def get_articles():


    HEADERS = {
        'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
        'Accept-Language': 'ru-RU,ru;q=0.9',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
        'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'sec-ch-ua-mobile': '?0'
        }
    response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
    response.raise_for_status()
    text = response.text
    # return text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    article = soup.find_all('article')
    # print(article)
    for art in article:
        # print(art)
        article_title = art.find('h2')
        # print(article_title.text)
        article_hub = art.find_all('a', class_="tm-article-snippet__hubs-item-link")
        article_hub = [hub.find('span').text for hub in article_hub]
        # print(article_hub)
        article_tag = article_title.find('a')
        href = article_tag.attrs['href']
        article_link = 'https://habr.com' + href
        # print(article_link)
        # print('----')
        date_info = art.find('span', class_="tm-article-snippet__datetime-published")
        # print(date_info)
        date_article = date_info.find('time')['title']
        # print(date_article)
        for word in KEYWORDS:
            if word in art.text or word.title() in art.text:
                print(f'<{date_article}> - {article_title.text} - <{article_link}>')


if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    get_articles()


