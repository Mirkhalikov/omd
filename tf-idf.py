import numpy as np
from sklearn.preprocessing import normalize


class CountVectorizer:
    """Convert a collection of text documents to a matrix of token counts.

    Parameters:
    ----------
    lowercase : bool, default=True
        Convert all characters to lowercase.
    """

    def __init__(self, lowercase: bool = True):
        self.lowercase = lowercase
        self._vocabulary = dict()
        self._was_transformed = False  # определяет, был ли вызвын fit_transform

    def fit_transform(self, raw_documents: list[str]) -> list[list[int]]:
        """Learn the vocabulary dictionary and return document-term matrix.

        Parameters
        -------
        raw_documents : iterable
            A list of str.

        Returns
        -------
        X : array of shape (n_samples, n_features)
            Document-term matrix.
        """
        if self.lowercase:
            raw_documents = list(map(lambda x: x.lower(), raw_documents))

        X = []
        vocab_set = set()
        ind = 0
        for word in ' '.join(raw_documents).split():
            if word not in vocab_set:
                vocab_set.add(word)
                self._vocabulary[word] = ind
                ind += 1

        vocab_len = len(vocab_set)
        for i, words in enumerate(raw_documents):
            X.append([0] * vocab_len)
            for word in words.split():
                X[i][self._vocabulary[word]] += 1

        self._was_transformed = True
        return X

    def get_feature_names(self) -> list[str]:
        """	Get output feature names.

        Returns
        -------
        X : array of shape (n_features, )
        Consists of feature_names.
        """
        if not self._was_transformed:
            raise RuntimeError("Vocabulary is not fitted")
        return list(self._vocabulary.keys())


class TfidfTransformer:

    @staticmethod
    def tf_transform(count_matrix: list[list[int]]) -> list[list[int]]:
        """Applies tf transformation to document-term matrix (count_maxtrix).

        Parameters
        -------
        count_matrix : list[list[int]]
            A document-term matrix.

        Returns
        -------
        X : array of shape (n_samples, n_features).
        """
        rows_sums = [sum(x) for x in count_matrix]
        return [list(map(lambda x: round(x/rows_sums[i], 3), row))
                for i, row in enumerate(count_matrix)]

    @staticmethod
    def idf_transform(count_maxtrix: list[list[int]]) -> list[int]:
        """Applies idf transformation to document-term matrix (count_maxtrix).

        Parameters
        -------
        count_matrix : list[list[int]]
            A document-term matrix.

        Returns
        -------
        X : array of shape (n_features, 1).
        """
        result = []
        total = len(count_maxtrix)
        words_count = len(count_maxtrix[0])
        for word_num in range(words_count):
            count = 0
            for doc in count_maxtrix:
                if doc[word_num] > 0:
                    count += 1
            result.append(round(np.log((total + 1) / (count + 1)), 3) + 1)
        return result

    def fit_transform(self, count_matrix: list[list[int]]) -> list[list[int]]:
        """Applies tf-idf transformation to document-term matrix (count_maxtrix).

        Parameters
        -------
        count_matrix : list[list[int]]
            A document-term matrix.

        Returns
        -------
        X : array of shape (n_samples, n_features).
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf_line = self.idf_transform(count_matrix)
        return [[round(tf * idf, 3) for tf, idf in zip(tf_line, idf_line)]
                for tf_line in tf_matrix]


class TfidfVectorizer(CountVectorizer):
    """Convert a collection of raw documents to a matrix of TF-IDF features.

    Parameters:
    ----------
    lowercase : bool, default=True
        Convert all characters to lowercase.
    """

    def __init__(self):
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """Learn vocabulary and idf, return document-term matrix.

        Parameters
        -------
        count_matrix : list[list[int]]
            A document-term matrix.

        Returns
        -------
        X : array of shape (n_samples, n_features).
        """
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == '__main__':

    print('-------------------Task 1-------------------\n')

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names(), '\n')
    print(*count_matrix, sep='\n')

    print('\n-------------------Task 2-------------------\n')

    # Сразу запихнул tf и idf transform в TfidfTransformer, чтобы
    tf_matrix = TfidfTransformer.tf_transform(count_matrix)
    print(*tf_matrix, sep='\n')

    print('\n-------------------Task 3-------------------\n')

    idf_matrix = TfidfTransformer.idf_transform(count_matrix)
    print(idf_matrix)

    print('\n-------------------Task 4-------------------\n')

    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(*tfidf_matrix, sep='\n')

    print('\n-------------------Task 5-------------------\n')

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names(), '\n')

    print(*tfidf_matrix, sep='\n')
