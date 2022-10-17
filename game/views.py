from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request , 'game/index.html')


def game(request):

    total = 0 

    if request.method == 'POST':
        one = request.POST.get('first_checkbox')
        tow = request.POST.get('second_checkbox')
        three = request.POST.get('third_checkbox')
        four = request.POST.get('forth_checkbox')
        five = request.POST.get('fifth_checkbox')

        checkboxes = [one , tow , three , four , five ]
        for checkbox in checkboxes :
            if checkbox is not None :
                total += int(checkbox)
        
        return render(request , 'game/game.html' , {'total' : total})


    return render(request , 'game/game.html' , {'total' : total})


def instructions(request):
    return render(request , 'game/insturctions.html')

