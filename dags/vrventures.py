from asyncio.base_tasks import _task_get_stack
from email.policy import default
from venv import create
import requests  #is used for for network communication and fething the url links 
import pandas as pd #pandas is used for data frame to csv transformation 
import json
import datetime
from xmlrpc.client import DateTime
from datetime import timedelta
import psycopg2 
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator  
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator 


def fetch_github_data():
    github_username = "vaibhavtewani"                           #"apache"
    github_repo = "pyspark"                                     #"incubator-streampark"


    api_url2=f"https://api.github.com/repos/{github_username}/{github_repo}/commits" 
    response = requests.get(api_url2)
    data2 =  response.json()
    data1 = data2
    fetch = []
    for i in range(len(data1)):
        date_obj = data1[i]['commit']['author']['date'][0:10]
        time_obj = data1[i]['commit']['author']['date'][11:13]
        today = str(datetime.datetime.today() -datetime.timedelta(hours=5,minutes=30)).split()[0]
        time = str(datetime.datetime.today() - datetime.timedelta(hours=5,minutes=30)).split()[1][0:2]
        print(time_obj , time)
        print(date_obj,today)
        if date_obj == today and time==time_obj:
            a = []
            a = str(data1[i]['sha'])
            a += ','+ data1[i]['commit']['author']['name'] +"," +'commit'+','+  str(i) + ',' +data1[i]['commit']['author']['email'] + ','+ data1[i]['commit']['author']['date']
            fetch.append(a)
        else:
            pass
    
    
    return(fetch)



def pull_xcom_data(ti):
    pulled_data = ti.xcom_pull(key = 'fetched_data', task_id='fetch_github_Data')
    print(pulled_data)
    

default_args = {
    'owner': 'VRVENTURES',
    'retries': 5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(dag_id = 'vrventures',
       default_args = default_args,
       schedule_interval = None,
       start_date = datetime.datetime(2022,9 ,15)
       ) as dag:  # sd = datetime(2022,9,15) but giving an error module object is noot callable

            task1 = PythonOperator(
                task_id = 'fetch_github_Data', #task id and python name should be diffrent 
                python_callable = fetch_github_data
            )   
            
            task2 = PostgresOperator(
            task_id = 'vrventure_db',
            postgres_conn_id = 'vrventures_db',
            sql = """CREATE TABLE IF NOT EXISTS github_activities(sha_id int, 
                                                                    repo_name text, 
                                                                    type int, 
                                                                    activity_id varchar(225) , 
                                                                    author_id varchar(225) ,
                                                                    created_at varchar(225)); """ ,  #here we created a table using the bsaic sql commands 
        
            )

            task1 >> task2


# dataframe = pd.DataFrame(fetch_github_data())
# dataframe = pd
# print(dataframe)

# print(fetch_github_data())
# dataframe = pd.DataFrame(fetch_github_data())

# print(dataframe)









conn = psycopg2.connect(
host = 'host.docker.internal',
database = 'vrventures',
user = 'airflow',
password = 'airflow',
port = 5432 

)
curr = conn.cursor()
insert_script= """INSERT INTO github_activities(
                sha_id , 
                repo_name , 
                type , 
                activity_id , 
                author_id ,
                created_at ) VALUES({},{},{},{},{},{})"""


# x= fetch_github_data()
# print(x)
# print('x[0] = ',x[0])
# y =  x.split(',')
# # print(y)
# # print(x)
# # print(y[0].split(","))

# curr.execute(insert_script , (y[0],y[1],y[2],y[3],y[4],y[5])) 
# curr.execute()
# print(x)
# for i in range(  0,len(x),1 ):
#     print(len(x))
#     print(i)
#     print(x[i])
#     y = tuple(x[i])
#     print(y)
#     curr.execute(insert_script,y)
#     print('insertion_successful') 

curr.close()

# def fetch_commits(self,github_repo_link,github_username):
#     """
#     This function fetches all the commits of a GitHub repository.
#     """
#     self.github_repo_link = github_repo_link,
#     self.github_username = github_username

#     api_url2=f"https://api.github.com/repos/{self.github_username}/{self.github_repo}/commits" 


#     #getting all the commits of the GitHub repository
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
# data1['sha'] 

# # print(data1)

# # print(data)
# # for key , value in data.items():
# #     print('------------------------------------')
# #     print([key, value])
# # table = pt.PrettyTable()
# # for key, value in data1.items():
# #     table.add_row([key, value])
# # print(table)

# # print(table)
# # print(data)
# # print(data)
# # df = pd.DataFrame.from_dict(data, orient='index')
# # print(df)
# # df
# # print(df)
# # dict1 = dict()
# # create_table = MySQLOperator(
# #     task_id = "create_table",
# #     mysql_conn_id = "mysql_db1"
# #     sql = "CREATE TABLE IF NOT EXISTS github_activities(id int, repo_name varchar(225), type int varchar(225), activity_id varchar(225) , author_id varchar(225) , created_at varchar(225) )" 
# #     )

# FETCH = PythonOprator(
#     fetch = []    
#     for i in data1:
#     #  print(" ------------------------------------------------------------------------------------")
#     #  print(i['sha'])
#         fetch += (i['sha']).split(',')
#     #  print('name:', i['name'])
#     #  print('commit:',i['commit']['author'])
#         fetch += [(i['commit']['author']['name'].split(',') , i['commit']['author']['date'],i['commit']['message'])] 
# )
       
#     #  print(i['commit']['message'])
#     #  fetch += (i['commit']['message'])  
#     #  print('protected:',i[ 'protected'])
#     #  print('date:',i[ 'date'])
 
# # print(fetch)


# # for key , value in data1.items():
# #     print('----------------------------------------------------------------')
# #     print(key, "------>>> ",value)

# for key, value in data1.items():
#     if key == 'commit':
#         fetch += [value]
# print(fetch)
 
# is_eligible = PythonOperator (
#     for count, i in enumerate(fetch):
#     # print(i)
#         if count%2 != 0 and count > 0:
#             print('--------------------------')
#             date_object = fetch[count][1][0:10]
#             # print(fetch[count][1][0:10])
#             time_object = fetch[count][1][11:13]
#             today = str(datetime.datetime.today()).split()[0]
#             time = str(datetime.datetime.today()).split()[1][0:2]
#             print(today, time)
#             print(date_object, time_object)
#             if today == date_object and time == time_object:
#                 print('approved')
#             else:
#                 print('Failed')
# )