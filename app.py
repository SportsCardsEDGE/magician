from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def getFomAI(que):
    import os
    import openai
    import random

    #key = os.environ.get("MY_VARIABLE")
    openai.api_key = "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"
    tarot_cards = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers', 'The Chariot', 'Strength', 'The Hermit', 'Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgment', 'The World', 'Ace of Wands', 'Two of Wands', 'Three of Wands', 'Four of Wands', 'Five of Wands', 'Six of Wands', 'Seven of Wands', 'Eight of Wands', 'Nine of Wands', 'Ten of Wands', 'Page of Wands', 'Knight of Wands', 'Queen of Wands', 'King of Wands', 'Ace of Cups', 'Two of Cups', 'Three of Cups', 'Four of Cups', 'Five of Cups', 'Six of Cups', 'Seven of Cups', 'Eight of Cups', 'Nine of Cups', 'Ten of Cups', 'Page of Cups', 'Knight of Cups', 'Queen of Cups', 'King of Cups', 'Ace of Swords', 'Two of Swords', 'Three of Swords', 'Four of Swords', 'Five of Swords', 'Six of Swords', 'Seven of Swords', 'Eight of Swords', 'Nine of Swords', 'Ten of Swords', 'Page of Swords', 'Knight of Swords', 'Queen of Swords', 'King of Swords', 'Ace of Pentacles', 'Two of Pentacles', 'Three of Pentacles', 'Four of Pentacles', 'Five of Pentacles', 'Six of Pentacles', 'Seven of Pentacles', 'Eight of Pentacles', 'Nine of Pentacles', 'Ten of Pentacles', 'Page of Pentacles', 'Knight of Pentacles', 'Queen of Pentacles', 'King of Pentacles']
    random_cards = random.sample(tarot_cards, 10)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= "You are a tarot card reader and I am your client. please describe the imagery, symbolism, and meaning of each card in the following celtic spread in the context of “"+que+"” and the cards:  The Present: "+random_cards[0]+", The Challenge: "+random_cards[1]+", The Past: "+random_cards[2]+", The Future: "+random_cards[3]+", Above: "+random_cards[4]+", Below: "+random_cards[5]+", Advice: "+random_cards[6]+", External Influences: "+random_cards[7]+", Hopes and Fears: "+random_cards[8]+", Outcome: "+random_cards[9]+". Add <br><br> tag when a card is complete.",
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)