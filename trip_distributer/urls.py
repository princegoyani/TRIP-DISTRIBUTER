from django.urls import path

from . import views

urlpatterns = [
    path("index/<str:username>" , views.index , name="index"),
    path("addtrip" , views.add_trip , name="addtrip"),
    path("endtrip" , views.end_trip , name="endtrip"),  
    path("trip/<int:tripid>" , views.trip_view , name="view_trip"),
    path("add_user", views.add_user , name="add_user"),
    path("delete_trip" , views.delete_trip , name="delete_trip"),
    path("remove_spend" , views.remove_spend , name="remove_spend"),
    path("spend", views.add_spend , name= "add_spend"),
    path("add_user_to_trip" , views.add_user_to_trip , name="add_user_to_trip"),
    path("save_trip" , views.save_trip  , name="add_trip"),
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")

]