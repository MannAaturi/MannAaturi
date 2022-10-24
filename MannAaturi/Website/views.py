import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Video, Message, Pdf

# Create your views here.

def Home(request):
    return render(request, "Home.html")

def Signup(request):
    return render(request, "Signup.html")

def Signing_In(request):
    """Creates New User If It Does Not Exist Already."""
    if request.method == 'POST':
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        
        if not username.isalnum():
            messages.error(request, "Username Can Only Contain Letters And Numbers !")
            return render(request, "Login.html")
        else:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Account Created Successfully ! You May Login Now !")
            return render(request, "Home.html")

def Login(request):
    return render(request, "Login.html")

def Logging_In(request):
    """Log Ins User If It Exists."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully !")
            return render(request, "Home.html")
            
        else:
            messages.error(request, "Invalid Credentials ! Please Try Again !")
            return render(request, "Login.html")

def Logout(request):
    """Logs Out The User."""
    logout(request)
    messages.success(request, "Logged Out Successfully !")
    return render(request, "Login.html")

def Videos(request):
    """Fetches Videos From Database And Shows To The User."""
    obj = Video.objects.all()
    return render(request, "Videos.html", {'obj' : obj})

def Contact(request):
    """Shows Contact Page To The User."""
    return render(request, "Contact.html")

def Sending_Message(request):
    """Saves Contact Message To Database."""
    if request.method == "POST":
        Email = request.user.email
        username = request.user.username
        fname = request.POST['fname']
        lname = request.POST['lname']
        msg = request.POST['msg']
        data = Message(Email=Email, Username=username, First_Name=fname, Last_Name=lname, Message=msg)
        data.save()
        messages.success(request, "I have received Your Message ! I will Reach Out to you via Email As Soon As Possible !")
        return render(request, "Home.html")

def PDF(request):
    """Shows PDF Page To The User."""
    context = {'files' : Pdf.objects.all()}
    return render(request, "PDFs.html", context)

def Download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/File")
            response['Content-Diposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404

def Search(request):
    """Handles Search Function For Videos."""
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            vid = Video.objects.filter(Title__icontains=query) 
            return render(request, 'Results_Videos.html', {'results':vid})
        else:
            return HttpResponse("No Information To Show !")

def Search_PDF(request):
    """Handles Search Function For PDFs.."""
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            pdf = Pdf.objects.filter(Title__icontains=query) 
            return render(request, 'Results_PDFs.html', {'results':pdf})
        else:
            return HttpResponse("No Information To Show !")
    