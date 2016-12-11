from twilio.rest import TwilioRestClient 
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
 
 #put into an env file
# put your own credentials here 
ACCOUNT= os.environ["ACCOUNT_SID"]
AUTH= os.environ["AUTH_TOKEN" ]
 
client = TwilioRestClient(ACCOUNT, AUTH) 
 

message = client.messages.get(ACCOUNT,AUTH) 
#'SMd29732f67f654cfeabc6ef2a06c9b412'
 
print (message.body )