import requests
import datetime
from twilio.rest import Client
from prettytable import PrettyTable

f = open("pincode.txt", "rt")
pincodestr = f.read().strip()
pincode = pincodestr[0:len(pincodestr)].split(',')

email_to = 'RECEIVER_EMAIL'  #Need not be Authorized

def teleg(vac_name,center_name,day,i):
   
   bot_message = "Slot for "+vac_name+" Available At "+center_name+" on "+day+". The Pincode "+i
   bot_token = '_BOT_TOKEN_HERE_'
   bot_chatID = '_CHAT_ID_HERE_' #Find How to get Chat ID in Readme file

   send_text ='https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=Markdown&text='+bot_message
   
   requests.get(send_text)


def sendg(vac_name,center_name,day,i):
	from sendgrid import SendGridAPIClient
	from sendgrid.helpers.mail import Mail

	message = Mail(
	    from_email='Sender_Email_ID',  #Need to be authorized in SendGrid Account
	    to_emails=email_to,
	    subject='Vaccine Availability Information',
	    html_content='<strong>Slot for '+vac_name+' Available at '+center_name+' on '+day+'. The Pincode '+i+'</strong>')
	try:
	    sg = SendGridAPIClient('API_KEY_HERE')
	    response = sg.send(message)
	except Exception as e:
	    print(e.message)

def twili(vac_name,center_name,day,i):
	# Your Account SID from twilio.com/console
	account_sid = "Account_SID_Here"
	# Your Auth Token from twilio.com/console
	auth_token  = "API_Key_Here"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to="Authorized_Mob_number_here", 
	    from_="Your_Twilio_Trial_Number_Here",
	    body=("Slot for"+vac_name+"Available At "+center_name+" on "+day+". The Pincode "+i))
	return 0

table = PrettyTable()
table.field_names = ["Date","Pin Code","Center Name","Capacity","Vaccine Name"]
today = str(datetime.date.today().day)
today_month = str(datetime.date.today().month)
print("Current time is ",datetime.datetime.now().time(),"\n")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

for i in pincode:

	tod_v = requests.get(url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+i+'&date='+today+'-'+today_month+'-2021',headers=headers)

	if not tod_v.ok:
		print("Too Many Requests Sent")
		exit()
	elif not tod_v.json()["centers"]:
		pass	
	else:
		for j in tod_v.json()["centers"]:
			for k in j["sessions"]:
				if (k["available_capacity"])>1:
					#twili(k["vaccine"],j["name"],str(k["date"]),str(i))  #Commented as API Keys Are Removed
					#sendg(k["vaccine"],j["name"],str(k["date"]),str(i))  #Commented as API Keys Are Removed
					#teleg(k["vaccine"],j["name"],str(k["date"]),str(i)) #Commented as Tokens Are Removed
					print(k["date"]+" AVAILABLE AT "+j["name"]+" "+k["vaccine"]+" "+str(j["pincode"]))
				table.add_row([(k["date"]),i,j["name"],k["available_capacity"],k["vaccine"]])
			
print(table)

