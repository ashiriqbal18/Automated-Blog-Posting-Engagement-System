from flask import Flask, render_template, request, jsonify
import pandas as pd

from file1 import run_data_mining
from comment_generation import generate_human_like_comment
from comment_poster import post_comments

app = Flask(__name__)


# =========================
# HOME
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# DASHBOARD PAGE
# =========================
@app.route("/dashboard")
def dashboard():
    try:
        df = pd.read_csv("analyzed_blogs.csv")

        stats = {
            "blogs": len(df),
            "comments": int(df["comment_count"].sum()),
            "sentiment": round(df["sentiment"].mean(), 2)
        }

        table = df.to_dict(orient="records")

    except:
        stats = {"blogs": 0, "comments": 0, "sentiment": 0}
        table = []

    return render_template("dashboard.html", stats=stats, table=table)


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
# COMMENT GENERATION
# =========================
@app.route("/generate-comment")
def generate_comment():
    comment, meta = generate_human_like_comment()

    return jsonify({
        "comment": comment,
        "title": meta["title"],
        "summary": meta["summary"]
    })


# =========================
# POST COMMENTS
# =========================
@app.route("/post-comments")
def post_comments_route():
    try:
        df = pd.read_csv("generated_comment.csv")
        blogs = df.to_dict("records")

        post_comments(blogs)

        return jsonify({"message": "Comments Posted Successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)