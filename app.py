from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from test import *
from spell import *

app = Flask(__name__)
preps = ["in","at","from","on","near", "of","for","names"]
arti = ["a","an","the","in"]

def check(li,preps):                                        # function for checking if any of preps's content present in incoming massage list and return it
    length1 = len(preps)
    length2 = len(li)
    for i in range(0,length1):
        for j in range(0,length2):
            if (preps[i] == li[j]):
                return preps[i]
    return 0
def Convert(li,p):                                          # function for serching the main place name
    length = len(li) 
    if(length < 3):return 0
    indexx = li.index(p)
    if(indexx == length-1 or indexx == 0):
        return 0
    final = li[indexx+1]
    if(li[indexx+1] in arti):
        if(indexx+2 == length):
            return 0
        final = li[indexx+2]
    res=[correct(li[indexx-1]),final]
    return res

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    li = list(incoming_msg.split(" "))                          # making the list of incoming massage like "i am sanmay" to ["i","am","sanmay"]
    if 'hi' in li or 'hello' in li or 'hlw' in li:
        msg.body('Welcome 🤝,I am your guide 😊, and let me know what you are looking for')
        responded = True
    elif check(li,preps):
        prep = check(li,preps)                                  # in there prep is preps's content which is present in incoming massage's list called li
        last = Convert(li,prep)                                 # in there last is the final place
        # msg.body(f'{last}')
        if(last==0):
            msg.body('sorry !! can you rewrite the sentence 😒')
        else:
            msg.body('👉')
            
            # msg.body(nearby(last[0],last[1],i)[1]+'\n'+'\n'+'location'+'\n'+'\n'+nearby(last[0],last[1],i)[0]+'\n'+'\n'+'👉')
            # msg.body(last[0]+' '+last[1])
            
            for i in range(0,4):
                msg.body(nearby(last[0],last[1],i)[1]+'\n'+'\n'+'📌'+'landmark'+'\n'+'\n'+nearby(last[0],last[1],i)[2]+'\n'+'\n'+'🌏'+'location'+'\n'+'\n'+nearby(last[0],last[1],i)[0]+'\n'+'\n'+'👉')
                responded = True
    if not responded :
        msg.body('Sorry!! I can not understand \n your words  😔!!')
    return str(resp)
if __name__ == '__main__':
    app.run(port=4000)
    

