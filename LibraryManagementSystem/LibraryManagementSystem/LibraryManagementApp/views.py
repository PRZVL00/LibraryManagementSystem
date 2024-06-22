from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'LoginPage/login.html', {})

def dashboard(request):
    return render(request, 'DashboardPage/dashboard.html', {})

def transactionhistory(request):
    return render(request, 'TransactionHistoryPage/transactionhistory.html', {})

def timeintimeout(request):
    return render(request, 'TimeinTimeoutPage/timeintimeout.html', {})