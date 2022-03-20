import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


def train():
    df = pd.read_csv("HW2_CSCI571/SBP_new.csv")

    x = df[["Age", "Weight"]]
    y = df["SBP"]

    regr = LinearRegression()
    regr.fit(x, y)

    joblib.dump(regr, "HW2_CSCI571/regr_new.pkl")


def load(age, weight):
    clf = joblib.load("HW2_CSCI571/regr_new.pkl")
    x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
    prediction = clf.predict(x)[0]
    return prediction


if __name__ == "__main__":
    train()
    load()