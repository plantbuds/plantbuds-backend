from django.http import HttpResponse
import pyrebase

firebaseConfig = {
    'apiKey': "${FIREBASE_KEY}",
    'authDomain': "plantbuds-110.firebaseapp.com",
    'databaseURL': "https://plantbuds-110.firebaseio.com",
    'projectId': "plantbuds-110",
    'storageBucket': "plantbuds-110.appspot.com",
    'messagingSenderId': "165337168830",
    'appId': "1:165337168830:web:2ab03bb5a5565a13f2d7ef",
    'measurementId': "G-BYFCNFSWJL",
    'serviceAccount': "./credentials.json",
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


# Example route to retrieve data
def get_user(request, user_id):
    if request.method == 'GET':
        users = db.child("people").child(user_id).get()
        return HttpResponse(f"{users.val()}")
    else:
        # Normally this would be a 500 Bad Request code
        return HttpResponse("Invalid request")