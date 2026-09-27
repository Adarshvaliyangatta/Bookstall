import pandas as pd
import matplotlib.pyplot as plt

def get_analysis():

    df = pd.read_csv("data/orders.csv")

    return {

        "orders": len(df),

        "revenue": df["Amount"].sum(),

        "average": round(df["Amount"].mean(),2),

        "popular": df["Item"].mode()[0],

        "highest": df["Amount"].max(),

        "recent": df.tail(5).to_dict(orient="records")

    }


def create_chart():

    df = pd.read_csv("data/orders.csv")

    sales = df.groupby("Item")["Amount"].sum()

    plt.figure(figsize=(7,4))

    sales.plot(kind="bar")

    plt.title("Sales by item")

    plt.xlabel("items")

    plt.ylabel("Revenue")

    plt.tight_layout()

    plt.savefig("static/charts/sales.png")

    plt.close()