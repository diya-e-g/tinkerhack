import re
import nltk
from nltk.tokenize import sent_tokenize

# Download the required NLTK data
nltk.download('punkt')

# Predefined dictionary for normalization
custom_corrections = {
    "helo": "hello",
    "wrld": "world",
    "pythonn": "python",
    "heloo": "hello",
    "woorrrld": "world"
}

def remove_repeated_characters(word):
    """
    Removes consecutive repeated characters in a word.
    Example: 'hhhheeelllo' -> 'helo'
    """
    return re.sub(r"(.)\1+", r"\1", word)

def normalize_word(word):
    """
    Normalizes a word using the custom dictionary, if available.
    Otherwise, returns the word as is.
    """
    word = word.lower()  # Convert to lowercase for case-insensitive matching
    return custom_corrections.get(word, word)

def remove_duplicate_words(sentence):
    """
    Removes duplicate words within a single sentence.
    Example: 'hello hello world' -> 'hello world'
    """
    words = sentence.split()
    seen = set()
    unique_words = []
    for word in words:
        if word not in seen:  # Case-insensitive removal handled earlier
            seen.add(word)
            unique_words.append(word)
    return " ".join(unique_words)

def process_sentence(sentence):
    """
    Processes a sentence to remove repeated characters, normalize words, and remove duplicate words.
    """
    # Step 1: Remove repeated characters in each word
    words = sentence.split()
    processed_words = [normalize_word(remove_repeated_characters(word)) for word in words]

    # Step 2: Remove duplicate words
    return remove_duplicate_words(" ".join(processed_words))

def remove_duplicate_sentences(sentences):
    """
    Removes duplicate sentences from the list of sentences.
    """
    seen = set()
    unique_sentences = []
    for sentence in sentences:
        if sentence.lower() not in seen:  # Case-insensitive check for duplicates
            seen.add(sentence.lower())
            unique_sentences.append(sentence)
    return unique_sentences

def convert_structured_to_normal_text(text):
    """
    Converts structured text into normal text by removing repeated characters,
    duplicate words, applying dictionary corrections, and removing duplicate sentences.
    """
    # Step 1: Remove bullet points, numbering, and special characters
    cleaned_text = re.sub(r"[\-\*\•\d]+\s", "", text)  # Remove bullets or numbers
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()  # Remove excess whitespace

    # Step 2: Tokenize into sentences
    sentences = sent_tokenize(cleaned_text)

    # Step 3: Process each sentence
    processed_sentences = [process_sentence(sentence) for sentence in sentences]

    # Step 4: Remove duplicate sentences
    unique_sentences = remove_duplicate_sentences(processed_sentences)

    # Step 5: Combine sentences into a coherent paragraph
    normal_text = " ".join(unique_sentences)

    return normal_text


# Take user input for structured text
print("Enter your structured text (use '-' or '*' for bullets, or type 'DONE' on a new line to finish):")
user_input_lines = []
while True:
    line = input()
    if line.strip().upper() == "DONE":  # Stop input on 'DONE'
        break
    user_input_lines.append(line)

structured_text = "\n".join(user_input_lines)

# Convert structured text to normal text
normal_text = convert_structured_to_normal_text(structured_text)

# Display the result
print("\nConverted Normal Text (All Repetitions Removed):\n")
print(normal_text)
