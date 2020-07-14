from helper import disease,l1
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import joblib

#load models
RF=joblib.load("random_forest.pkl")
DT=joblib.load("decision.pkl")
NB=joblib.load("NB.pkl")
KNN=joblib.load("knn.pkl")

def predict(clf,symptoms):
  l2=[]
  for i in range(0,len(l1)):
    l2.append(0)
  for k in range(0,len(l1)):
    for z in symptoms:
      if(z==l1[k]):
        l2[k]=1

  inputtest = [l2]
  predict = clf.predict(inputtest)
  predicted=predict[0]

  h='no'
  for a in range(0,len(disease)):
    if(predicted == a):
      h='yes'
      break

  if (h=='yes'):
    return (disease[predicted])
  else:
    return ("Not Found")





#print(predict(DT,psymptoms))
#print(predict(KNN,psymptoms))
#print(predict(NB,psymptoms))
#print(predict(RF,psymptoms))

def models_predict(psymptoms):
	result={"Decision Tree":predict(DT,psymptoms),"RandomForestClassifier":predict(RF,psymptoms),"Naive Bayes":predict(NB,psymptoms),"KNN ":predict(KNN,psymptoms)}
	return result


