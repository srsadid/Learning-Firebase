#https://www.codespeedy.com/connecting-firebase-with-python/
#https://morioh.com/p/a593f973aff0
import firebase_admin
from firebase_admin import credentials,firestore
from firebase_admin import db

#initializing the credentials of the app
# after creating app project settings>service account> generate new private key
cred = credentials.Certificate("mist-pmx-firebase-adminsdk-php5z-f6d7dcba56.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mist-pmx-default-rtdb.firebaseio.com/'
})
ref = db.reference('mist-pmx-default-rtdb')
