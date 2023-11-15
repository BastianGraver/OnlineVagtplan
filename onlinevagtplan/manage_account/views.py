from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from manage_account.models import Users, Shifts, Movies

# Create your views here.
def home(request):
    # Placeholder for index page
    return render(request, "home.html", context={"users": Users.objects.all()})

def login(request):
    # Placeholder for login page
    print("Login page under construction")
    return HttpResponseRedirect("/")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the provided username and password match a user in the database
        try:
            user = Users.objects.get(username=username)
            print(user.username, user.password, username, password)
            if user.password == password:
                # Asks super to user admin login
                if user.type == 'Super':
                    # Show an alert if the user is of type "super"
                    return render(request, "user_login.html", context={"alert_message": "Please use the admin login."})
                                        
                return render(request, "welcome.html", context={"user_name": user.name,
                                                                "user_id" : int(user.id),
                                                                "shifts": Shifts.objects.all(),
                                                                "movies": Movies.objects.all()})
        except Users.DoesNotExist:
            # User does not exist
            pass

    # If login failed, or it's a GET request, render the login page
    return render(request, "user_login.html")