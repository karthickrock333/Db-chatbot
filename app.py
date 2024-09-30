# app.py
from flask import Flask, render_template, request, jsonify
from chatbot import get_few_shot_db_chain
from audio_helper import record_audio, transcribe_audio
import os

app = Flask(__name__)
chain = get_few_shot_db_chain()

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/record', methods=['POST'])
def record():
    try:
        audio_file = record_audio()
        transcription = transcribe_audio(audio_file)
        return jsonify({'transcription': transcription})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    try:
        response = chain.run(question)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)