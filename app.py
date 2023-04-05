from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def getFomAI(que):
    import os
    import openai

    key = os.environ.get("MY_VARIABLE")
    # openai.api_key = "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"

    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt= "You are a tarot card reader and I am your client. please describe the imagery, symbolism, and meaning of each card in the following celtic spread in the context of “"+que+"” and the cards:  The Present: Six of Wands, The Challenge: Ace of Pentacles, The Past: Page of Swords, The Future: Wheel of Fortune, Above: Two of Cups, Below: The Sun, Advice: Three of Pentacles, External Influences: The Empress, Hopes and Fears: Eight of Swords, Outcome: Knight of Swords. Add <br><br> tag when a card is complete.",
    #     temperature=0.7,
    #     max_tokens=1000,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    # )

    # ans = response['choices'][0]['text']
    return key

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)