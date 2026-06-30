# nexora-minds-india-runs-ai-challenge

AI-powered candidate discovery and ranking system developed for the INDIA.RUNS Data & AI Challenge.

# Intelligent Candidate Discovery & Ranking

## Team Name

Nexora Minds

## Team ID

[Add Your Team ID Here]

## Challenge

INDIA.RUNS Data & AI Challenge

## Problem Statement

Build an AI-powered candidate ranking system that identifies the most suitable candidates for a given job description by leveraging semantic understanding, career history, technical skills, experience, and behavioral indicators.

## Objective

The goal of this project is to intelligently discover and rank candidates based on their relevance to a target job role. The system combines multiple evaluation signals to generate an explainable and reliable ranking.

## Approach

The solution follows a hybrid AI-driven methodology:

### 1. Candidate Profile Analysis

Candidate resumes and profiles are cleaned, standardized, and transformed into structured information.

### 2. Semantic Matching

Sentence Transformer embeddings are used to measure semantic similarity between job descriptions and candidate profiles.

### 3. Skill & Experience Evaluation

Technical skills, work history, and domain expertise are incorporated into the scoring process.

### 4. Behavioral Signal Ranking

Additional behavioral indicators and profile attributes are considered to improve recommendation quality.

### 5. Hybrid Scoring Mechanism

Multiple signals are combined into a unified ranking score to produce the final recommendations.

### 6. Final Candidate Ranking

The system generates the top-ranked candidates along with their scores and supporting explanations.

## Technologies Used

* Python
* Pandas
* NumPy
* Sentence Transformers
* FAISS
* Scikit-Learn
* OpenPyXL

## Project Structure

```text
nexora-minds-india-runs-ai-challenge/
│
├── data/                  # Input datasets
├── outputs/               # Generated ranking outputs
├── main.py                # Main execution script
├── requirements.txt       # Project dependencies
├── README.md              # Documentation
└── .gitignore             # Ignored files
```

## Installation

```bash
git clone https://github.com/rsathishkumar-2697/nexora-minds-india-runs-ai-challenge.git

cd nexora-minds-india-runs-ai-challenge

pip install -r requirements.txt
```

## Running the Project

```bash
python main.py
```

## Output

The system produces:

* Top 100 ranked candidates
* Candidate relevance scores
* Explainable ranking insights
* XLSX output file for submission

## Key Features

* AI-powered semantic candidate matching
* Hybrid scoring framework
* Efficient similarity search using FAISS
* Explainable candidate recommendations
* Scalable architecture for large datasets

## Future Enhancements

* Interactive web dashboard
* Real-time job description input
* Advanced explainability features
* Multi-model ensemble ranking
* Automated feedback-driven learning

## Repository

https://github.com/rsathishkumar-2697/nexora-minds-india-runs-ai-challenge

## License

This project was developed solely for participation in the INDIA.RUNS Data & AI Challenge.
