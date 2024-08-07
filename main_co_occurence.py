import re
import nltk

from graph.co_occurence import CoOccurence
from graph.tokenizer import Tokenizer

# nltk.download('brown')
# nltk.download('gutenberg')
# from nltk.corpus import brown
# from nltk.corpus import gutenberg

import logging
logging.basicConfig(level=logging.INFO)

# TODO only nonce

co_occurence = CoOccurence()
# print(f"Lenght: {len(brown.sents()[:])}")
# co_occurence.add_sentences(brown.sents()[:1000])
# co_occurence.add_sentences(brown.sents()[:1000])
# print(co_occurence.graph.find_highest_connection())
example_sentences = [
    "Just as there are many variants and forms of electronic malware and Internet-based threats around the globe, so there are many forms of protection against these threats.",
    "Signature-based detection is one of the multifarious forms of defense that have been developed in order to keep us safe from malicious content.",
    "Although signature-based detection can be argued to have been overshadowed by more sophisticated methods of protection in some environments, it remains as a core ‘technique’ featuring in the anti-virus controls of packages and suites that work to protect a user’s system today.",
    "How does signature-based detection work? Signature-based detection works by scanning the contents of computer files and cross-referencing their contents with the “code signatures” belonging to known viruses.",
    "A library of known code signatures is updated and refreshed constantly by the anti-virus software vendor.",
    "If a viral signature is detected, the software acts to protect the user’s system from damage.",
    "Suspected files are typically quarantined and/or encrypted in order to render them inoperable and useless."
]
co_occurence.add_sentences(example_sentences[:1])
co_occurence.plot_graph()

# many -> 2
# form -> 2
# threat -> 2
['many', 'variant', 'form', 'electronic', 'malware', 'threat', 'around', 'globe', 'many', 'form', 'protection', 'threat']

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