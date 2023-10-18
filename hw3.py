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

    def fit_transform(self, raw_documents: list[str]):
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
        self._vocabulary.clear()  # обнуляем на случай повторного вызова

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

    def get_feature_names(self):
        """	Get output feature names.
        """
        if not self._was_transformed:
            raise RuntimeError("Vocabulary is not fitted")
        return list(self._vocabulary.keys())


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(*count_matrix, sep='\n')
