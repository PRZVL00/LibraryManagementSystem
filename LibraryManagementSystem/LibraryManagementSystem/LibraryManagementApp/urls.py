from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('reset-password/', views.passwordrecovery, name='passwordrecovery'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('book-browsing/', views.bookbrowsing, name='bookbrowsing'),
    path('transactionhistory/', views.transactionhistory, name='transactionhistory'),
    path('timeintimeout/', views.timeintimeout, name='timeintimeout')
]
