from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, CustomPasswordResetForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import logging

# Configurez le logger
logger = logging.getLogger(__name__)

User = get_user_model()


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        logger.debug(f"Checking if email {email} exists in the database.")  # Log for debugging

        if User.objects.filter(email=email).exists():
            logger.debug(f"Email {email} exists. Proceeding with password reset.")  # Log for debugging
            form.save(
                request=self.request,
                use_https=self.request.is_secure(),
                email_template_name=self.email_template_name,
                subject_template_name=self.subject_template_name,
            )
            return super().form_valid(form)
        else:
            logger.debug(f"Email {email} does not exist. Showing error message.")  # Log for debugging
            messages.error(self.request, _('No account found with that email address.'))
            return self.form_invalid(form)
        

# Vue pour l'inscription
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Vue pour la connexion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Vue pour le profil de l'utilisateur connecté
@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

# Vue pour la confirmation de déconnexion
def logout_confirm(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Sorry to see you go! See you soon.')
        return redirect('login')
    return render(request, 'users/logout_confirm.html')
