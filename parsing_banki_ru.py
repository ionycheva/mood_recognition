import requests
from bs4 import BeautifulSoup as Bs
from tqdm import tqdm

num_of_pages = 2

url1 = 'https://www.banki.ru/services/responses/list/?page='
url2_positive = '&is_countable=on&rate[]=4&rate[]=5'
url2_negative = '&is_countable=on&rate[]=1&rate[]=2'
url2_neutral = '&is_countable=on&rate[]=3'

url_root = 'https://www.banki.ru'


def get_set_of_links(url_new_intro: str) -> set:

    """ Parses links to all reviews on page """

    list_of_links = []
    res = requests.get(url_new_intro)
    soup = Bs(res.text, 'html.parser')

    for link2 in soup.find_all('a'):  # inspect all links
        if link2.get('href')[:34] == "/services/responses/bank/response/" \
                and len(link2.get('href')) == 43:  # filter links to find links to reviews
            list_of_links.append(link2.get('href'))

    set_of_links = set(list_of_links)  # removing duplicates

    return set_of_links


def get_reviews(set_of_links: list) -> list:

    """ Parses reviews by links """

    list_of_revs = []
    for link_to_rev in tqdm(set_of_links):
        url_of_review = url_root + link_to_rev
        res_of_review = requests.get(url_of_review)
        soup_of_review = Bs(res_of_review.text, 'html.parser')
        list_of_revs.append(soup_of_review.p)

    return list_of_revs


def download(url_to_revs: str, name: str):

    """ Method to get reviews from site and write it to file"""

    list_of_revs_links = []
    for page in range(1, num_of_pages):  # going through pages of site
        url_new = url1 + str(page) + url_to_revs
        list_rev_links = get_set_of_links(url_new)  # get links to reviews
        list_of_revs_links += list_rev_links
    list_of_reviews = get_reviews(list_of_revs_links)  # get reviews

    with open('data/{name}.txt'.format(name=name), 'w') as f:  # write to file
        for line in list_of_reviews:
            f.write("%s\n" % line)


print('Positive reviews are downloading')
download(url_to_revs=url2_positive, name='reviews_positive')

print('Neutral reviews are downloading')
download(url_to_revs=url2_neutral, name='reviews_neutral')

print('Negative reviews are downloading')
download(url_to_revs=url2_negative, name='reviews_negative')
