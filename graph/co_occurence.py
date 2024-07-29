import collections
import itertools
import logging.config
from nltk.corpus import stopwords
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from nltk import pos_tag
import nltk
from nltk.stem import WordNetLemmatizer

from nltk import ngrams, bigrams
from nltk.corpus import wordnet as wn

import logging

from graph.tokenizer import Tokenizer
from graph.graph import Graph

from typing import List

logging.basicConfig(level=logging.INFO)

# https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-bigrams/
# https://www.kaggle.com/code/xxxxyyyy80008/analyze-co-occurrence-and-networks-of-words
# https://www.kaggle.com/code/itoeiji/simple-co-occurrence-network

class CoOccurence:

    def __init__(self, noun: bool = True, verb: bool = True, adjective: bool = True, adverb: bool = True, n_gram: int = 2) -> None:
        # nltk.download('stopwords')
        # stop_words = set(stopwords.words('english'))

        # Remove stop words from each tweet list of words
        # tweets_nsw = [[word for word in tweet_words if not word in stop_words]
        #             for tweet_words in words_in_tweet]

        # self.noun: bool = noun
        # self.verb: bool = verb
        # self.adjective: bool = adjective
        # self.adverb: bool = adverb

        self.word_tags: List[str] = []
        if noun: self.word_tags.extend(['NN', 'NNS', 'NNP', 'NNPS'])
        if verb: self.word_tags.extend(['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'])
        if adjective: self.word_tags.extend(['JJ', 'JJR', 'JJS'])
        if adverb: self.word_tags.extend(['RB', 'RBR', 'RBS'])

        self.n_gram = n_gram

        self.tokenizer = Tokenizer(self.word_tags)
        self.graph = Graph()

    # def add_document(self, sentences: list[str]):
    #     for sentence in sentences:
            

    def create_n_grams(self, n: int, sentences: list[str]):
        # Create list of lists containing bigrams 
        n_grams = [list(ngrams(words, 3)) for words in sentences]

        # View bigrams for the first assay
        print('View N-grams (N=3) for the first assay')
        print(n_grams[0][:5])

        gram3_list = list(itertools.chain(*n_grams))

        # Create counter of words in clean bigrams
        gram3_counts = collections.Counter(gram3_list)

        gram3_counts.most_common(5)

        # Create network plot 
        G = nx.Graph()


        for _, row in word_pairs_count.iterrows():
            G.add_edge(row['word1'], row['word2'], weight=row[0])

        pos_kkl = nx.kamada_kawai_layout(G)
        f, ax = plt.subplots(figsize=(16, 16))


        d = dict(nx.degree(G))
        edges = G.edges()
        weights = [G[u][v]['weight']/1000 for u,v in edges]

        nx.draw(G, pos_kkl, 
                with_labels=True, 
                node_size=[v * 100 for v in d.values()],
                nodelist=d.keys(),  
                width=weights, 
                edge_color='grey', #node_color=list(df_skills_stats['core_number']), cmap="coolwarm_r", 
                alpha=0.9,
            )
        #node_labels = nx.draw_networkx_labels(G, pos_kkl, labels, font_size=10)
        # Set title
        ax.set_title('Word Co-occurrence Network', 
                    fontdict={'fontsize': 26,
                    'fontweight': 'bold',
                    'color': 'salmon', 
                    'verticalalignment': 'baseline',
                    'horizontalalignment': 'center'}, 
                    loc='center')
        # Set edge color
        plt.gca().collections[0].set_edgecolor("#000000")


    def add_sentences(self, sentences: list[str]):
        clean_sentences = []
        for sen in sentences:
            # print(f"Senctence before: {sen}")
            expanded_contractions = self.tokenizer.expand_contractions(sen)
            # print(f"Senctence after contraction expand: {expanded_contractions}")
            lemmatized_sen = self.tokenizer.lemmatize_words(expanded_contractions)
            # print(f"Senctence after lemmatizing: {lemmatized_sen}")
            stopword_free_sen = self.tokenizer.remove_stop_words(lemmatized_sen)
            # print(f"Senctence after stopword removing: {stopword_free_sen}")

            clean_sentences.append([word.lower() for word in stopword_free_sen])

        # for sen in clean_sentences:
        #     sentence_bigram = list(bigrams(sen))
        #     print(f"Bigrams: {sentence_bigram}")

        # Flatten list of bigrams
        sentence_bigrams = list(itertools.chain(*[list(bigrams(sen)) for sen in clean_sentences]))

        # add bigrams to graph
        for bigram in sentence_bigrams:
            self.graph.add_bigram(bigram=bigram)

        return
        ### start new
        G = nx.Graph()

        for key, global_node in self.graph.nodes.items():
            G.add_edge(k[0], k[1], weight=(v * 10))
        ### end new


        # Create counter of words in clean bigrams
        bigram_counts = collections.Counter(sentence_bigrams)

        # print(bigram_counts.most_common(20))

        bigram_df = pd.DataFrame(bigram_counts.most_common(100), columns=["bigram", "count"])

        # print(bigram_df.head())

        # Create dictionary of bigrams and their counts
        d = bigram_df.set_index('bigram').T.to_dict('records')

        # Create network plot 
        G = nx.Graph()

        # Create connections between nodes
        for k, v in d[0].items():
            G.add_edge(k[0], k[1], weight=(v * 10))

        # G.add_node("china", weight=100)

        fig, ax = plt.subplots(figsize=(10, 8))

        pos = nx.spring_layout(G, k=2)

        # Plot networks
        nx.draw_networkx(G, pos,
                        font_size=16,
                        width=3,
                        edge_color='grey',
                        node_color='purple',
                        with_labels = False,
                        ax=ax)

        # Create offset labels
        for key, value in pos.items():
            x, y = value[0]+.135, value[1]+.045
            ax.text(x, y,
                    s=key,
                    bbox=dict(facecolor='red', alpha=0.25),
                    horizontalalignment='center', fontsize=13)
            
        plt.show()


        # Maybe only nouns

    def plot_graph(self):
        # Create network plot 
        G = nx.Graph()

        # Create connections between nodes
        for edge in self.graph.edges:
            G.add_edge(edge.source.word, edge.destination.word, weight=(1/edge.frequence))

        # G.add_node("china", weight=100)

        fig, ax = plt.subplots(figsize=(10, 8))

        pos = nx.spring_layout(G, k=2)

        # Plot networks
        nx.draw_networkx(G, pos,
                        font_size=16,
                        width=3,
                        edge_color='grey',
                        node_color='purple',
                        with_labels = False,
                        ax=ax)

        # Create offset labels
        for key, value in pos.items():
            x, y = value[0]+.135, value[1]+.045
            ax.text(x, y,
                    s=key,
                    bbox=dict(facecolor='red', alpha=0.25),
                    horizontalalignment='center', fontsize=13)
            
        plt.show()

    def __str__(self) -> str:
        return f"Nodes: {len(self.graph.nodes)}"