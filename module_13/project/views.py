from django.shortcuts import render

all_users = []

def home(request):
    return render(request, 'project/index.html')

def form(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('email')
        all_users.append({"name": name, "email": email})
        return render(request, 'project/users.html')
    else:
        return render(request, 'project/form.html')

def users(request):
    return render(request, 'project/users.html', {
        "users": all_users
        })