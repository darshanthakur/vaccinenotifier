import requests
import datetime
from twilio.rest import Client
from prettytable import PrettyTable

f = open("pincode.txt", "rt")
pincodestr = f.read().strip()
pincode = pincodestr[0:len(pincodestr)].split(',')

email_to = 'dram1998@gmail.com'

def sendg(center_name,day,i):
	from sendgrid import SendGridAPIClient
	from sendgrid.helpers.mail import Mail

	message = Mail(
	    from_email='sunnyprakash198@gmail.com',
	    to_emails=email_to,
	    subject='Vaccine Availability Information',
	    html_content='<strong>Slot Available at '+center_name+' '+day+' '+i+'</strong>')
	try:
	    sg = SendGridAPIClient('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')
	    response = sg.send(message)
	except Exception as e:
	    print(e.message)

def twili(center_name,day,i):
	# Your Account SID from twilio.com/console
	account_sid = "ACd1067b36c5eca4482d3528fb7137ae34"
	# Your Auth Token from twilio.com/console
	auth_token  = "a3b68a6cf30cee97439241663c536629"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to="+918888876040", 
	    from_="+18135188145",
	    body=("Slot Available At "+center_name+" "+day+" "+i))
	return 0

table = PrettyTable()
table.field_names = ["Date","Pin Code","Center Name","Capacity","Vaccine Name"]
today = str(datetime.date.today().day)
print("Current time is ",datetime.datetime.now().time(),"\n")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

for i in pincode:

	tod_v = requests.get(url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+i+'&date='+today+'-05-2021',headers=headers)


	if not tod_v.json()["centers"]:
		pass	
	else:
		for j in tod_v.json()["centers"]:
			for k in j["sessions"]:
				if (k["available_capacity"])>1:
					twili(j["name"],str(k["date"]),str(i))
					sendg(j["name"],str(k["date"]),str(i))
					print(k["date"]+" AVAILABLE AT "+j["name"]+" "+k["vaccine"]+" "+i)
				table.add_row([(k["date"]),i,j["name"],k["available_capacity"],k["vaccine"]])
			
print(table)

	    
#heroku (server)
# Cronjob (scheduler)
# sendgrid (email)
# twilio (whatsapp)

#Sendgrid Key: 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
#https://devcenter.heroku.com/articles/clock-processes-python
