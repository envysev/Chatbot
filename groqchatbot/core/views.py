from django.shortcuts import render, redirect
from django.contrib.auth import logout
import requests
from django.contrib.auth.decorators import login_required


def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')

import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required
def chatbot(request):
    response_text = None
    prompt = None

    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {settings.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        groq_response = requests.post(url, headers=headers, json=payload)

        if groq_response.status_code == 200:
            data = groq_response.json()
            try:
                response_text = data['choices'][0]['message']['content']
            except (KeyError, IndexError):
                response_text = "⚠️ Unexpected response format from Groq API."
        else:
            response_text = f"❌ Error {groq_response.status_code}: {groq_response.text}"

    return render(request, 'chatbot.html', {
        'response': response_text,
        'prompt': prompt
    })

def logout_view(request):
    logout(request)
    return redirect('dashboard')


from social_django.models import UserSocialAuth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

@login_required
def disconnect_github(request):
    try:
        request.user.social_auth.get(provider='github').delete()
        messages.success(request, "Your GitHub account was disconnected. Please log out from GitHub (https://github.com/logout) to fully remove access.")
    except UserSocialAuth.DoesNotExist:
        messages.error(request, "No GitHub account is linked.")
    return redirect('dashboard')