from flask import Flask, render_template, request, jsonify
import pandas as pd

from file1 import run_data_mining
from comment_generation import generate_human_like_comment

app = Flask(__name__)


# =========================
# HOME
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# DASHBOARD PAGE
@app.route("/dashboard")
def dashboard():

    try:
        df = pd.read_csv("analyzed_blogs.csv")

        stats = {
            "blogs": len(df),
            "comments": int(df["comment_count"].sum()) if "comment_count" in df.columns else 0,
            "sentiment": round(df["sentiment"].mean(), 2) if "sentiment" in df.columns else 0
        }

        columns = df.columns.tolist()
        table = df.fillna("").to_dict(orient="records")

    except Exception as e:

        print("Dashboard Error:", e)

        stats = {
            "blogs": 0,
            "comments": 0,
            "sentiment": 0
        }

        columns = []
        table = []

    return render_template(
        "dashboard.html",
        stats=stats,
        columns=columns,
        table=table
    )


# =========================
# DATA MINING
# =========================
@app.route("/mine", methods=["GET", "POST"])
def mine():
    if request.method == "POST":
        keyword = request.form.get("keyword")

        if keyword:
            run_data_mining(keyword)
            return jsonify({"message": "Mining Completed Successfully!"})

        return jsonify({"message": "Please enter keyword"}), 400

    return render_template("mining.html")


# =========================
# COMMENT GENERATION (ONLY)
# =========================
@app.route("/generate-comment")
def generate_comment():
    comment, meta = generate_human_like_comment()

    return jsonify({
        "comment": comment,
        "title": meta["title"],
        "summary": meta["summary"]
    })


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)