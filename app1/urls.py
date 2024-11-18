from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('regAcc',views.regAcc,name='regAcc'),
    path('confirmlogin',views.confirmlogin,name='confirmlogin'),
    path('success',views.suclogin,name='suclogin'),
    path('logout',views.logout,name='logout'),
    path('addnewpie',views.addnewpie,name="addnewpie"),
    path('editpieview/<int:id>',views.editpieview,name="editpieview"),
    path('editpie',views.editpie,name='editpie'),
    path('deletepie/<int:id>',views.deletepie,name="deletepie"),
    path('allpies',views.allpies,name='allpies'),
    path('pieview/<int:id>',views.pieview,name='pieview')
]