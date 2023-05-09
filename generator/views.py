from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, "pages/home.html")

def kontakt(request):
    return render(request, "pages/kontakt.html")   

def cenik(request):
    return render(request, "pages/cenik.html")

def sluzby(request):
    return render(request, "pages/sluzby.html")   

def password(request):
    # Základní nastavení
    result_password = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

    # Načítáme hodnoty z formuláře přes URL adresy
    let_length = int(request.GET.get("letters"))
    big_length = int(request.GET.get("big_letters"))
    num_length = int(request.GET.get("numbers"))
    spec_length = int(request.GET.get("special"))


    # Ze seznamu vybíráme počet hodnot podle údajů z form
    for _ in range(let_length):
        result_password.append(random.choice(letters))

    for _ in range(big_length):
        result_password.append(random.choice(big_letters))

    for _ in range(num_length):
        result_password.append(random.choice(numbers)) 

    for _ in range(spec_length):
        result_password.append(random.choice(special_char))  

    #Zamícháme pořadím
    random.shuffle(result_password)   

    #převod listu na text
    final_password = ""
    for one_letter in result_password:
        final_password = final_password + one_letter   


    return render(request, "pages/password.html", {"heslo": final_password})     

