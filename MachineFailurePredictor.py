import uvicorn
from fastapi import FastAPI
print("uvicorn version:", uvicorn.__version__)
from MachineFailures import MachineFailure
import joblib

## Create the api object
api = FastAPI()

model = joblib.load("classifier2")

@api.get('/')
def Index():
    return {'message': 'Predictive Maintenance API'}

@api.post('/predict')
def predict_failure(data:MachineFailure):
    data = data.dict()
    print(data)
    print("Hello")
    airtemperature = data['airtemperature']
    print(airtemperature)
    processtemperature = data['processtemperature']
    rotationalspeed = data['rotationalspeed']
    torque = data['torque']
    toolwear = data['toolwear']
    input_data = [[airtemperature, processtemperature, rotationalspeed, torque, toolwear]]
    prediction = model.predict(input_data)[0]
    if prediction == 0:
        prediction = 'No Failure in Machine'
    else:
        prediction = 'Machine Failure'    
    return {
        'prediction' : prediction
    }    

## ru the API with Uvicorn 
if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000)

#uvicorn MachineFailurePredictor:api --reload
##swagger http://127.0.0.1:8000/docs