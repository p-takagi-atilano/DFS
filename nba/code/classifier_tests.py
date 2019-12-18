import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm

def evaluate_models(data):
    # read in and process training dataset
    df = pd.read_csv(data)
    x_train = df.loc[:, df.columns != 'y']
    y_train = df['y']
    
    # create models
    #gnb = GaussianNB()
    #bnb = BernoulliNB()
    #mnb = MultinomialNB()
    #dtc = DecisionTreeClassifier()
    etc = DecisionTreeClassifier(criterion='entropy')
    etc.fit(x_train, y_train)
    #svc = svm.SVC()
    #nvc = svm.NuSVC()
    #lvc = svm.LinearSVC()

    # conduct cross validations using training dataset
    #gnb_scores = cross_val_score(gnb, x_train, y_train, cv=20)
    #bnb_scores = cross_val_score(bnb, x_train, y_train, cv=20)
    #mnb_scores = cross_val_score(mnb, x_train, y_train, cv=20)
    #dtc_scores = cross_val_score(dtc, x_train, y_train, cv=20)
    etc_scores = cross_val_score(etc, x_train, y_train, cv=10, scoring='accuracy')
    #svc_scores = cross_val_score(svc, x_train, y_train, cv=20)
    #nvc_scores = cross_val_score(nvc, x_train, y_train, cv=10)
    #lvc_scores = cross_val_score(lvc, x_train, y_train, cv=10)
    
    # print accuracies
    #print("gnb accuracy: %0.4f (+/- %0.4f)" % (gnb_scores.mean(), gnb_scores.std()*2))
    #print("bnb accuracy: %0.4f (+/- %0.4f)" % (bnb_scores.mean(), bnb_scores.std()*2))
    #print("mnb accuracy: %0.4f (+/- %0.4f)" % (mnb_scores.mean(), mnb_scores.std()*2))
    #print("dtc accuracy: %0.4f (+/- %0.4f)" % (dtc_scores.mean(), dtc_scores.std()*2))
    print("etc accuracy: %0.4f (+/- %0.4f)" % (etc_scores.mean(), etc_scores.std()*2))
    #print("svc accuracy: %0.4f (+/- %0.4f)" % (svc_scores.mean(), etc_scores.std()*2))
    #print("nvc accuracy: %0.4f (+/- %0.4f)" % (nvc_scores.mean(), etc_scores.std()*2))
    #print("lvc accuracy: %0.4f (+/- %0.4f)" % (lvc_scores.mean(), etc_scores.std()*2))

evaluate_models('train_ml/wa_dataset.csv')