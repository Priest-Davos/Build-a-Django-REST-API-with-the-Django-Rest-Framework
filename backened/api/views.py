from django.http import JsonResponse
import json
# Create your views here.

def api_home(request , *args , **kwargs ):
  # print(request) # <WSGIRequest: GET '/api/?user=1'>
  # print(type(request)) # <class 'django.core.handlers.wsgi.WSGIRequest'>
  # print(request.headers)#{'Content-Length': '25', 'Content-Type': 'application/json', 'Host': '127.0.0.1:8000', 'User-Agent': 'python-requests/2.31.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
  # print(request.GET) #<QueryDict: {'user': ['1']}>
  # print(request.user) #AnonymousUser
  data={}
  if request.body:
     # in Django cannt do directly request.jsonn() unlike in Flask so  do json.loads(request.body)
      body=request.body
      # print(type(body)) #<class 'bytes'>
      data=json.loads(body)     
      print(data)#{'query': 'Helloo there'}
      print(data.keys()) #dict_keys(['query'])
      # data['headers']=request.headers # cannt do so chage it to dict
      print(type(request.headers)) #<class 'django.http.request.HttpHeaders'>
      data['headers']=dict(request.headers) # like this
      print(type(data)) #<class 'django.http.request.HttpHeaders'>
      print (data)
  # response={"message": " is the api_home view","msg2": "ok"}
  # return JsonResponse (response )
  return JsonResponse (data )
