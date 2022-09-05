# firebase-admin == 4.5.2
import firebase_admin
from firebase_admin import credentials,firestore
from firebase_admin import _http_client
from firebase_admin import db

from matplotlib import pyplot as plt
from datetime import datetime

#initializing the credentials of the app
# after creating app project settings>service account> generate new private key
cred = credentials.Certificate("pmssx.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pmss-7fd59-default-rtdb.firebaseio.com/'
})

doctor_id = "d1"
patient_id = "p4"

abs_path = "Doctors/" + doctor_id +"/Patients/" + patient_id

def get_values (abs_path):
	ecg = []
	hr = []
	spo2 = []
	bili  = []

	ref = db.reference(abs_path)
	data = ref.order_by_child("timestamp").limit_to_last(1).get() 
	data = dict(data).values()
	data = list(data)
	#print(data)
	for i in data:
	 	hr.append(i.get("hr"))
	 	ecg += (i.get("ecg"))
	 	spo2.append(i.get("spo2"))
	 	bili.append(i.get("bili"))

	return(ecg,hr,spo2, bili)

def get_range_values (abs_path,start_date = 0, start_hour =0 , start_min = 0 , end_date = 0, end_hour =  0 , end_min = 0):
	ecg = []
	hr = []
	spo2 = []
	bili  = []

	ref = db.reference(abs_path)
	
	def convert_timestamp(date,hour,mins):
		sec = "0"
		input_datetime = date +" " + hour+":"+ mins +":"+ sec
		date_time_obj = datetime.strptime(input_datetime, '%d/%m/%y %H:%M:%S')
		#print("python date time object: ",date_time_obj)
		timestamp = str(int(datetime.timestamp(date_time_obj)))
		#print(timestamp)
		return timestamp
	start_time = convert_timestamp(date = start_date ,hour = start_hour ,mins = start_min )
	end_time = convert_timestamp(date = end_date ,hour = end_hour ,mins = end_min )

	data = ref.order_by_child("timestamp").start_at(start_time).end_at(end_time).get()

	data = dict(data).values()
	data = list(data)
	#print(data)
	for i in data:
	 	hr.append(i.get("hr"))
	 	ecg += (i.get("ecg"))
	 	spo2.append(i.get("spo2"))
	 	bili.append(i.get("bili"))

	return(ecg,hr,spo2, bili)

last_val = get_values( abs_path )
print("ECG :" ,last_val[0])
print("hr :" , last_val[1])
print("spo2 :" , last_val[2])
print("bilirubin :" , last_val[3])
print("")


range_val = get_range_values (abs_path, 
					start_date = "02/01/22", start_hour = '22' , start_min = '50' , 
					end_date = "02/01/22", end_hour =  "22" , end_min = "53" )

print("ECG :" ,range_val[0])
print("hr :" , range_val[1])
print("spo2 :" , range_val[2])
print("bilirubin :" , range_val[3])
print("")

'''
plt.figure(1)
plt.plot(range_val[0])
plt.grid()
plt.show()
plt.savefig("ecg.png")

plt.figure(2)
plt.plot(range_val[1])
plt.grid()
plt.show()
plt.savefig("hr.png")

plt.figure(3)
plt.plot(range_val[2])
plt.grid()
plt.show()
plt.savefig("spo2.png")
'''



