from flask import Blueprint, request, jsonify
from grammar_checker import correct_grammar
from textblob import TextBlob

correct_spelling_route = Blueprint('correct_spelling_route', __name__)

@correct_spelling_route.route('/correct_spelling', methods=['POST'])
def correct_spelling_route_handler():
    incorrect_text = request.json.get('text', '')
    
    if not incorrect_text:
        return jsonify({'error': 'No text provided'}), 400

    blob = TextBlob(incorrect_text)
    corrected_text = str(blob.correct())

    return jsonify({'original': incorrect_text, 'corrected': corrected_text})



correct_grammar_route = Blueprint('correct_grammar_route', __name__)

@correct_grammar_route.route('/check_grammar', methods=['POST'])
def check_grammar_route_handler():
    
    sentence = request.json.get('sentence', '')
    
    if not sentence:
        return jsonify({'error': 'No sentence provided'}), 400

    corrected_sentence = correct_grammar(sentence)
    
    return jsonify({
        'original_sentence': sentence,
        'corrected_sentence': corrected_sentence
    })
