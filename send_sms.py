from twilio.rest import TwilioRestClient 
import os
import requests, time
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

 
# put your own credentials here 
#input_text=input("please input some text: ")

def send_text(text,to):
	ACCOUNT= os.environ["ACCOUNT_SID"]
	AUTH = os.environ["AUTH_TOKEN" ]
	client = TwilioRestClient(ACCOUNT, AUTH) 
	text_message=client.messages.create(to=to, from_="+12564141426", body=text)
		#status_callback='http://127.0.0.1:5000/') 
	#r = requests.post("http://127.0.0.1:5000/", data={"ts":time.time()})
	#print(r)
	return "{}".format(text_message)

	#print(r.status_code)
	#print (r.content)




#'http://http://requestb.in/z8z70iz8'



 
#"+35796016554 

 


#Fraulein
#+971563921508

#+971564803856

#+35796016554