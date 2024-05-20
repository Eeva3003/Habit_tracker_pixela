import requests
from datetime import datetime
USERNAME=#upload your username
TOKEN="fiykgkyftjgvjk"
GRAPH_ID="graph1"
#create your user id
pixela_end_Point="https://pixe.la/v1/users"
parameters={
    "token":TOKEN,
    "username":USERNAME,
"agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response = requests.post(url=pixela_end_Point,json=parameters)
#print(response.text)
#create your own graph
graph_end=f"{pixela_end_Point}/{USERNAME}/graphs"
graph_para={
    "id": GRAPH_ID,
        "name":"water intake",
"unit":"l",
"type":"float",
"color":"sora",
}
headers={
    "X-USER-TOKEN":TOKEN
}
#update pixel day by day
response_graph=requests.post(url=graph_end,json=graph_para,headers=headers)
#print(response_graph.text)
today=datetime.now()
#print(today.strftime("%Y%m%d"))
pixel_end=f"{pixela_end_Point}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_para={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many litres of water did you drink "),
}
#response_pixel=requests.post(url=pixel_end,json=pixel_para,headers=headers)
#print(response_pixel.text)

update_end=f"{pixela_end_Point}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data={"quantity":"1.5"}

response_update=requests.put(url=update_end,json=new_pixel_data,headers=headers)
#print(response_update.text)
delete_endpoint=f"{pixela_end_Point}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response_delete=requests.delete(url=delete_endpoint,headers=headers)
