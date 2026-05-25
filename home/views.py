from django.shortcuts import render,redirect
from .forms import registeration
from django.contrib.auth import authenticate,login,logout
def index(request):
    return render(request,'index.html')

def login_user(request):
    if request.method=='POST': 
        form=registeration(request.POST) 
        if form.is_valid():
             user = form.save(commit=False) 
             user.set_password(form.cleaned_data['password'])
             user.save() 
             return redirect('go_login_otp') 
    else: 
        form=registeration() 
    return render(request,'login_regis.html',{'form':form})
    

def user_logout(request):
    logout(request)
    return redirect('home')

def otp(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(
            username=username,
            password=password
        )

        print(user)

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            return render(request, 'login_otp.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login_otp.html')