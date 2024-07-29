import re
import nltk

from graph.co_occurence import CoOccurence
from graph.tokenizer import Tokenizer

nltk.download('brown')
nltk.download('gutenberg')
from nltk.corpus import brown
from nltk.corpus import gutenberg

co_occurence = CoOccurence()
print(f"Lenght: {len(brown.sents()[:])}")
co_occurence.add_sentences(brown.sents()[:1000])
co_occurence.add_sentences(brown.sents()[:1000])
print(co_occurence.graph.find_highest_connection())
#co_occurence.add_sentences([["He's", "a", "dogs", "said", "best", "or", "better"]])


exit(0)

tokenizer = Tokenizer()



#Downloads and cleans text corpuses from brown university (brown) and the Gutenberg library (gutenberg).

print(f"Brown type {brown}")
print(f"Brown word type {brown.words()}")
print(f"Brown word length {len(brown.words())}")
print(f"Brown word length {len(brown.words()[:])}")

clean_brown = tokenizer.tokenize(brown.words()[:])
clean_gutenburg = tokenizer.tokenize(gutenberg.words()[:])

print(f"Brown word length after tokenizer {len(clean_brown)}")


tokenizer.tokenize_sentence()



# co_occurence.add_document(brown.words()[:])

def clean_text(sentence):
    sentence = re.sub("[%s]" % re.escape(string.punctuation), "", sentence.lower())
    sentence = re.sub("([^\x00-\x7F])+", " ", sentence)    
    sentence = sentence.replace('\n', ' ').replace('.', ' ').replace(',', ' ').replace('?', ' ')\
    .replace('\r', ' ').replace('!', ' ').replace('"\r', ' ').replace('"', ' ')\
    .replace("'", ' ').replace("''", ' ').replace('(', ' ').replace(')', ' ').replace(']', ' ')\
    .replace('-', ' ').replace('/', ' ')
    
    while ('  ' in sentence):
        sentence = sentence.replace('  ', ' ')
    return sentence

from nltk.corpus import stopwords
eng_stopwords = set(stopwords.words('english')) | {''}

def get_words(sentence, stopwords):
    words = set(sentence.split(' '))
    words = list(words-set(stopwords))
    if '' in words:
        words.remove('')   
    return list(words)