from nltk.tokenize import word_tokenize
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from typing import List

import nltk
import string
import contractions

class Tokenizer:
# https://www.guru99.com/de/pos-tagging-chunking-nltk.html
# https://www.guru99.com/pos-tagging-chunking-nltk.html
# https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
    def __init__(self, word_tags: List[str]) -> None:
        try:
            #Check for punkt dataset and download if it doesn't not exist
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')

        nltk.download('averaged_perceptron_tagger')
        nltk.download('stopwords')
        nltk.download("wordnet")

        self.wl = WordNetLemmatizer()

    def tokenize(self, original_seq: list[str]):
        #Given a list of strings remove alpha numeric elements and make everything lowercase. (And include periods ".")
        seq = []
        for t in original_seq:
            if t.isalnum() or t == ".":
                seq.append(t.lower())
            else:
                print(t)
        return seq
    
    def tokenize_words(self, words: list[str]):
        pass

    def tokenize_sentence(self, sentence: str):
        pass

    def get_word_seq(self, text):
        #convert text document into a list of words.
        seq = []
        for t in word_tokenize(text):
            if t.isalnum() or t == ".":
                seq.append(t.lower())
        return seq

    def seq_to_sentence(self, seq):
        #convert a sequence of words into a sentence.
        return ' '.join(seq)
    
    def remove_stop_words(self, words: list[str]) -> list[str]:
        stop_words = set(stopwords.words('english') + list(string.punctuation))

        # Remove stop words from each tweet list of words
        # brown_nsw = [[word for word in brown_words if not word in stop_words]
        #             for brown_words in brown.sents()]
        
        stopword_free_words = []
        for word in words:
            if not word in stop_words and word.isalnum():
                stopword_free_words.append(word)

        return stopword_free_words
    
    from nltk.corpus import wordnet as wn

    tag_mapping = {
        "a": ['JJ', 'JJR', 'JJS'],
        "v": ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],
        "n": ['NN', 'NNS', 'NNP', 'NNPS'],
        "r": ['RB', 'RBR', 'RBS']
    }

    def lemmatize_words(self, words: list[str]) -> list[str]:
        from nltk.corpus import wordnet as wn
        from nltk.stem.wordnet import WordNetLemmatizer
        from nltk import word_tokenize, pos_tag
        from collections import defaultdict
        tag_map = defaultdict(lambda : wn.NOUN)
        tag_map['J'] = wn.ADJ
        tag_map['V'] = wn.VERB
        tag_map['R'] = wn.ADV

        # lemma_function = WordNetLemmatizer()
        lemmatized_sen = []
        for token, tag in pos_tag(words):
            lemma = self.wl.lemmatize(token, tag_map[tag[0]])
            #print(token, "=>", lemma)
            lemmatized_sen.append(lemma.lower())

        return lemmatized_sen
        tags = pos_tag(words)

        return [self.wl.lemmatize(tag[0], pos=self.tag_mapping[tag[1]]) for tag in tags]
        # return self.wl.lemmatize(tag[0], pos=penn_to_wn(tag[1]))
        self.tag_mapping

    def expand_contractions(self, words: list[str]) -> list[str]:
        expanded_words = []
        for word in words:
            expanded_word = contractions.fix(word)
            if expanded_words == word:
                expanded_words.append(word)
            else:
                expanded_words.extend(word_tokenize(expanded_word))
        return expanded_words

    # def is_noun(tag):
    #     return tag in ['NN', 'NNS', 'NNP', 'NNPS']


    # def is_verb(tag):
    #     return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


    # def is_adverb(tag):
    #     return tag in ['RB', 'RBR', 'RBS']


    # def is_adjective(tag):
    #     return tag in ['JJ', 'JJR', 'JJS']

    # https://www.nltk.org/_modules/nltk/stem/wordnet.html
    # def penn_to_wn(tag):
    #     if is_adjective(tag):
    #         return "a"
    #         return wn.ADJ
    #     elif is_noun(tag):
    #         return "n"
    #         return wn.NOUN
    #     elif is_adverb(tag):
    #         return "r"
    #         return wn.ADV
    #     elif is_verb(tag):
    #         return "v"
    #         return wn.VERB
    #     return None