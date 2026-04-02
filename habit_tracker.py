import requests
username='prashantkundagol'
token='soierundour'
graphID='graph1'
pixel_endpoint="https://pixe.la/v1/users"
graph_endpoint="https://pixe.la/v1/{username}/graphs/{graphID}"
user_params={
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


# response=requests.post(pixel_endpoint,json=user_params)
# print(response.text)


graph_headers={"X-USER-TOKEN":token}
graph_params={
    "id":"graph1",
    "name":"my graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}
response=requests.post(graph_endpoint, headers=graph_headers, json=graph_params)
print(response.text)
