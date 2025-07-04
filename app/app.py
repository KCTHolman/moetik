from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("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")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/antwoord', methods=['POST'])
def antwoord():
    data = request.json
    vraag = data.get('vraag', '')
    toon = data.get('toon', 'neutraal')

    prompt = f"Beantwoord op een {toon} manier de vraag: Moet ik {vraag}?"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Je bent een behulpzame, grappige en soms filosofische assistent."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.8
    )

    antwoord = response['choices'][0]['message']['content'].strip()
    return jsonify({'antwoord': antwoord})
