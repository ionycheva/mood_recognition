# mood_recognition
 
Project for recognition mood of review.

1. [parsing_banki_ru.py](https://github.com/ionycheva/mood_recognition/blob/main/parsing_banki_ru.py) 
file is getting reviews from [this site](https://www.banki.ru/)

2. [dataset_maker.ipynb](https://github.com/ionycheva/mood_recognition/blob/main/dataset_maker.ipynb) 
notebook is preparing and saving data for further use. 
It's cleansing text from special characters and stop-words, lemmatize each word in reviews. 
It also vectorize data via [TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer) method.

3. [model_maker_only_positive_and_negative.ipynb](https://github.com/ionycheva/mood_recognition/blob/main/model_maker_only_positive_and_negative.ipynb) notebook is separates data into training and test datasets, vectorize it by TF-IDF matrix from previous step. 
Then creating [SVC-model](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html) and fits it with data. This notebook saves resulting classifier and calculates its accuracy.
   (Reviews are separates as positive and negative. Rating 3 set as negative.)
4. [model_maker_3_as_neutral.ipynb](https://github.com/ionycheva/mood_recognition/blob/main/model_maker_3_as_neutral.ipynb) notebook are similar with previous item with one difference: 
It's separates data adding neutral mood if rating is 3. It usually gives worse results because rating 3 is used as negative mark.
5. [make_prediction.ipynb](https://github.com/ionycheva/mood_recognition/blob/main/make_prediction.ipynb) file are used to estimate raw review with gotten classifier.



