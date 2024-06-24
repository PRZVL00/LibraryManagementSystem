from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transactionhistory/', views.transactionhistory, name='transactionhistory'),
    path('timeintimeout/', views.timeintimeout, name='timeintimeout'),
    path('user-management/', views.usermanagement, name='usermanagement')
]
