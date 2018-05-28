from django.shortcuts import render
import csv
from django.http import HttpResponse
import json
from django.template import loader
from polls.models import Matches, Deliveries
from django.db import transaction, models
from sortedcontainers import SortedList, SortedDict, SortedSet
from collections import OrderedDict

'''All THE FUNCTIONS ARE ARRANGE IN THE LEXICOGRAPHICAL ORDER'''


# print("file reading matches")
# file = '/home/dev/workspace/mysite/ipl/matches.csv'
# matches = csv.DictReader(open(file, newline=''), delimiter=',', quotechar='|')
# match = dict()
# count = 0
# for i in matches:
#     match[count] = i
#     count += 1


# print("file reading deliveries")

# file_del = '/home/dev/workspace/mysite/ipl/deliveries.csv'
# delivery_Reader = csv.DictReader(
#     open(file_del, newline=''), delimiter=',', quotechar='|')
# match_del = dict()
# c = 0
# for i in delivery_Reader:
#     match_del[c] = i
#     c += 1


# with transaction.atomic():
#     print("matches start")
#     for j in match:

#         temp = Matches(toss_decision=match[j]['toss_decision'],
#                     date=match[j]['date'],
#                     umpire2=match[j]['umpire2'],
#                     toss_winner=match[j]['toss_winner'],
#                     match_id=match[j]['id'],
#                     umpire1=match[j]['umpire1'],
#                     player_of_match=match[j]['player_of_match'],
#                     team1=match[j]['team1'],
#                     season=match[j]['season'],
#                     umpire3=match[j]['umpire3'],
#                     win_by_wickets=match[j]['win_by_wickets'],
#                     dl_applied=match[j]['dl_applied'],
#                     team2=match[j]['team2'],
#                     city=match[j]['city'],
#                     win_by_runs=match[j]['win_by_runs'],
#                     winner=match[j]['winner'],
#                     result=match[j]['result'],
#                     venue=match[j]['venue'])
#         temp.save()

#     print("matches end")

#     print("deliveries start")
#     for j in match_del:

#         temp_match_del = Deliveries(is_super_over=match_del[j]['is_super_over'],
#                                     noball_runs=match_del[j]['noball_runs'],
#                                     ball=match_del[j]['ball'],
#                                     bye_runs=match_del[j]['bye_runs'],
#                                     legbye_runs=match_del[j]['legbye_runs'],
#                                     inning=match_del[j]['inning'],
#                                     total_runs=match_del[j]['total_runs'],
#                                     match_id_id=match_del[j]['match_id'],
#                                     penalty_runs=match_del[j]['penalty_runs'],
#                                     extra_runs=match_del[j]['extra_runs'],
#                                     over=match_del[j]['over'],
#                                     fielder=match_del[j]['fielder'],
#                                     batting_team=match_del[j]['batting_team'],
#                                     bowling_team=match_del[j]['bowling_team'],
#                                     dismissal_kind=match_del[j]['dismissal_kind'],
#                                     player_dismissed=match_del[j]['player_dismissed'],
#                                     non_striker=match_del[j]['non_striker'],
#                                     bowler=match_del[j]['bowler'],
#                                     batsman_runs=match_del[j]['batsman_runs'],
#                                     batsman=match_del[j]['batsman'],
#                                     wide_runs=match_del[j]['wide_runs'])
#         temp_match_del.save()
#     print("deliveries end")


# print('end_______________________________')






# view to find the economical bowler
def economicalBowlers(request):

    # query to get the data from database
    requiedDataFromDBByQuery = Deliveries.objects.values('bowler', 'total_runs').filter(
        match_id_id__in=Matches.objects.values_list('match_id', flat=True).filter(season='2015')).order_by('bowler')


    # main logic
    economicalBowlerDictionary = dict()
    for delivery in requiedDataFromDBByQuery:
        if(delivery['bowler'] in economicalBowlerDictionary.keys()):
            economicalBowlerDictionary[delivery['bowler']] = {'runs': economicalBowlerDictionary[delivery['bowler']]['runs']+int(delivery['total_runs']), 'ball': economicalBowlerDictionary[delivery['bowler']]['ball']+1, 'economicity': float("{0:.3f}".format( (
                economicalBowlerDictionary[delivery['bowler']]['runs']+int(delivery['total_runs']))/((economicalBowlerDictionary[delivery['bowler']]['ball']+1)/6)))}
        else:
            economicalBowlerDictionary[delivery['bowler']] = {
                'runs': int(delivery['total_runs']), 'ball': 1, 'economicity': 0}
    

    #making key as value and value as a key
    sortedBowlerDict=SortedDict()
    for i,j in economicalBowlerDictionary.items():
        sortedBowlerDict[j['economicity']]=i


    # dataSet to plot on xaxis or on y axis
    xAxisData = list(sortedBowlerDict.values())
    yAxisData = list(map(float, sortedBowlerDict.keys()))


    #loading template 
    templte = loader.get_template('polls/economicalBowler.html')
    contaxt = {
       'xAxisData' :  xAxisData[0:10],
       'yAxisData' :  yAxisData[0:10]
    }


    return HttpResponse(templte.render(contaxt, request))




# view to find the matches played per year
def matchPlayedPerYear(request):
    matchData = Matches.objects.values('season').annotate(
        count=models.Count('season')).order_by('season')
    xData = matchData.values_list('season', flat=True)
    yData = matchData.values_list('count', flat=True)
    templte = loader.get_template('polls/matchesPlayedPerYear.html')
    contaxt = {
        "xdata": list(map(int, xData)),
        "ydata": list(map(int, yData))
    }

    return HttpResponse(templte.render(contaxt, request))





# view to find the extra runs bowler
def extraRuns(request):

    extraRunByTeamsDictionary = SortedDict()
    teams = Deliveries.objects.values('extra_runs', 'bowling_team').filter(
        match_id_id__in=Matches.objects.values_list('match_id', flat=True).filter(season='2016')).order_by('bowling_team')
    for delivery in teams:
        if(delivery['bowling_team'] in extraRunByTeamsDictionary.keys()):
            extraRunByTeamsDictionary[delivery['bowling_team']
                                      ] = extraRunByTeamsDictionary[delivery['bowling_team']]+int(delivery['extra_runs'])
        else:
            extraRunByTeamsDictionary[delivery['bowling_team']] = int(
                delivery['extra_runs'])

    xData = list(extraRunByTeamsDictionary.keys())
    yData = list(extraRunByTeamsDictionary.values())
    print(xData)
    print(yData)
    templte = loader.get_template('polls/extraRunIn2016.html')
    contaxt = {
        'xdata': xData,
        'ydata': yData
    }

    return HttpResponse(templte.render(contaxt, request))

