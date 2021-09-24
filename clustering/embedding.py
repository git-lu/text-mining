from matplotlib import pylab as plt
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.manifold import TSNE
from collections import defaultdict


class WordEmbedding():
    def __init__(
        self,
        wv=None,
        vectors=None,
        index_to_words=None
    ):
        if not wv or (vectors and index_to_words):
            print("Please provide either vw or vectors list and index_to_word")
        self.wv = wv
        self.vectors = vectors
        self.index_to_words = index_to_words
        if self.wv:
            self.vectors = self.wv.vectors
            self.index_to_words = self.wv.index2word

    def plot_tsne_proyection(
        self,
        id_range=(200, 600)
    ):
        # obtener las palabras más comunes en el corpus, entre la 200 y la 600
        words = [word for word in self.wv.index2word[id_range[0]:id_range[1]]]

        # convertirlas a vector
        embeddings = [self.wv[word] for word in words]

        #  T-SNEde
        words_embedded = TSNE(
            n_components=2, random_state=1).fit_transform(embeddings)

        # ... and visualize!
        plt.figure(figsize=(20, 20))
        for i, label in enumerate(words):
            x, y = words_embedded[i, :]
            plt.scatter(x, y)
            plt.annotate(label, xy=(x, y), xytext=(5, 2), textcoords='offset points',
                         ha='right', va='bottom', size=11)
        plt.show()

    def train_clustering(
            self,
            clustering_method='kmeans',
            n_clusters=100
    ):
        X = self.vectors
        if clustering_method == 'kmeans':
            self.kmeans = KMeans(
                n_clusters=n_clusters,
                random_state=0).fit(X)
            self.labels = self.kmeans.labels_
        if clustering_method == 'agglomerative':
            self.agc = AgglomerativeClustering(
                affinity='cosine',
                n_clusters=n_clusters,
                linkage='average')
            self.agc.fit_predict(self.vectors)
            self.labels = self.agc.labels_

        self.clusters = defaultdict(list)
        for word, label in zip(self.index_to_words, self.labels):
            self.clusters[label].append(word)

    def print_clustering_results(self, n=10):
        for cluster, words in self.clusters.items():
            print(cluster)
            print(words)
            print()
            print("----------------------------------------")
