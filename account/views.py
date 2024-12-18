from django.core.checks import messages
from django.shortcuts import render, redirect
from .forms import LoginForm, OTPForm, RegisterForm
from .utils import send_otp
from .models import OTP
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login


def phone_number_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            send_otp(phone)
            return redirect('account:enter_otp', phone=phone)
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def enter_otp_view(request, phone):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp']
            try:
                otp_instance = OTP.objects.filter(phone=phone, code=otp_code, is_used=False).latest('created_at')
                if otp_instance.is_valid():
                    otp_instance.is_used = True
                    otp_instance.save()
                    request.session['phone'] = phone
                    print(f"Phone saved in session: {request.session['phone']}")
                    return redirect('account:complete_registration')
                else:
                    form.add_error('otp', 'Invalid or expired OTP')
            except OTP.DoesNotExist:
                form.add_error('otp', 'Invalid OTP')
    else:
        form = OTPForm()

    return render(request, 'account/register.html', {'form': form, 'phone': phone})



def complete_registration(request, phone):
    # phone = request.session.get('phone')  # از session شماره تلفن را می‌گیریم
    if not phone:
        return redirect('account:phone_number_view')  # اگر شماره تلفن موجود نیست، کاربر را به صفحه شماره تلفن برگردانیم

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.phone = phone
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home:home')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {'form': form, 'phone': phone})




@login_required
def profile_view(request):
    return render(request, 'account/profile.html')

def logout_view(request):
    logout(request)
    return redirect('account:phone_number_view')