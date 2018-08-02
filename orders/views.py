from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse, HttpResponseRedirect


# for login
def user_login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/pinocchios/dash.html')
        else:
            error = " Sorry! Phone Number and Password didn't match, Please try again ! "
            return render(request, 'pinocchios/index.html',{'error':error})
    else:
        return render(request, "pinocchios/index.html")

# for signup
def users_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if pass_1 == pass_2:
             user = User.objects.create_user(
                                              username=phone,
                                              email=email,
                                              password=pass_1,
                                             )
             return HttpResponseRedirect("/")
        else:
             error = " Password Mismatch "
             return render(request, "pinocchios/signup.html",{"error":error})
    else:
         return render(request, "pinocchios/signup.html")

# loggout
def logout_view(request):
    logout(request)
    return render(request, "pinocchios/index.html", {"message": "Logged out."})


# the dash bord view
# def dash_view(request):
#     context = {
#         "pizza" : Pizza.objects.all()
#         "sub" : Sub.objects.all()
#         "toppings": Topping.objects.all()
#         "salad": Salad.objects.all()
#         "dinnerplate": DinnerPlate.objects.all()
#     }
#     return render(request, "pinocchios/dash.html", context)
