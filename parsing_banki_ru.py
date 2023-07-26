import requests
from bs4 import BeautifulSoup as Bs
import numpy as np

num_of_pages = 70

url1 = 'https://www.banki.ru/services/responses/list/?page='
url2_positive = '&is_countable=on&rate[]=4&rate[]=5'
url2_negative = '&is_countable=on&rate[]=1&rate[]=2'
url2_neutral = '&is_countable=on&rate[]=3'


url_root = 'https://www.banki.ru'


def get_set_of_links(url_new_intro):
    list_of_links = []
    res = requests.get(url_new_intro)
    soup = Bs(res.text, 'html.parser')

    for link2 in soup.find_all('a'):
        if link2.get('href')[:34] == "/services/responses/bank/response/" and len(link2.get('href')) == 43:
            # print(link.get('href'))
            list_of_links.append(link2.get('href'))
    set_of_links = set(list_of_links)
    return set_of_links


def get_reviews(set_of_links):
    list_of_revs = []
    for link1 in set_of_links:
        # print('rev')
        url_of_review = url_root + link1
        res_of_review = requests.get(url_of_review)
        soup_of_review = Bs(res_of_review.text, 'html.parser')
        # print(soup_of_review.p)
        list_of_revs.append(soup_of_review.p)
    return list_of_revs


'''Positive reviews'''
list_of_revs_links = []
for page in range(1, num_of_pages):
    print(1)
    url_new = url1 + str(page) + url2_positive
    list_rev_links = get_set_of_links(url_new)
    list_of_revs_links += list_rev_links
    # print(list_of_revs_links)

print(np.shape(list_of_revs_links))
list_of_reviews = get_reviews(list_of_revs_links)

with open('data/reviews_positive.txt', 'w') as f:
    for line in list_of_reviews:
        f.write("%s\n" % line)

'''Neutral reviews'''
list_of_revs_links = []
for page in range(1, num_of_pages):
    print(2)
    url_new = url1 + str(page) + url2_neutral
    list_rev_links = get_set_of_links(url_new)
    list_of_revs_links += list_rev_links
    # print(list_of_revs_links)

print(np.shape(list_of_revs_links))
list_of_reviews = get_reviews(list_of_revs_links)

with open('data/reviews_neutral.txt', 'w') as f:
    for line in list_of_reviews:
        f.write("%s\n" % line)


'''Negative reviews'''
list_of_revs_links = []
for page in range(1, num_of_pages):
    print(3)
    url_new = url1 + str(page) + url2_negative
    list_rev_links = get_set_of_links(url_new)
    list_of_revs_links += list_rev_links
    # print(list_of_revs_links)

print(np.shape(list_of_revs_links))
list_of_reviews = get_reviews(list_of_revs_links)

with open('data/reviews_negative.txt', 'w') as f:
    for line in list_of_reviews:
        f.write("%s\n" % line)
