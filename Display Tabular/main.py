import requests
import datetime
import schedule
from prettytable import PrettyTable

pincode = ["411007","412105","411026","411027","411057","411045","411039","411006","412205","411019","411015",
"411018","410501","411015","411019","411018","411004","411019","411005"]




table = PrettyTable()
table.field_names = ["Date","Center Name","Capacity","Vaccine Name"]

today = str(datetime.date.today().day)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

for i in pincode:

	tod_v = requests.get(url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+i+'&date='+today+'-05-2021',headers=headers)
	if not tod_v.ok:
		print("Too Many Requests Sent")
		exit()
	elif not tod_v.json()["centers"]:
		pass
	else:
		for j in tod_v.json()["centers"]:
			for k in j["sessions"]:
				if (k["available_capacity"])>0:
					print(k["date"]+" AVAILABLE AT "+j["name"]+" "+k["vaccine"]+" "+i)
				table.add_row([str((k["date"]))[0:2],j["name"],k["available_capacity"],k["vaccine"]])
								
print("\n")
print(table)
