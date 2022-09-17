# from asyncio.base_tasks import _task_get_stack
# from email.policy import default
# from venv import create
# from xmlrpc.client import DateTime
# import requests  #is used for for network communication and fething the url links 
# import pandas as pd #pandas is used for data frame to csv transformation 
# import json
# import datetime 

# # df =  pd.read_excel('C:\input_repo.xlsx')        # vs code could'nt read the file 
# # df
# github_username = "vaibhavtewani"                           #"apache"
# github_repo = "pyspark"                                     #"incubator-streampark"


# api_url2=f"https://api.github.com/repos/{github_username}/{github_repo}/commits" 
# response = requests.get(api_url2)
# data1 =  response.json()

# # print(data1['commit']['author']['date'].split()[0:10])
# print(data1)

# fetch = []
# for i in range(len(data1)):
#     date_obj = data1[i]['commit']['author']['date'][0:10]
#     time_obj = data1[i]['commit']['author']['date'][11:13]
#     today = str(datetime.datetime.today() -datetime.timedelta(hours=5,minutes=30)).split()[0]
#     time = str(datetime.datetime.today() - datetime.timedelta(hours=5,minutes=30)).split()[1][0:2]
#     print(time_obj , time)
#     print(date_obj,today)
#     if date_obj == today and time==time_obj:
#         a = []
#         a = str(data1[i]['sha'])
#         a += ','+ data1[i]['commit']['author']['name'] +"," +'commit'+','+  str(i) + ',' +data1[i]['commit']['author']['email'] + ','+ data1[i]['commit']['author']['date']
#         fetch.append([a])
# print(fetch)

# for i in data1:
#     print(" ------------------------------------------------------------------------------------")
#     date_obj = i['commit']['author']['date'][0:10]
#     time_obj = i['commit']['author']['date'][11:13]
#     today = str(datetime.datetime.today() -datetime.timedelta(hours=5,minutes=30)).split()[0]
#     time = str(datetime.datetime.today() - datetime.timedelta(hours=5,minutes=30)).split()[1][0:2]
#     print(time_obj , time)
#     print(date_obj,today)
#     if date_obj == today and time==time_obj:
#         fetch.append(i)



# list = [['commit',['name'],'new_name'],['author','author_senior'],['name','with']]
# print(list[0][2])