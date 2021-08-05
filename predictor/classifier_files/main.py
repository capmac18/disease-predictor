#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn import model_selection
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from pickle import dump


# In[2]:


dfTrain = pd.read_csv('dataset.csv')


# In[3]:


dfTrain.head()


# In[4]:


dfTrain["Disease"].value_counts()


# In[5]:


dfTrain.iloc[:,1:] = dfTrain.iloc[:,1:].apply(lambda x: x.str.lower())
dfTrain.iloc[:,1:] = dfTrain.iloc[:,1:].apply(lambda x: x.str.replace(' ',''))


# In[6]:


X = []
for i in range(len(dfTrain)):
    s = ' '.join(dfTrain.iloc[i, 1:].dropna().tolist())
    X.append(s)


# In[7]:


X


# In[8]:


st = set()
for row in X:
    for word in row.split():
        st.add(word)


# In[9]:


st


# In[10]:


X = np.array(X)


# In[11]:


le = LabelEncoder()
le.fit(dfTrain["Disease"])
le.classes_
Y = le.transform(dfTrain["Disease"])


# In[12]:


X_train, X_val, Y_train, Y_val = model_selection.train_test_split(X, Y, test_size = 0.2, random_state=100)


# In[13]:


# bag of words model
vectorizer = CountVectorizer()
X_train_model = vectorizer.fit_transform(X_train)
X_val_model = vectorizer.transform(X_val)

X_train_model = X_train_model.toarray()
X_val_model = X_val_model.toarray()


# In[14]:


clf = MultinomialNB()
clf.fit(X_train_model, Y_train)


# In[15]:


Y_train_model_pred = clf.predict(X_train_model)
accuracy_score(Y_train, Y_train_model_pred)


# In[16]:


clf.predict_proba(X_train_model)


# In[17]:


Y_train


# In[18]:


Y_val_model_pred = clf.predict(X_val_model)
accuracy_score(Y_val, Y_val_model_pred)


# In[19]:


def n_probable_diseases(clf, X_test, n=5):
    Y_pred = clf.predict_proba(X_test)
    
    for i in range(len(Y_pred)):
        ls = Y_pred[i]
        zipls = zip(ls, list(range(len(Y_pred[0]))))
        zipls = list(sorted(zipls, reverse=True))
        #print(i , len(ls)," : ")
        for j in range(n):
            prob, label = zipls[j]
            print(le.inverse_transform([label])[0], f"( {prob*100:.5f} % )", end='      ')
        print('\n')


# In[20]:


X_test = ['chest_pain high_fever headache', 'chest_pain acidity', 'high_fever headache']
X_test = vectorizer.transform(X_test)
X_test = X_test.toarray()


# In[21]:


X_test.shape


# In[22]:


n_probable_diseases(clf, X_test, 3)


# In[25]:


dump(clf, open('classifier.pkl', 'wb'))
dump(le, open('labelencoder.pkl', 'wb'))
dump(vectorizer, open('countvectorizer', 'wb'))


# In[ ]:




