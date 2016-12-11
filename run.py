from flask import Flask,render_template,request, redirect
import twilio.twiml
import send_sms	
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #request values returns a dictionary, get this from the user as an input in CSS 
    message= request.values.get('message')
    to=request.values.get('to')
    
    text_message=None
    if message:
        text_message=send_sms.send_text(message,to)
    return render_template('index.html',text_message= text_message)




    #message = None
    #if text: 
     #   message = send_sms.send_text(text_message)
  
    """Respond to incoming calls with a simple text message."""
    #

    #resp = twilio.twiml.Response()
    #resp.message("Hello, Mobile Monkey")
    #return str(resp)

if __name__ == "__main__":
    port=int(os.environ.get("PORT",5000))
    app.run(host ="0.0.0.0",port=port)