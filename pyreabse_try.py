#https://github.com/thisbejim/Pyrebase
import pyrebase
import sys
from datetime import datetime
from bisect import bisect_left

config = {
  "apiKey": "AIzaSyD9InLOfFAP9QruzyvtYRT8sJs99xHDcAw",
  "authDomain": "pmss-7fd59.firebaseapp.com",
  "databaseURL": "https://pmss-7fd59-default-rtdb.firebaseio.com",
  "storageBucket": "pmss-7fd59.appspot.com"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()

#### all of the inputs 
'''
path = '/doctor_7/patient_8/'
input_date_start = "12/04/21"
input_hour_start = "22"
input_min_start = "42"

input_date_end = "12/04/21"
input_hour_end = "22"
input_min_end = "48"
'''

def range_value(path,date_start,hour_start,min_start,date_end,hour_end,min_end):

	def noquote(s):
	    return s
	pyrebase.pyrebase.quote = noquote

	#gets all the keys and stores them in a list

	each_time_list = []
	all_user_ids = db.child(path).get()
	for user in all_user_ids.each():
		each_time_list.append(user.key())
		#print("python date time object: ", datetime.fromtimestamp(int(user.key())))
		#print("timestamp: ", user.key())

	print(each_time_list)



	#taking the date time input and changing to the timestamp
	print("")
	def index_from_time(date,hour,mins):
		for i in range(0,60):
			sec = str(i)
			input_datetime = date +" " + hour+":"+ mins +":"+ sec
			date_time_obj = datetime.strptime(input_datetime, '%d/%m/%y %H:%M:%S')
			#print("python date time object: ",date_time_obj)
			timestamp = str(int(datetime.timestamp(date_time_obj)))
			#print("timestamp: ", timestamp)
			list_available = (timestamp <= each_time_list[-1]) and (each_time_list[bisect_left(each_time_list, timestamp)] == timestamp)
			
			if list_available == True:
				time_index = each_time_list.index(timestamp)
				break
			else:
				time_index = 'none'

		return(time_index , timestamp)

	start_time_index,start_timestamp = index_from_time(date_start,hour_start,min_start)
	print(start_time_index)

	end_time_index , end_timestamp = index_from_time(date_end,hour_end,min_end)
	print(end_time_index)

	ecg_list = []
	spo2_list = []
	hr_list = []

	if  start_time_index or end_time_index == "none":
		print("input range not set properly") 

	else:

		# takes into concederation of all the values that are in the range and stores the values accordingly 

		for item in each_time_list[start_time_index:end_time_index+1]:
			
			#gets all the vlues once and stores in respective lists after converting to python dictionary 
			users = db.child(path + item + '/').get().val()
			dict_users = dict(users)
			hr_list.append(dict_users.get("hr"))
			spo2_list.append(dict_users.get("spo2"))
			ecg_list += dict_users.get("ecg")

	return [spo2_list,hr_list,ecg_list]


values = range_value(path = '/doctor_7/patient_8/' ,
					date_start = "12/04/21" , hour_start = "22" , min_start = "42" ,
					date_end = "12/04/21" , hour_end = "22" , min_end = "49")

print( "spo2 values: " , values[0])
print( "hr values: " , values[1])
print( "ecg values: " , values[2])


