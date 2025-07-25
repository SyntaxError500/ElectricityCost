from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
from typing_extensions import Annotated
import joblib
import pandas as pd


# Load pipeline
pipeline = joblib.load("model/final_pipeline.pkl")

app = FastAPI()

class InputData(BaseModel):
    site_area: Annotated[int, Field(ge=0)]
    structure_type: Annotated[
        Literal["Commercial", "Industrial", "Mixed-use", "Residential"],
        Field(description="Type of structure")
    ]
    water_consumption: Annotated[float, Field(ge=0)]
    recycling_rate: Annotated[int, Field(ge=0, le=100)]
    utilisation_rate: Annotated[int, Field(ge=0, le=100)]
    air_qality_index: Annotated[int, Field(ge=0)]
    issue_reolution_time: Annotated[int, Field(ge=0)]
    resident_count: Annotated[int, Field(ge=0)]

import pandas as pd


# Home route
@app.get("/")
def home():
    return {
        "message": "Welcome to the Electricity Cost Prediction API",
        "usage": {
            "predict": "/predict",
            "method": "POST",
            "input_fields": [
                "site_area", "structure_type", "water_consumption", "recycling_rate",
                "utilisation_rate", "air_qality_index", "issue_reolution_time", "resident_count"
            ]
        }
    }


#predict route
@app.post("/predict")
def predict(data: InputData):
    try:
        #input into a DataFrame
        input_df = pd.DataFrame([{
            "structure_type": data.structure_type,
            "site_area": data.site_area,
            "water_consumption": data.water_consumption,
            "resident_count": data.resident_count,
            "issue_reolution_time": data.issue_reolution_time,
            "utilisation_rate": data.utilisation_rate,
            "air_qality_index": data.air_qality_index,
            "recycling_rate": data.recycling_rate
        }])

        #  dataframe to pipeline
        prediction = pipeline.predict(input_df)[0]
        return {"predicted_electricity_cost": round(prediction, 2)}

    except Exception as e:
        return {"error": str(e)}
