from models_result import models_predict
from fastapi import FastAPI,Query 
import uvicorn 
import requests as req

#init app
app=FastAPI()

#Routes
#http://127.0.0.1:8000/
@app.get('/')
async def index():
	return {"Api":"Welcome To Disease Prediction Api"}


##for calculating BMI
##http://127.0.0.1:8000/bmi?hfeet=6&hinches=1&weight=100

@app.get('/bmi')
async def BMI(hfeet:float= Query(None),hinches:float= Query(None),weight:float= Query(None)):
	height=(12*hfeet+hinches)*0.0254 #inches to meter conversion
	bmi = weight/(height**2)
	bmi="Your BMI is: {:.1f}".format(bmi)
	return bmi

#countries list
@app.get('/countries')
async def country():
    l=[]
    url="http://emergencynumberapi.com/api/data/all"
    r=req.get(url)
    w=r.json()
    for i in w:
        if i['Ambulance']['All'][0]!=None:
            l.append(i['Country']['Name'])
    return l

@app.get('/country')
async def getContactByCountry(country:str=Query(None)):
    l=[]
    url="http://emergencynumberapi.com/api/data/all"
    r=req.get(url)
    w=r.json()
    for i in w:
        if country==i['Country']['Name']:
            l.append(i['Ambulance']['All'])
            break
    if l[0][0]!=None:
        return l[0][0]
    
    

@app.get('/predict')
async def predict(s1:str= Query(None),s2:str= Query(None),s3:str= Query(None),s4:str= Query(None),s5:str= Query(None)):
	
	s1=s1.replace("(","")
	s1=s1.replace(")","")
	s2=s2.replace("(","")
	s2=s2.replace(")","")
	s3=s3.replace("(","")
	s3=s3.replace(")","")
	s4=s4.replace("(","")
	s4=s4.replace(")","")
	s5=s5.replace("(","")
	s5=s5.replace(")","")
	psymptoms=[s1,s2,s3,s4,s5]
	print(psymptoms)
	return models_predict(psymptoms)






#uvicorn.run(app,port=5000)
#psymptoms=['watering_from_eyes','constipation','mild_fever','irritation_in_anus','muscle_pain']
#print(models_predict(psymptoms))

#http://127.0.0.1:5000/predict?s1=watering_from_eyes&s2=constipation&s3=mild_fever&s4=irritation_in_anus&s5=muscle_pain
