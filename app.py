from models_result import models_predict
from fastapi import FastAPI,Query 
import uvicorn 

#init app
app=FastAPI()

#Routes
#http://127.0.0.1:8000/
@app.get('/')
async def index():
	return {"Api":"Welcome To Disease Prediction Api"}



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
