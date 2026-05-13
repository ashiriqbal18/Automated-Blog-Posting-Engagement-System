import pandas as pd
import ast
import ollama
import re

def generate_human_like_comment():

    print("📂 Loading 'analyzed_blogs.csv'...")

    try:
        df = pd.read_csv("analyzed_blogs.csv")
    except FileNotFoundError:
        return "", {"error": "CSV file not found"}

    if df.empty:
        return "", {"error": "CSV is empty"}

    # Select most commented blog
    blog_to_analyze = df.sort_values(by='comment_count', ascending=False).iloc[0]

    summary = blog_to_analyze['summary']
    raw_comments = blog_to_analyze['comments']

    try:
        existing_discussion = ast.literal_eval(raw_comments) if pd.notna(raw_comments) else []
    except:
        existing_discussion = []

    discussion_snippet = "\n".join([str(c)[:200] for c in existing_discussion[:5]])

    prompt = f"""
    [TASK] Write a short, casual comment for this blog.

    SUMMARY: {summary}

    PREVIOUS COMMENTS:
    {discussion_snippet if discussion_snippet else "None"}

    [CONSTRAINTS]
    - Max 40 words
    - Use "I" or "me"
    - Simple, informal language (like a 12–14 year old)
    - No labels or explanations
    - Output ONLY the comment
    """

    try:
        local_res = ollama.chat(
            model='mistral',
            messages=[{'role': 'user', 'content': prompt}]
        )

        synthetic_comment = local_res['message']['content'].strip()

        synthetic_comment = re.sub(
            r'^(Comment|Response|Text):\s*',
            '',
            synthetic_comment,
            flags=re.IGNORECASE
        )

        synthetic_comment = synthetic_comment.replace('"', '')

        meta = {
            "title": blog_to_analyze['title'],
            "summary": summary
        }

        return synthetic_comment, meta

    except Exception as e:
        return "", {"error": f"Ollama failed: {str(e)[:100]}"}


if __name__ == "__main__":
    comment, meta = generate_human_like_comment()
    print(comment, meta)