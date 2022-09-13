from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if ':hritik' in incoming_msg:
        msg.body('😏 ohoo.. you are the guy')
        msg.body('If you want to know about famouse quotes then enter quote ')
        msg.body('ans If you want to know about cates then enter cat')
        responded = True  
    if ':sayan' in incoming_msg:
        msg.body(f'welcome {incoming_msg}!!  mother fucker')
        msg.body('If you want to know about famouse quotes then enter quote ')
        msg.body('ans If you want to know about cates then enter cat')
        responded = True  
    if ':krishnendu' in incoming_msg:
        msg.body(f'welcome {incoming_msg}!!  bokka choda')
        msg.body('If you want to know about famouse quotes then enter quote ')
        msg.body('ans If you want to know about cates then enter cat')
        responded = True  
    if ':anik' in incoming_msg:
        msg.body(f'welcome {incoming_msg}!!  mother fucker')
        msg.body('If you want to know about famouse quotes then enter quote ')
        msg.body('ans If you want to know about cates then enter cat')
        responded = True       
    if ':arka' in incoming_msg:
        msg.body(f'welcome {incoming_msg}!!  mother fucker')
        msg.body('If you want to know about famouse quotes then enter quote ')
        msg.body('ans If you want to know about cates then enter cat')
        responded = True  
    elif 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    elif 'hi' in incoming_msg:
        # return a cat pic
        msg.body('hello, enter you name please')
        responded = True
    elif ':' in incoming_msg:
        msg.body(f'welcome -{incoming_msg}-!! ')
        msg.body('If you want to know about famouse quotes then enter quote ')
        msg.body('ans If you want to know about cates then enter cat')
        responded = True
    if not responded:
        msg.body('Sorry!! can you please send me hi or enter you name (by typing `:<name>:` at first )')
    return str(resp)

if __name__ == '__main__':
    app.run(port=4000)