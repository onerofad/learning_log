from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # No data submitted, return blank form
        form = UserCreationForm()
    else:
        # data submitted, data process
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()

            # Log the user in and redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')

    
    # Display blank or invalid form
    context = {'form' : form}
    return render(request, 'registration/register.html', context)


