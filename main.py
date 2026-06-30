import json
import pandas as pd

candidates = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        score = 0
        reasons = []

        exp = candidate["profile"]["years_of_experience"]

        if 5 <= exp <= 9:
            score += 20
            reasons.append(f"{exp} years of experience matches target range")

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

        matched = []

        for k in ai_keywords:
            if k in skills:
                score += 10
                matched.append(k)

        if matched:
            reasons.append(
                "Strong skills in " + ", ".join(matched)
            )

        if not reasons:
            reasons.append(
                "Limited match based on current scoring criteria"
            )

        candidates.append({
            "candidate_id": candidate["candidate_id"],
            "score": float(score),
            "reasoning": ". ".join(reasons)
        })

df = pd.DataFrame(candidates)

df = df.sort_values(
    by=["score", "candidate_id"],
    ascending=[False, True]
)

df = df.head(100).reset_index(drop=True)

df["rank"] = range(1, 101)

df = df[
    ["candidate_id", "rank", "score", "reasoning"]
]

df.to_csv(
    "ranked_candidates.csv",
    index=False,
    encoding="utf-8"
)

print("Submission file generated successfully!")
