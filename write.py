#https://www.codespeedy.com/connecting-firebase-with-python/
import firebase_admin
from firebase_admin import credentials,firestore
import datetime; 
  
# ct stores current time 
dt = datetime.datetime.now() 
print("current time:-", dt) 

#initializing the credentials of the app
# after creating app project settings>service account> generate new private key
cred = credentials.Certificate("mist-pmx-firebase-adminsdk-php5z-f6d7dcba56.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
patients = db.collection(u'patient 01').document(str(dt))
patients.set({
    u'ecg': [31, 32, 33, 34, 36], u'bp dia': 10, u'bp sys': 1000, u'spo2': 9, u'temp': 3 
})