from django.shortcuts import render, redirect
from recommendation.models import Login, Signup
from joblib import load

model = load('./saveModels/model.joblib')
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    # Check if the user has visited either the "signup" or "login" page
    if not request.session.get('user_authenticated', False):
        return redirect('login')  # Redirect to login page if not authenticated
    return render(request, 'about.html')

def service(request):
    # Check if the user has visited either the "signup" or "login" page
    if not request.session.get('user_authenticated', False):
        return redirect('login')  # Redirect to login page if not authenticated

    if request.method == "POST":
        N = int(request.POST.get('N'))
        P = int(request.POST.get('P'))
        K = int(request.POST.get('K'))
        temperature = float(request.POST.get('temperature'))
        humidity = float(request.POST.get('humidity'))
        ph = float(request.POST.get('ph'))
        rainfall = float(request.POST.get('rainfall'))
        y_pred = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])
        return render(request, 'service.html', {'result': y_pred[0]})
    else:
        return render(request, 'service.html')

def login(request):
    if request.method == "POST":
        # ... your existing code for handling the login POST request ...
        # After successful login, set the session variable to indicate user authentication
        request.session['user_authenticated'] = True
        return redirect('about')  # Redirect to the "about" page after successful login
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        # ... your existing code for handling the signup POST request ...
        # After successful signup, set the session variable to indicate user authentication
        request.session['user_authenticated'] = True
        return redirect('about')  # Redirect to the "about" page after successful signup
    return render(request, 'signup.html')
