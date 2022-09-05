#https://www.codespeedy.com/connecting-firebase-with-python/
import firebase_admin
from firebase_admin import credentials,firestore
import csv
#initializing the credentials of the app
# after creating app project settings>service account> generate new private key
cred = credentials.Certificate("pmx-test-5687a-firebase-adminsdk-joinr-5f724091d2.json")
firebase_admin.initialize_app(cred)

csv_columns = ['spo2', 'bp sys', 'bp dia', 'ecg', 'temp']
csv_file = "patient.csv"

try:
	with open(csv_file, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
		writer.writeheader()
except IOError:
	print("I/O error")

db = firestore.client()
patients = db.collection(u'patient 01')
docs = patients.stream()
for doc in docs:
    #print('{} : {}'.format(doc.id,doc.to_dict()))
    dictionary  = doc.to_dict()
    try:
    	with open(csv_file, 'a') as csvfile:
    		writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    		#writer.writeheader()
    		writer.writerow(dictionary)
    except IOError:
    	print("I/O error")

    print("successfully updated !")





#try:
#    with open(csv_file, 'a') as csvfile:
#        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#        #writer.writeheader()
#        writer.writerow(dictionary)
#except IOError:
#    print("I/O error")