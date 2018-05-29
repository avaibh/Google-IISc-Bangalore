from math import *
import sys
import json
import urllib.request 
import requests
import hashlib

r_earth = 6371000
latitude = 12.877854 
r_longitude = 77.625501
f_longitude = 77.625501
orig_stdout = sys.stdout
a=1
sum=0
count = 0
for i in range(0,100):
	if count%10==0:
		r_longitude = f_longitude
		latitude = 12.877854 
	count = count +1 
	file_name = str(a)+".txt"
	a += 1
	sys.stdout = open(file_name, "w+")
	j = 0
	k = 0
	sum = 0
	ref = ''
	while(j<10):
		longitude = r_longitude
		while(k<10):			
			#print(latitude,",",longitude,"|",sep="",end="")
			if(sum<100):
				ref = ref+str(latitude)+","+str(longitude)+"|"
			sum = sum + 1
			longitude = longitude + 0.0008993216;
			k = k + 1
			if k==9:
				f_longitude = longitude
		j = j + 1
		k=0
		latitude  = latitude - 0.0008993216;
		# ref =ref + "\n"
	ref  =ref[:-1]
	api_link = "https://roads.googleapis.com/v1/snapToRoads?path="+ref+"&interpolate=true&key=AIzaSyAtyh3XgY8KPHuDygUZfyjL-6SXcGGogw8"
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36'}
	r = requests.get(api_link, headers=headers)
	string = r.text
	placeId_dict = json.loads(string)
	# print(ref)
	# print(string)
	for snappedPoints in placeId_dict['snappedPoints']:
		print(snappedPoints['placeId'],'\n', end="")
	sys.stdout.close()
	sys.stdout=orig_stdout  
