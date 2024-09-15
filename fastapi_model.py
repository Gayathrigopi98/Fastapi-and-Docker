from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import joblib

app = FastAPI()

# Define the Input model to include all features
class Input(BaseModel):
    Item_Identifier: str
    Item_Weight: float
    Item_Fat_Content: str
    Item_Visibility: float
    Item_Type: str
    Item_MRP: float
    Outlet_Identifier: str
    Outlet_Establishment_Year: int
    Outlet_Size: str
    Outlet_Location_Type: str
    Outlet_Type: str

class Output(BaseModel):
    y: float

@app.post("/predict")
def predict(data: Input) -> Output:
    # Convert input to a dictionary and then DataFrame
    input_dict = {
        'Item_Identifier': [data.Item_Identifier],
        'Item_Weight': [data.Item_Weight],
        'Item_Fat_Content': [data.Item_Fat_Content],
        'Item_Visibility': [data.Item_Visibility],
        'Item_Type': [data.Item_Type],
        'Item_MRP': [data.Item_MRP],
        'Outlet_Identifier': [data.Outlet_Identifier],
        'Outlet_Establishment_Year': [data.Outlet_Establishment_Year],
        'Outlet_Size': [data.Outlet_Size],
        'Outlet_Location_Type': [data.Outlet_Location_Type],
        'Outlet_Type': [data.Outlet_Type]
    }
    
    X_input = pd.DataFrame(input_dict)
    
    # Load the model
    model = joblib.load('big_market_sales_prediction.pkl')
    
    # Make prediction
    prediction = model.predict(X_input)
    
    return {"y": prediction}




#input sample
# {
#   "Item_Identifier": "FDA15",
#   "Item_Weight": 9.30,
#   "Item_Fat_Content": "Low Fat",
#   "Item_Visibility": 0.016047,
#   "Item_Type": "Dairy",
#   "Item_MRP": 249.8092,
#   "Outlet_Identifier": "OUT049",
#   "Outlet_Establishment_Year": 1999,
#   "Outlet_Size": "Medium",
#   "Outlet_Location_Type": "Tier 1",
#   "Outlet_Type": "Supermarket Type1"
# }

