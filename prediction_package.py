import re
import pymorphy3
from joblib import load


morph = pymorphy3.MorphAnalyzer()
special_characters = ['</p>', '\xa0', '<br/>', '\n', '-&gt;']

stop_words = ['в', 'на', 'с', 'и', 'я', 'о', 'к', 'а', 'за', 'по',
              'об', 'у', 'бы', 'от', 'ли', 'ул', 'что', 'со', 'из',
              'для', 'про', 'г', 'до', 'то', 'быть', 'по', 'мочь',
              'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
              'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь', 'год',
              'стать', 'это', 'когда', 'даже', 'янв', 'фев', 'апр', 'авг',
              'сен', 'окт', 'ноя', 'дек', 'ые', 'ый', 'ым', 'ых', 'ая']


def cleansing(text: list) -> list:
    """ Removes numbers, special characters
        and Roman alphabet characters from raw data.
        Converts all characters to lowercase """
    res = []
    for i in range(len(text)):
        res.append(text[i])
        for sp_ch in special_characters:
            res[i] = (text[i].replace(sp_ch, ' '))
        res[i] = res[i].lower()
        res[i] = re.sub(r'[^\w\s]', ' ', res[i])
        res[i] = re.sub(r'[^\w\s]+|[\d]+', r' ', res[i]).strip()
        res[i] = re.sub('[a-zA-Z\s]+', ' ', res[i])
        res[i] = re.sub(" +", " ", res[i])

    return res


def lemmatize(sentence: str) -> list:
    """ Converts each word in a sentence to its initial form"""
    words = sentence.split()  # Split sentence into words
    res = list()
    for word in words:
        p = morph.parse(word)[0]
        res.append(p.normal_form)
    return res


def delete_stop_words(sentence: list) -> list:
    """ Removes stop-words from a sentence """
    res = list()
    for word in sentence:
        if word not in stop_words:
            res.append(word)
    return res


def join(sentence: list) -> str:
    """ Joins list sentence into a string """
    return ' '.join(sentence)


def processing_pipeline(reviews):
    """ Passes raw data through all processing methods """
    cleansed_reviews = cleansing(reviews)
    lemmatized_reviews = list(map(lemmatize, cleansed_reviews))
    clean_reviews = list(map(delete_stop_words, lemmatized_reviews))
    final_reviews = list(map(join, clean_reviews))
    return final_reviews


def make_prediction(vectorizer_name: str, model_name: str, x: str) -> int:

    vectorizer = load(vectorizer_name)
    x_prepared = vectorizer.transform([x])
    model = load(model_name)

    y = int(model.predict(x_prepared)[0])

    return y


def str_prediction(y: int) -> str:

    if y == 1:
        prediction = ' Положительный'
    elif y == 0:
        prediction = 'Нейтральный'
    else:
        prediction = 'Негативный'

    return prediction
