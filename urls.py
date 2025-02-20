
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth import views as auth_views
from django.urls import path





urlpatterns = [
   path('signup/',register,name='signup'),
   path('update/',update,name='update'),
   path('profile/',prof,name='profile'),
   path('login/',login,name='login'),
   path('recycle/',recycle,name='recycle'),
   path('collect/',collect,name='collect'),
   path('request_pickup/', request_pickup, name='request_pickup'),
   path('',home,name='home'),
   path('logout/', logout, name='logout'),
   path('categories/',category_list, name='categories'),
   path('categories/<int:category_id>/',scrap_list, name='buy1'),
   path('buy/<int:scrap_id>/',buy_scrap, name='check'),
   path('about/', about, name='about'),
   path('compost/', compost, name='compost'),
   path('contact/', contact, name='contact'),
   path('checkout/', checkout, name='checkout'),
   path("order_success/<int:order_id>/", order_success, name="order_success"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)