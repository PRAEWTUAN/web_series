from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash


def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, 'login.html')  # ตัวอย่างการเรนเดอร์เทมเพลต login


# def logout(request):
#     auth.logout(request)
#     messages.success(request, 'คุณได้ออกจากระบบเรียบร้อยแล้ว')  # แสดงข้อความยืนยันการออกจากระบบ
#     return redirect('login')  # เปลี่ยนเส้นทางไปยังหน้าเข้าสู่ระบบ


def addUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username นี้ซ้ำ')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email นี้ซ้ำ')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password
                )
                user.save()
                messages.success(request, 'Registration successful')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return redirect('signup')

def loginForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')  # เปลี่ยนให้ไปยังหน้า home แทน
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('login')

