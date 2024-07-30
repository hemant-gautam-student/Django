from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Raju'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=val1+val2
    name = request.POST["username"]
    return render(request,'results.html',{'result':val3, 'username':name})
 
# def inputname(request):

def dashboard(request):
    return render(request,'dashboard.html')
    