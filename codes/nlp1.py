from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print X_train_counts.shape



tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print X_train_tf.shape

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print X_train_tfidf.shape

clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)





