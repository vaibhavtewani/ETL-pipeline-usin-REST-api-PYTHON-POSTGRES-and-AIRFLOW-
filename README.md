what i'll be doing in the projects given to me 
this project of ETL process taught me a whole lot of new thing i was lagging and broke my overconfidence as well . although i tried my best 
major challenges were :
0).pandas could'nt read csv files on vscode and using anaconda prompt would result in ipynb format instead of .py file which is what actually          airflow needs during the execution of dags so have to drop that thing 
1).selecting a proper github api request amoungst the ton of similar resulting api's 
2).runnng airflow on my machine litreally took 35+ hours of thinking what's happening and what will work eventually
3).shifting on to a new machine atlast was difficult but still was a better dicision 
4).apache's xcom was not that handy (not designed to handle big data and even small data even 48kb i think is the limit )so have to switched up for
5).request for an api from a machine was reached so i could'nt run it/fetch it anymore , the solution to this problem can be using pyspark's            dataframe as they were immutable , but i was'nt allowed to use that so..
6).connectivity of SQL(postgres) with python in my case was difficult as  i was using debeaver and the airflow's connection part need to be regularized in regular intervals 
7).for REST api of fetched commit request i've used flask



![Capture_connection_list](https://user-images.githubusercontent.com/111138949/190877872-51a62b00-8397-4aad-b5fb-21a67e34a442.PNG)
![Capture_dag_log_for_vrventues_db](https://user-images.githubusercontent.com/111138949/190877893-2cfd2d6b-ae0b-480e-9397-1243395075ea.PNG)
![Capture_logs_of_pyhton operator_or_trimmed _or_fetched_data](https://user-images.githubusercontent.com/111138949/190877910-8ce9efe8-735d-4b77-8c86-04bd51361b28.PNG)

![Capture_dags](https://user-images.githubusercontent.com/111138949/190877898-98dde1b2-aa91-4fcd-91b6-ed7fabb45dd8.PNG)
![Capture_docker](https://user-images.githubusercontent.com/111138949/190877904-2d28aa32-5c90-4385-be50-7de44ed4e17d.PNG)
![Capture_graph](https://user-images.githubusercontent.com/111138949/190877906-efe36088-5046-4218-9148-184b3bad8f9e.PNG)


![Capture](https://user-images.githubusercontent.com/111138949/190877853-911b8795-5ade-4d4d-876b-8f6d3b15348e.PNG)
![Capture](https://user-images.githubusercontent.com/111138949/190877863-4e17ae92-7248-4147-a382-59334b4145cb.PNG)
