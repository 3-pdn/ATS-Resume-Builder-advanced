# train_model.py - train a simple ML classifier (TF-IDF + LogisticRegression) on sample resumes
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

DATA = 'data/sample_resumes.csv'
MODEL_DIR = 'models'
os.makedirs(MODEL_DIR, exist_ok=True)

def main():
    df = pd.read_csv(DATA)
    X = df['text'].fillna('')
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    vec = TfidfVectorizer(ngram_range=(1,2), max_features=5000)
    Xtr = vec.fit_transform(X_train)
    clf = LogisticRegression(max_iter=1000)
    clf.fit(Xtr, y_train)
    acc = clf.score(vec.transform(X_test), y_test)
    print('Test accuracy:', acc)
    joblib.dump({'vectorizer': vec, 'model': clf}, os.path.join(MODEL_DIR, 'tfidf_lr.joblib'))
    print('Saved model to', MODEL_DIR)

if __name__ == '__main__':
    main()
