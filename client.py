import requests

def check_spelling(text):
    url = 'http://127.0.0.1:5000/correct_spelling'
    data = {'text': text}
    response = requests.post(url, json=data)
    return response.json()

def check_grammar(sentence):
    url = 'http://127.0.0.1:5000/check_grammar'
    data = {'sentence': sentence}
    response = requests.post(url, json=data)
    return response.json()

if __name__ == '__main__':
    
    text = input("Enter text: ")

    spelling_response = check_spelling(text)
    corrected_spelling = spelling_response['corrected']

    print(f"Original Spelling: {spelling_response['original']}")
    print(f"Corrected Spelling: {corrected_spelling}")

    grammar_response = check_grammar(corrected_spelling)

    print(f"Original Grammar: {grammar_response['original_sentence']}")
    print(f"Corrected Grammar: {grammar_response['corrected_sentence']}")
