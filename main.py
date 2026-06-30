import json
import pandas as pd

candidates = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        score = 0

        exp = candidate["profile"]["years_of_experience"]

        if 5 <= exp <= 9:
            score += 20

        skills = [
            s["name"].lower()
            for s in candidate.get("skills", [])
        ]

        ai_keywords = [
            "python",
            "machine learning",
            "llm",
            "embeddings",
            "rag",
            "faiss",
            "vector"
        ]

        for k in ai_keywords:
            if k in skills:
                score += 10

        candidates.append({
            "candidate_id": candidate["candidate_id"],
            "score": score
        })

df = pd.DataFrame(candidates)

df = df.sort_values(
    by="score",
    ascending=False
)

df["rank"] = range(1, len(df)+1)

df.head(100).to_csv(
    "outputs/ranked_candidates.csv",
    index=False
)

print("Done")