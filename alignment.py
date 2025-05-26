from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def get_factual_embedding(text: str) -> np.ndarray:
    return np.array([1.0, 0.0, 0.0])

def get_emotional_embedding(text: str) -> np.ndarray:
    return np.array([0.0, 1.0, 0.0])

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    dot = float(a.dot(b))
    norm_a = float(np.linalg.norm(a))
    norm_b = float(np.linalg.norm(b))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0

def compute_alignment_score(text: str) -> float:
    f_embed = get_factual_embedding(text)
    e_embed = get_emotional_embedding(text)
    return cosine_similarity(f_embed, e_embed)

def scan_document(text: str, threshold: float = 0.75):
    segments = [seg.strip() for seg in text.split('\n\n') if seg.strip()]
    results = []
    for seg in segments:
        score = compute_alignment_score(seg)
        results.append({
            "text": seg,
            "alignment_score": round(score, 3),
            "bias_flag": score < threshold
        })
    return {"segments": results}

@app.route('/scan', methods=['POST'])
def scan_endpoint():
    data = request.get_json(force=True)
    text = data.get('text', '')
    threshold = float(data.get('threshold', 0.75))
    report = scan_document(text, threshold)
    return jsonify(report)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
