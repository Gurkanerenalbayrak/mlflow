import mlflow.pyfunc 
import joblib
import numpy as np
import pandas as pd

class SentimentClassifier(mlflow.pyfunc.PythonModel):
    def __init__(self) -> None:
        self.vectorizer = None
        self.model = None

    def load_context(self, context):
        self.model = joblib.load(context.artifacts["model"])
        self.vectorizer = joblib.load(context.artifacts["vectorizer"])

    def predict(self, context, model_df: pd.DataFrame) -> np.ndarray:
        inputs = self.vectorizer.transform(input_df["review"])
        return self.model.predict(inputs)
    

    

