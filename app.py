from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def getFomAI(que):
    import os
    import openai

    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= "You are a tarot card reader and I am your client. please describe the imagery, symbolism, and meaning of each card in the following celtic spread in the context of “"+que+"” and the cards:  The Present: Six of Wands, The Challenge: Ace of Pentacles, The Past: Page of Swords, The Future: Wheel of Fortune, Above: Two of Cups, Below: The Sun, Advice: Three of Pentacles, External Influences: The Empress, Hopes and Fears: Eight of Swords, Outcome: Knight of Swords. Add <br><br> tag when a card is complete.",
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    ans = response['choices'][0]['text']
    return ans

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_data():
    name = request.form.get('name')
    
    text = getFomAI(name)

    response = {
        "text": text,
    }

    return response

app.run(debug=True)