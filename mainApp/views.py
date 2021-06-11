from django.shortcuts import render, redirect
import random

def index(request):
    
    if 'activity' not in request.session:
        request.session['activity'] = ["string", "something_else"]
    if 'activity1' not in request.session:
        request.session['activity1'] = []

    if 'gold' not in request.session:
        request.session['gold'] = 0
    context = {
        'gold': request.session['gold'],
        'activity': request.session['activity']
    }
    return render(request, 'index.html', context)

def process_money(request):
    
    if request.POST["which_form"] == "farm":
        # print(str(request.session['gold']))
        test = request.session['activity']
        gold_gained = getRandomNum(10, 20)
        log = "Earned " + str(gold_gained) + " gold from the farm!"
        request.session["gold"] += gold_gained
        request.session['activity1'].append(log)
        print(request.session["activity1"])
        print (str(request.session['gold']))
        print(log)
        return redirect("/")

    if request.POST["which_form"] == "cave":
        # print (str(request.session['gold']))
        gold_gained = getRandomNum(5, 10)
        log = "Earned " + str(gold_gained) + " gold from the cave!"
        request.session["gold"] += gold_gained
        request.session['activity1'].append(log)
        print(request.session["activity1"])
        print (str(request.session['gold']))
        return redirect("/")

    if request.POST["which_form"] == "house":
        # print(str(request.session['gold']))
        gold_gained = getRandomNum(2, 5)
        log = "Earned " + str(gold_gained) + " gold from the house!"
        request.session["gold"] += gold_gained
        request.session['activity1'].append(log)
        print(request.session["activity1"])
        print(str(request.session['gold']))
        return redirect("/")

    if request.POST["which_form"] == "casino":
        # print(str(request.session['gold']))
        gold_gained = getRandomNum(-50, 50)
        log = "Earned " + str(gold_gained) + " gold from the casino!"
        request.session["gold"] += gold_gained
        request.session['activity1'].append(log)
        print(request.session["activity1"])
        print(str(request.session['gold']))
        return redirect("/")
    
def destroy(request):
    request.session['gold'] = 0
    request.session['activity1'] = []
    return redirect("/")

def getRandomNum(min, max):
    result = random.randint(min, max)
    return result