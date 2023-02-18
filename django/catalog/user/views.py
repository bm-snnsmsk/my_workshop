from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(request) :
    if request.method == 'POST' :
        
        ## get form values 
        username = request.POST['username']
        parola = request.POST['parola']

        user = auth.authenticate(username=username, password=parola)
        if user is not None :
            auth.login(request, user)
            print("login başarılı")
            messages.add_message(request, messages.SUCCESS, 'Oturum açıldı')
            return redirect('index')
        else:
            print("kullanıcı adı veya parola yanlış")
            messages.add_message(request, messages.ERROR, 'kullanıcı adı veya parola yanlış')
            return redirect("login")
    else :
       return render(request,"user/login.html") 

    

def register(request) :
    if request.method == 'POST' :
        print("submitted")
        ## get form values 
        username = request.POST['username']
        email = request.POST['email']
        parola = request.POST['parola']
        reparola = request.POST['reparola']

        if parola == reparola :
            ## database de böyle bir kullanıcı varmı
            if User.objects.filter(username = username).exists() :
                messages.add_message(request, messages.WARNING, 'bu kullanıcı mevcut')
                print("bu kullanıcı mevcut")
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists() :
                    messages.add_message(request, messages.WARNING, 'Bu email mevcut')
                    print("bu email  mevcut")
                    return redirect('register')
                else :
                    ## kayıt yapılabilir
                    #user = User.objects.create_user(username=username, password= parola, email=email)
                    user = User.objects.create_superuser(username=username, password= parola, email=email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'kullanıcı oluşturuldu')
                    print("kulanıcı oluşturuldu")
                    return redirect('login')
        else :
            messages.add_message(request, messages.WARNING, 'parolalar eşleşmiyor')
            print("prolalar eşleşmiyor")
            return redirect('register')
    else :
        return render(request,"user/register.html") 

def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'çıkış başarılı')
        return redirect("login") 
