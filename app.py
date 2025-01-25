from flask import Flask, request, jsonify, render_template
import re
import nltk

# Initialize Flask app
app = Flask(__name__)

# Download required NLTK data (ensure this runs at least once)
# nltk.download('punkt')

# Predefined dictionary for normalization
custom_corrections = {
    "helo": "hello",
    "wrld": "world",
    "pythonn": "python",
    "heloo": "hello",
    "woorrrld": "world"
}

def remove_repeated_characters(word):
    return re.sub(r"(.)\1+", r"\1", word)

def normalize_word(word):
    word = word.lower()
    return custom_corrections.get(word, word)

def remove_duplicate_words(sentence):
    words = sentence.split()
    seen = set()
    unique_words = []
    for word in words:
        if word not in seen:
            seen.add(word)
            unique_words.append(word)
    return " ".join(unique_words)

def process_sentence(sentence):
    words = sentence.split()
    processed_words = [normalize_word(remove_repeated_characters(word)) for word in words]
    return remove_duplicate_words(" ".join(processed_words))

def remove_duplicate_sentences(sentences):
    seen = set()
    unique_sentences = []
    for sentence in sentences:
        if sentence.lower() not in seen:
            seen.add(sentence.lower())
            unique_sentences.append(sentence)
    return unique_sentences

def convert_structured_to_normal_text(text):
    cleaned_text = re.sub(r"[\-\*\•\d]+\s", "", text)
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()
    sentences = nltk.sent_tokenize(cleaned_text)
    processed_sentences = [process_sentence(sentence) for sentence in sentences]
    unique_sentences = remove_duplicate_sentences(processed_sentences)
    return " ".join(unique_sentences)

# Route for serving the frontend
@app.route('/')
def home():
    return render_template('demo.html')

# API endpoint for processing text
@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    structured_text = data['text']
    try:
        normal_text = convert_structured_to_normal_text(structured_text)
        return jsonify({'normal_text': normal_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
