from pickle import load
import os


def predict(X_test, n=5):

    clf = load(open('predictor/classifier_files/classifier.pkl', 'rb'))
    le = load(open('predictor/classifier_files/labelencoder.pkl', 'rb'))
    vectorizer = load(open('predictor/classifier_files/countvectorizer', 'rb'))
    X_test = vectorizer.transform(X_test)
    X_test = X_test.toarray()

    Y_pred = clf.predict_proba(X_test)

    ans = []
    for i in range(len(Y_pred)):
        ls = Y_pred[i]
        zipls = zip(ls, list(range(len(Y_pred[0]))))
        zipls = list(sorted(zipls, reverse=True))
        #print(i , len(ls)," : ")
        for j in range(n):
            prob, label = zipls[j]
            #print(le.inverse_transform([label])[0], f"( {prob*100:.5f} % )", end='      ')
            ans.append([le.inverse_transform([label])[0], f"{prob*100:.5f} %"])
        # print('\n')
    return ans