from django.views.generic.simple import direct_to_template
from django.contrib.auth import login

from forms import AuthForm

def main_page(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            login(request, form.user)
    else:
        form = AuthForm()
    return direct_to_template(request, 'core/main_page.html', {'form': form, 'user': request.user})

    
