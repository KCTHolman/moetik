from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
from flask import send_from_directory

@app.route('/quotes.json')
def quotes():
    return send_from_directory('static', 'quotes.json')

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
