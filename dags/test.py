from asyncio.base_tasks import _task_get_stack
from email.policy import default
from venv import create
from xmlrpc.client import DateTime
import requests  #is used for for network communication and fething the url links 
import pandas as pd #pandas is used for data frame to csv transformation 
import json
import datetime 

# df =  pd.read_excel('C:\input_repo.xlsx')        # vs code could'nt read the file 
# df
github_username = "vaibhavtewani"                           #"apache"
github_repo = "pyspark"                                     #"incubator-streampark"


api_url2=f"https://api.github.com/repos/{github_username}/{github_repo}/commits" 
response = requests.get(api_url2)
data1 =  response.json()

# print(data1)

fetch = []
for i in data1:
    print(" ------------------------------------------------------------------------------------")
    date_obj = i['commit']['author']['date'][0:10]
    time_obj = ['commit']['author']['date'][11:13]
    today = str(datetime.datetime.today() -datetime.timedelta(hours=5,minutes=30)).split()[0]
    time = str(datetime.datetime.today() - datetime.timedelta(hours=5,minutes=30)).split()[1][0:2]
    print(i['sha'])
    fetch += (i['sha']).split(',')
    print('name:', i['commit']['author']['name'])
    print('commit:',i['commit']['author'])
    print('commit message:', i['commit']['message'])
    fetch += i['commit']['author']['name'].split(',') + i['commit']['author']['date'].split(',')+i['commit']['message'].split(',') 
print(fetch)
final_fetch = []
for count, i in enumerate(fetch ):
    if count%2 != 0 and count > 0:
        print('--------------------------')
        date_object = fetch[count][1][0:10]
        # print(fetch[count][1][0:10])
        time_object = fetch[count][1][11:13]
        today = str(datetime.datetime.today() -datetime.timedelta(hours=5,minutes=30)).split()[0]
        time = str(datetime.datetime.today() - datetime.timedelta(hours=5,minutes=30)).split()[1][0:2]
        # print(today, time, datetime.datetime.today())
        # print(date_object, time_object)
        if today == date_object and time == time_object:
            final_fetch += fetch[count -1].split(',')
            final_fetch += i
            # print('added a row in a final_fetch')
        else:
            pass
























































































#    #getting all the commits of the GitHub repository
# # github_repo_link = "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}"
# github_username = "vaibhavtewani"#"apache"
# github_repo = "pyspark"  #"incubator-streampark"
# #api url to grab public user data
# # api_url = f"https://api.github.com/repos/{github_username}/{github_repo}/stats/punch_card"
# # api_url1= f'https://api.github.com/repos/{github_username}/{github_repo}/branches'  
# api_url2=f"https://api.github.com/repos/{github_username}/{github_repo}/commits" 
# #send get request
# response = requests.get(api_url2)
# #get the data in json or equivalent dict format
# data1 =  response.json()
# # data1['sha'] 
