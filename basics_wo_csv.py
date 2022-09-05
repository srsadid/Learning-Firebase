#https://www.codespeedy.com/connecting-firebase-with-python/
import firebase_admin
from firebase_admin import credentials,firestore
import csv
import pandas as pd

#initializing the credentials of the app
# after creating app project settings>service account> generate new private key
cred = credentials.Certificate("mist-pmx-firebase-adminsdk-php5z-f6d7dcba56.json")
firebase_admin.initialize_app(cred)

csv_columns = ['spo2', 'temp' , 'ecg']
data_list = []

db = firestore.client()
patients = db.collection(u'patient 01')
docs = patients.stream()
for doc in docs:
    #print('{} : {}'.format(doc.id,doc.to_dict()))
    dictionary  = doc.to_dict()
    data_list.append(dictionary)

#print(data_list)
df = pd.DataFrame(data_list, columns= csv_columns)
print(df)  