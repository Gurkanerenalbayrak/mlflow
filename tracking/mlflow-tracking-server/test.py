import os 
from random import random,randint
from mlflow import log_metric,log_param,log_params,log_artifacts 
import mlflow



if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:6101")

    log_param("config_value", randint(0, 100))

    log_params({"param1": randint(0, 100), "param2": randint(0, 100)})

    log_metric("accuracy", random() / 2.0)

    log_metric("accuracy", random() + 0.1)

    log_metric("accuracy", random() + 0.2)

    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world")

    log_artifacts("outputs")

