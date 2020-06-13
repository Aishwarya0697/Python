from interfaces.preprocessing_interface import preprocessing_interface
from bs4 import BeautifulSoup
import unicodedata
from preproceesing.contractions import CONTRACTION_MAP
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk
import string
from nltk.chunk import conlltags2tree, tree2conlltags





class NLTK_preprocessing(preprocessing_interface):

    def __init__(self, text):
        self._text = text
        self._result = None


    def remove_html_tags(self, parameter_dictionary):
        soup = BeautifulSoup(self._text, "html.parser")
        self._text = soup.get_text(separator=" ")
        return self._text

    def remove_accented_chars(self, parameter_dictionary):
        self._text = unicodedata.normalize('NFKD', self._text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        return self._text

    def remove_emails(self,parameter_dictionary):
        sentence=self._text
        emails=re.compile("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
        self._text= re.sub(emails,"",sentence)
        return self._text

    def remove_unicode(self, parameter_dictionary):
        self._text = (self._text.encode("ascii", "ignore")).decode("utf-8")
        return self._text




    def expand_contractions(self,parameter_dictionary,contraction_mapping=CONTRACTION_MAP):
        text=self._text
        contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),
                                          flags=re.IGNORECASE | re.DOTALL)

        def expand_match(contraction):
            match = contraction.group(0)
            first_char = match[0]
            expanded_contraction = contraction_mapping.get(match) \
                                    if contraction_mapping.get(match) \
                                    else contraction_mapping.get(match.lower())
            expanded_contraction = first_char + expanded_contraction[1:]
            return expanded_contraction

        self._text= contractions_pattern.sub(expand_match, text)
        self._text = re.sub("'", "", self._text)
        return self._text


    def remove_specialcharacter(self, parameter_dictionary):
        self._text = " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\s+)", " ", self._text).split())
        return self._text



    def remove_punctuations(self, parameter_dictionary):
        punctuations = string.punctuation
        for w in self._text:
            if w in punctuations:
                self._text.remove(w)
        return self._text


    def tokenization(self, parameter_dictionary):
        token_type = parameter_dictionary.get("token type", "word")
        if token_type == "word":
            result = word_tokenize(self._text)

        else:
            result = sent_tokenize(self._text)

        self._result = result
        return self._result

    def remove_number(self, parameter_dictionary):
        self._result = [i for i in self._result if not i.isdigit()]
        return self._result


    # def lemmatization(self,parameter_dictionary):
    #     word_lemma = WordNetLemmatizer()
    #     result = word_tokenize(self._text)
    #     self._result =[word_lemma if word_lemma != '-PRON-' else word.result for word in result]
    #     return self._result

    def stemming(self, parameter_dictionary):
        self._result1 = []
        ps = PorterStemmer()
        for w in self._result:
            rootWord = ps.stem(w)
            self._result1.append(rootWord)
        return self._result1


    def remove_stopword(self, parameter_dictionary):
        stop_words = set(stopwords.words('english'))
        self._result2 = []
        for w in self._result1:
            if w not in stop_words:
                self._result2.append(w)
        return self._result2


    def pos(self, parameter_dictionary):
        self._result3 = nltk.pos_tag(self._result2)
        return self._result3


    def NER(self, parameter_dictionary):
        pattern = 'NP:{<.*>+}'  # chunk everythings
        cp = nltk.RegexpParser(pattern)
        self._result4 = cp.parse(self._result3)
        # return self._result5
        self._result5 = tree2conlltags(self._result4)  # chunk in tree format
        return self._result5




if __name__ == "__main__":
    nk = NLTK_preprocessing("<html><h2>Some important text</h2></html>"
                            "\n Sómě Áccěntěd těxt, mobile no 7887731338 , email id is ghadgeaishwarya@gmail.com"
                            "\n Y'all can't expand contractions I'd think"
                            "\n Well this was fun! What do you think? 123#@!"
                            "\n My system keeps crashing! his crashed yesterday, ours crashes daily")


    print("\n", nk.remove_html_tags({"token type": "word"}))
    print("\n", nk.remove_accented_chars({}))
    print("\n", nk.remove_emails({"token type": "word"}))
    print("\n", nk.remove_unicode({"token type": "word"}))
    print("\n", nk.expand_contractions({"token type": "word"}))
    print("\n", nk.remove_specialcharacter({"token type": "word"}))
    print("\n", nk.remove_punctuations({"token type": "word"}))
    print("\n", nk.tokenization({"token type": "word"}))
    print("\n", nk.remove_number({"token type": "word"}))
    # print("\n", nk.lemmatization({}))
    print("\n", nk.stemming({"token type": "word"}))
    print("\n", nk.remove_stopword({"token type": "word"}))
    print("\n", nk.pos({"token type": "word"}))
    print("\n", nk.NER({"token type": "word"}))

