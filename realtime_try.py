import firebase_admin
from firebase_admin import credentials,firestore
from firebase_admin import db
import pandas as pd
from matplotlib import pyplot as plt
#initializing the credentials of the app
# after creating app project settings>service account> generate new private key
cred = credentials.Certificate("private_key_fb.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pmss-7fd59-default-rtdb.firebaseio.com/'
})
unique_id ="6"
# Get a database reference to our posts
ref = db.reference("/doctor_" + unique_id + "/patient_8/")
print(ref.get())

