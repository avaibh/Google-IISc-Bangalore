from math import *
import sys
import json
import urllib.request 
import requests
#import str

r_earth = 6371000
latitude = 12.877854 
longitude = 77.625501
orig_stdout = sys.stdout
a=1
sum=0
for i in range(0,1):
	file_name = str(a)+".json"
	a += 1
	sys.stdout = open(file_name, "w+")
	j = 0
	k = 0
	ref = ''
	while(j<10):
		while(k<10):	
			k = k + 1
			sum = sum + 1
			longitude = longitude + 0.0008993216;
			#print(latitude,",",longitude,"|",sep="",end="")
			if(sum<100):
				ref = ref+str(latitude)+","+str(longitude)+"|"
		j = j + 1
		k=0
		latitude  = latitude - 0.0008993216;
	ref  =ref[:-1]
	api_link = "https://roads.googleapis.com/v1/snapToRoads?path="+ref+"&interpolate=true&key=AIzaSyAtyh3XgY8KPHuDygUZfyjL-6SXcGGogw8"
	# headers = {'content-type' : 'application/json'}
	# message = {"atribute_a": "value", "atribute_b": "false"}
	# params = {"priority":"normal"}
	# r = requests.post(api_link, params=params, headers=headers, data = json.dumps(message) )
	# data = requests.get(api_link)
	# print(data)
	# with urllib.request.urlopen(api_link) as url:
	# 	data = json.loads(url.read().decode())
	# 	print(data)
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36'}
	r = requests.get(api_link, headers=headers)
	print(r.text)
sys.stdout.close()
sys.stdout=orig_stdout  




	

	