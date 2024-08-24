from django.contrib import admin
from django.urls import path,include
from home import views
from Stock import views as sviews

urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path("about",views.about,name='about'),
    path("service",views.service,name='service'),
   
    path("testimonial",views.testimonial,name='testimonial'),
    path("team",views.team,name='team'),
    path("project",views.project,name='project'),
    path("feature",views.feature,name='feature'),
    path("contact",views.contact,name='contact'),
    #path("about",views.about,name='about'),



    


    path("signup",views.signup,name='signup'),
    path("login",views.LoginPage,name='login'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("marketing",views.marketing,name='marketing'),

   
    
    
    path("stock", sviews.stock, name="stock"),
    path("predict", sviews.predict, name="predict"),
    path("predict_stock/<str:symbol>/<str:period>/<int:sim>/<int:future>", sviews.stock_predict, name="predict_stock"),
    path("trade", sviews.trade, name="trade"),
    path("trade_stock/<str:symbol>/<str:period>/<int:init>/<int:skip>", sviews.stock_trade, name="trade_stock")
]


