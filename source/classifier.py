from joblib import load
from numpy import vectorize

class Classifier:

    __clf = None
    __vectorizer = None

    def __init__(self) -> None:
        # these are pretrained models
        self.__clf = load("objects\\articleclassifier.joblib") # loading the classifier file
        self.__vectorizer = load("objects\\tfidfvectorizer.joblib") # loading the vectorizor file
    
    def get_probabilities(self, article_text): # returns the probability of an article being real or fake
        sample = [article_text]
        sample = self.__vectorizer.transform(sample)
        
        return self.__clf._predict_proba_lr(sample)

    def classify(self, article_text): # returns the raw classification conclusion, not currently used
        sample = [article_text]
        sample = self.__vectorizer.transform(sample)

        return self.__clf.predict(sample)