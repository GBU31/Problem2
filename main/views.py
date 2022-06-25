from django.shortcuts import render
import pandas as pd
from .models import *


def player(request):
    t1.objects.all().delete()
    t2.objects.all().delete()

    # Define a dictionary containing player data
    data1 = {'Name':['Player_A', 'Player_B'], 'Height':['103', '100'], 'weight':['219', '216']}
    data2 = {'Name':['Player_A', 'Player_A'], 'game_no':['game_1', 'game_2'], 'Activity_1':['3', '4'], 'Activity_2':['86', '85'], 'Activity_3':['94', '93'], 'year':['2093', '2097'], 'Narrative':['Exceled in boxing Championed in Worlds Championship', 'Exceled in boxing Championed in Worlds Championship']}

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
        game = request.POST['game']
        try:
            return render(request, 'player.html', {'t1':t1.objects.get(name=name), 't2':t2.objects.get(name=name, game_no=game)})
        except:
            return render(request, 'player.html', {'msg':'Player not found'})


    return render(request, 'player.html')
