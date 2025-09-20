import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os


def train_and_save_model():
    # Load dataset
    data_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "dataset.csv",
    )
    df = pd.read_csv(data_path)

    X = df.drop("label", axis=1)
    y = df["label"]

    # Train model
    model = LogisticRegression()
    model.fit(X, y)

    # Save model
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print("✅ Model trained and saved at", model_path)


def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    with open(model_path, "rb") as f:
        return pickle.load(f)


if __name__ == "__main__":
    train_and_save_model()
    print("✅ Model trained and saved as model/model.pkl")
