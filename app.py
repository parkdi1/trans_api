from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_lang = request.form['target_lang']
    try:
        translation = translator.translate(text, dest=target_lang)
        return jsonify({
            'original_text': text,
            'translated_text': translation.text,
            'source_language': translation.src,
            'target_language': target_lang
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)