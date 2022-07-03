from cv2 import DescriptorMatcher_BRUTEFORCE_SL2
from django.shortcuts import render
import pandas as pd
from .models import *


def player(request):
    t1.objects.all().delete()
    t2.objects.all().delete()
    

    # Define a dictionary containing player data
    global data1
    data1 = {'Name':['Player_A', 'Player_B'], 'Height':['103', '100'], 'weight':['219', '216']}
    data2 = {'Name':['Player_A', 'Player_A', 'Player_B'], 'game_no':['game_1', 'game_2', 'game_1'], 'Activity_1':['3', '4', '18'], 'Activity_2':['86', '85', '99'], 'Activity_3':['94', '93', '155'], 'year':['2093', '2097', '2022'], 'Narrative':['Exceled in boxing Championed in Worlds Championship', 'Exceled in boxing Championed in Worlds Championship', 'Exceled in boxing Championed in Worlds Championship']}
    
    df = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    
    

    for i in range(len(df['Name'])):
        # adding t1 
        t1.objects.create(name = df['Name'][i], height = df['Height'][i], weight = df['weight'][i])

        
    for i in range(len(df2['Name'])):
        # adding t2 
        t2.objects.create(name = df2['Name'][i], game_no = df2['game_no'][i], activity_1 = df2['Activity_1'][i], activity_2 = df2['Activity_2'][i], activity_3 = df2['Activity_3'][i], year= df2['year'][i], narrative = df2['Narrative'][i])

    
    # search for the Player Name e.g. Player_A
    if request.method == 'POST':
        name = request.POST['name']
        if t1.objects.filter(name=name):
            return render(request, 'player.html', {'name':name,'t1':t1.objects.filter(name=name), 'df':df,'t2':t2.objects.filter(name=name)})

        else:
            return render(request, 'player.html', {'msg':'Player or Game is incorrect'})


    return render(request, 'player.html')


def game(request, pk):
    return render(request, 'game.html', {'t2':t2.objects.filter(pk=pk)})
    
    
    
    
