from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# a dictionary 
monthly_challenges = {
    'january': "Eat meat for the entire month",
    'febuary': "walk for atleast 20 minutes everyday",
    'march':"Learn Django for at least 20 minutes every dar",
    'april': "Eat o meat for at least 20 miutes veryday",
    'may': "Eat meat for the entire month",
    'june': "walk for atleast 20 minutes everyday",
    'july':"Learn Django for at least 20 minutes every dar",
    'agust': "Eat o meat for at least 20 miutes veryday",
    'september': "walk for atleast 20 minutes everyday",
    'octorber':"Learn Django for at least 20 minutes every dar",
    'november': "Eat o meat for at least 20 miutes veryday",
    'december': "Eat o meat for at least 20 miutes veryday..::"
}

# Create your views here.

# coverting dictionary to a list 
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    # These make gives a codition o redirection on the url maybe if number entered is greater the length of the list
    if month > len(months):
        return HttpResponseNotFound("invalid month")

    # the redirect_month variable make 
    redirect_month = months[month - 1  ]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This is not supported")
    return HttpResponse(challenge_text)