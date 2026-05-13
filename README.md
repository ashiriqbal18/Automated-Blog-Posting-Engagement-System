# Automated-Blog-Posting-Engagement-System

An intelligent Data Mining + NLP + AI-powered blog analysis platform built using Python, Streamlit, Machine Learning, and Local LLMs (Ollama).

This system automatically discovers blogs from the web, extracts useful information, analyzes sentiment and discussion patterns, identifies hidden topics using LDA, generates AI summaries, and even creates human-like comments using local AI models.

🚀 Features

✅ Automated blog discovery using Google Search
✅ Web scraping and content extraction
✅ Comment extraction from blogs
✅ Sentiment analysis on discussions
✅ AI-generated summaries using local LLMs
✅ Topic clustering using Hybrid LDA
✅ TF-IDF keyword extraction
✅ Interactive Streamlit dashboard
✅ Word cloud visualization
✅ Human-like AI comment generation
✅ Automated Dev.to comment posting API integration

🏗️ Project Architecture
<img width="251" height="722" alt="image" src="https://github.com/user-attachments/assets/58a4440b-fba7-49c6-b99b-d008a3ef7241" />

⚙️ Technologies Used
Frontend
Streamlit
Data Mining & Web Scraping
BeautifulSoup
Newspaper3k
Requests
SerpAPI
NLP & Machine Learning
NLTK
VADER Sentiment
Scikit-learn
TF-IDF Vectorizer
Latent Dirichlet Allocation (LDA)
AI Models
Ollama
Phi-3
Mistral
Visualization
Matplotlib
Seaborn
WordCloud

🧠 System Workflow
Step 1 — Keyword Input

User enters a keyword like:

AI
Python
Blockchain
Cybersecurity
Step 2 — Blog Collection

The system:

Searches Google using SerpAPI
Collects blog URLs
Filters blogs from:
WordPress
Blogspot
Dev.to
Step 3 — Blog Processing

Each blog is analyzed for:

Title
Author
Publish date
Blog content
Comments
Sentiment
Step 4 — Local AI Analysis

Using Phi-3 via Ollama:

Blog summary generation
Motive detection
Tone classification
Step 5 — Topic Modeling

Hybrid LDA groups blogs into hidden themes.

Example:

AI Research
Technical Tutorials
Product Reviews
Step 6 — Keyword Extraction

TF-IDF extracts the most important keywords from every blog.

Step 7 — Dashboard Visualization

The system generates:

Sentiment graphs
Engagement charts
Topic distributions
Discussion word clouds
Step 8 — AI Comment Generation

Mistral generates realistic human-like comments based on:

Blog summary
Existing discussion
Blog engagement
📊 Generated Outputs
CSV Dataset
analyzed_blogs.csv

Contains:

Blog metadata
Sentiment scores
AI summaries
Topics
Keywords
Comments
Dashboard Image
data_mining_dashboard.png
Posting Logs
logs/posting_log.json
📈 Visual Analytics Included
✅ Sentiment Analysis

Shows positivity/negativity of discussions.

✅ Content Motive Distribution

Pie chart showing blog categories.

✅ Engagement vs Sentiment

Scatter plot comparing comments and sentiment.

✅ Discussion Word Cloud

Most frequently discussed terms.

🤖 AI Models Used
Model	Purpose
Phi-3	Blog summarization and classification
Mistral	Human-like comment generation
🔍 Data Mining Techniques Used
Technique	Purpose
TF-IDF	Keyword extraction
LDA	Topic clustering
Sentiment Analysis	Comment emotion detection
Web Scraping	Blog extraction
NLP Classification	Tone & motive detection
🛡️ Ethical Considerations

The system includes:

API disclosure support
Bot disclosure footer for Dev.to comments
Respectful request rate limiting
Local AI processing for privacy
