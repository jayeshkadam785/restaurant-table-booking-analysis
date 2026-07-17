from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "Dataset_.csv")


def load_analysis():
    df = pd.read_csv(DATA_PATH)
    df.columns = df.columns.str.strip()

    total = len(df)

    # --- 1. Table booking & online delivery percentages ---
    table_booking_yes = int((df["Has Table booking"] == "Yes").sum())
    online_delivery_yes = int((df["Has Online delivery"] == "Yes").sum())

    table_booking_pct = round(table_booking_yes / total * 100, 2)
    online_delivery_pct = round(online_delivery_yes / total * 100, 2)

    # --- 2. Average rating comparison: table booking Yes vs No ---
    avg_rating_tb_yes = round(
        df[df["Has Table booking"] == "Yes"]["Aggregate rating"].mean(), 2
    )
    avg_rating_tb_no = round(
        df[df["Has Table booking"] == "No"]["Aggregate rating"].mean(), 2
    )

    # --- 3. Online delivery availability across price ranges ---
    price_range_labels = {1: "Cheap ($)", 2: "Moderate ($$)", 3: "Expensive ($$$)", 4: "Very Expensive ($$$$)"}
    price_delivery = (
        df.groupby("Price range")["Has Online delivery"]
        .apply(lambda x: round((x == "Yes").mean() * 100, 2))
        .to_dict()
    )
    price_range_data = [
        {"range": price_range_labels.get(k, str(k)), "pct": v}
        for k, v in sorted(price_delivery.items())
    ]

    return {
        "total": total,
        "table_booking_yes": table_booking_yes,
        "table_booking_pct": table_booking_pct,
        "online_delivery_yes": online_delivery_yes,
        "online_delivery_pct": online_delivery_pct,
        "avg_rating_tb_yes": avg_rating_tb_yes,
        "avg_rating_tb_no": avg_rating_tb_no,
        "price_range_data": price_range_data,
    }


# Compute once at startup (dataset is static, keeps requests fast on serverless)
ANALYSIS = load_analysis()


@app.route("/")
def index():
    return render_template("index.html", data=ANALYSIS)


if __name__ == "__main__":
    app.run(debug=True)
