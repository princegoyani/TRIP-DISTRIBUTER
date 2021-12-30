import json


from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import render
from datetime import date, datetime
from .models import User , Trip ,Notification , Spending


# Create your views here.
@csrf_exempt
@login_required(login_url='')
def index(request , username):
    try:
        notifications = Notification.objects.get(user  = request.user)
        notifications_list = list(notifications.trip.all())
        print(notifications_list)
    except Notification.DoesNotExist:
        pass

    current_trip = list(request.user.users_ontrip.filter(status="current").order_by("-start_date") )
    print(current_trip)

    completed_trips = list(request.user.users_ontrip.filter(status="end").order_by("-end_date"))
    print(completed_trips)


    return render(request ,"trip_distributer/index.html" , {
        "username":username,
        "notifications" : notifications_list,
        "current_trips": current_trip,
        "completed_trips":completed_trips

    })


@csrf_exempt
@login_required(login_url='')
def end_trip(request):
    if request.method== "POST":
        print("ending")
        trip_id = json.loads(request.body)["trip_id"]
        trip = Trip.objects.get(id = int(trip_id))
        trip.status = "end"
        trip.end_date = datetime.now().date()
        trip.save()
    return HttpResponse("ENDED")


@csrf_exempt
@login_required(login_url='')
def add_user(request):
    print("here")
    if request.method == "POST":
        username_toadd = json.loads(request.body)['user_toadd']

        try: 
            if username_toadd == request.user.username:
                print(request.user , "here")
                raise User.DoesNotExist
            user = User.objects.get(username= username_toadd)
            return JsonResponse({"post":"accepted"})
        except User.DoesNotExist:
            return JsonResponse({"post":"no_such_user"})
    



@csrf_exempt
@login_required(login_url='')
def trip_view(request, tripid):

    trip= Trip.objects.get(id= tripid)
    users_on_trip = list(trip.user_ontrip.all())
    
    total_spend = 0
    for spend in trip.trip_spend.all() :
        total_spend += spend.spend

    print(total_spend)
    a = {}
    for user in users_on_trip:
        user_total_spend= 0
        print(user.user_spend.filter(trip = trip))
        for user_spend in user.user_spend.filter(trip = trip):
            user_total_spend += user_spend.spend
        a[user.username] = [ round(user_total_spend ,2 ) , round(user_total_spend -(total_spend/len(users_on_trip)), 2 )]

    print(a)  
    

    if request.user in users_on_trip:
        return render(request , "trip_distributer/trip.html" , {
            "trip" : trip,
            "total_spend":total_spend,
            "users_spend":a

        })

@csrf_exempt
@login_required(login_url='')        
def remove_spend(request):
    if request.method == "POST":
        print(json.loads(request.body)["spend_id"])
        spend_id =  json.loads(request.body)["spend_id"]
        spend = Spending.objects.get( id = int(spend_id) )
        spend.delete()
    return HttpResponse("<h1> REMOVED </h1>")
        




@csrf_exempt
@login_required(login_url='')
def add_spend(request):

    if request.method == "POST":
        trip_id = int(json.loads(request.body)['trip_id'])
        description = json.loads(request.body)['desciption']
        spend = int(json.loads(request.body)['spend'])
        trip = Trip.objects.get(id = trip_id)
        
        print(trip_id , description , spend)
        add_spend_to_model =  Spending.objects.create(trip = trip ,user= request.user ,  description = description , spend = spend , date_time = datetime.now() )
        add_spend_to_model.save()
        return JsonResponse({"user": request.user.username , "date_time":str(datetime.now()) })
    return HttpResponse("spend_Added")


@csrf_exempt
@login_required(login_url='')
def save_trip(request):
    if request.method == "POST":
        trip_name = json.loads(request.body)['trip_name']
        user_toadd_list = json.loads(request.body)['user_torequest']
        print(trip_name)
        print(user_toadd_list)

        trip_toadded = Trip.objects.create(
            trip_name = trip_name,
            user_tohost = request.user,
            start_date = date.today()
        )
        trip_toadded.user_ontrip.add(request.user)
        trip_toadded.save()

        notification(trip_toadded.id , user_toadd_list )
    
    return HttpResponseRedirect( reverse("index" , kwargs={"username": request.user}))


def notification(trip_id , user_list):    
    for user_fromlist in user_list:
        try :
            user_id = User.objects.get(username = user_fromlist)
        except User.DoesNotExist :
            continue

        try : 
            get_user_notifications = Notification.objects.get(user = user_id)
        except Notification.DoesNotExist :
            get_user_notifications = Notification.objects.create(user = user_id)

        get_user_notifications.trip.add(trip_id)
        get_user_notifications.save()
        print("notifications_sented")
        
        
@csrf_exempt
@login_required(login_url='')
def add_user_to_trip(request):
    print("here")
    print(request.method)
    if request.method == "POST":
        json_load = json.loads(request.body)
        print(json_load)
        trip_id = json_load['trip_id']    
        user_response = json_load['user_response']
        print(user_response)
        try : 
            notification = Notification.objects.get(user = request.user )
            if notification.trip.get(id = trip_id):
                if user_response == "accept":
                    trip  = Trip.objects.get(id= trip_id)
                    trip.user_ontrip.add(request.user)
                    print("Added")
                notification.trip.remove(trip_id)
                return JsonResponse({
                    "trip_name": trip.trip_name,
                    "trip_start_date": trip.start_date

                })   
            else:
                raise Notification.DoesNotExist
        except Notification.DoesNotExist:
            HttpResponse("<h2>DOES NOT EXIT</h2>")
        return HttpResponse("REQUEST SENT")
    else:
        return HttpResponse("NOT SENT")


@csrf_exempt
@login_required(login_url='')
def delete_trip(request):
    print("here")
    if request.method == "POST":
        trip_id = json.loads(request.body)["trip_id"]
        trip = Trip.objects.get(id = int(trip_id))
        if request.user == trip.user_tohost:
            trip.delete()
        else:
            trip.user_ontrip.remove(request.user)
    return HttpResponseRedirect(reverse('index' , kwargs={'username': request.user}))


@csrf_exempt
@login_required(login_url='')
def add_trip(request):
    return render(request ,"trip_distributer/addtrip.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(f"index/{username}")
        else:
            return render(request, "trip_distributer/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_authenticated :
            return HttpResponseRedirect(reverse('index', kwargs={'username': request.user}))
        return render(request, "trip_distributer/login.html")



@login_required(login_url='')
def logout_view(request):
    print("logout")
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    
    if request.method == "POST":
        print("here" , request.POST)
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "trip_distributer/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name = firstname , last_name = lastname)
            user.save()
        except IntegrityError:
            return render(request, "trip_distributer/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index") , kwargs={'username':request.user})
    else:
        return render(request, "trip_distributer/register.html")
