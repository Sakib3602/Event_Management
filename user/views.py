from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def Sign_Up(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
        else:
            print("Form errors: ", form.errors)
    
    return render(request, "registration.html", {"form":form})