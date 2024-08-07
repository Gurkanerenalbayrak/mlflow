import mlflow
import numpy as np

mlflow.set_tracking_uri("http://mlflow-tracking-server:5000")
logged_model_location = # konumu ileride yazabiliyor olucaksın "models:/sklearn-model/1"
logged_model = mlflow.pyfunc.load_model(logged_model_location)


random_data = np.random.randn(10, 87931)
prediction = logged_model.predict(random_data)
print(prediction)

