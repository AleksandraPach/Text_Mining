from cleaning import text_tokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics
import pandas as pd

df_true = pd.read_csv('Datasets/True.csv', usecols=['title', 'text'])
df_fake = pd.read_csv('Datasets/Fake.csv', usecols=['title', 'text'])
df_true["type"] = 1
df_fake["type"] = 0

df = pd.concat([df_true, df_fake])


def main():
    vectorizer_count = CountVectorizer(tokenizer=text_tokenizer)
    count_transform = vectorizer_count.fit_transform(df['title'])
    x_train, x_test, y_train, y_test = train_test_split(count_transform, df['type'], test_size=0.33, random_state=42)
    # pojedyncze drzewo decyzyjne;
    clf_tree = DecisionTreeClassifier().fit(x_train, y_train)
    y_pred = clf_tree.predict(x_test)
    print("Accuracy of Decission Tree:", round(metrics.accuracy_score(y_test, y_pred), 2))
    # lasy losowe
    clf_forecast = RandomForestClassifier().fit(x_train, y_train)
    y_pred = clf_forecast.predict(x_test)
    print("Accuracy of Random Forecast:", round(metrics.accuracy_score(y_test, y_pred), 2))
    # SVM
    clf_svm = LinearSVC().fit(x_train, y_train)
    y_pred = clf_svm.predict(x_test)
    print("Accuracy of SVM:", round(metrics.accuracy_score(y_test, y_pred), 2))
    # AdaBoost
    clf_ada = AdaBoostClassifier().fit(x_train, y_train)
    y_pred = clf_ada.predict(x_test)
    print("Accuracy of AdaBoost:", round(metrics.accuracy_score(y_test, y_pred), 2))
    # Bagging
    clf_bagging = BaggingClassifier().fit(x_train, y_train)
    y_pred = clf_bagging.predict(x_test)
    print("Accuracy of Bagging:", round(metrics.accuracy_score(y_test, y_pred), 2))


main()
