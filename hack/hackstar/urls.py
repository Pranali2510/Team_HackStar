from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("checkout", views.checkout, name="checkout"),

    path("", views.home, name="Home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="about"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("event_dashboard", views.event_dashboard, name="event_dashboard"),
    path("view_order/<int:id>", views.view_order, name="view_order"),
    path('delete_order/<int:id>/', views.delete_order, name='delete_order'),

    path("canteen", views.canteen, name="canteen"),
    path("cleanliness", views.cleanliness, name="cleanliness"),
    path("view_cleanliness", views.view_cleanliness, name="view_cleanliness"),
    path("viewcl", views.viewcl, name="viewcl"),
    path("viewl", views.viewl, name="viewl"),
    path("view_canteen", views.view_canteen, name="view_canteen"),
    path("view_lost", views.view_lost, name="view_lost"),
    path("update_cleanliness/<int:id>/", views.update_cleanliness, name="update_cleanliness"),
    path("update_canteen/<int:id>/", views.update_canteen, name="update_canteen"),
    path("event", views.event, name="event"),
    path("lostfound", views.lostfound, name="lostfound"),
    path('delete/<int:id>/', views.delete, name='delete'),
    path("update_lost/<int:id>/", views.update_lost, name="update_lost"),
    path('delete_lost/<int:id>/', views.delete_lost, name='delete_lost'),
    path("signin", views.signin, name="signin"),
    path("user_dashboard", views.user_dashboard, name="userdashboard"),
    path("cleanniness_dashboard", views.cleanniness_dashboard, name="admindash"),
    path("canteen_dashboard", views.canteen_dashboard, name="canteendash"),
    path("lostfounddashboard", views.lostfounddashboard, name="lostfounddash"),
    path("registeruser/", views.registeruser, name="registeruser"),
    path("loginuser/", views.loginuser, name="loginuser"),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path("postevent/", views.postevent, name="postevent"),
    path("create_event/", views.create_event, name="create_event"),
    path("view_event/", views.view_event, name="view_event"),
    path("registerevent/", views.registerevent, name="registerevent"),

]
