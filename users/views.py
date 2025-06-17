# from django.contrib.auth import authenticate
# from django.contrib.auth import login as user_login
# from django.shortcuts import redirect, render


# def login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=user_name, password=password)
#         if user:
#             user_login(request, user)
#             return redirect("/")
#         else:
#             print("Please enter the valid cred")

#     return render(request, "login.html")
