import sys
import json
import glob
import os

orig_stdout = sys.stdout
# read_files = glob.glob("split_placeID/*.txt")
# for f in read_files:

with open("links.txt", 'r') as myfile:
	content = myfile.readlines()
	content = [x.strip() for x in content]
# count = 1
# file = set(line.strip() for line in open('links.txt'))
flag=0
	# print(x,count)
	# count+=1
with open("test.txt",encoding="utf-8") as id_ref:
	lines = id_ref.readlines()
	lines = [y.strip() for y in lines]
for line in lines:
	# print(line)
	flag+=1
	# line.strip()
	# line=line[:-1]
	# print(line,"\n",sep="", end="")
	for x in content:
		if x == line:
			print(flag,x,"\n",end="")
			filename = "split_placeID/"+ line + ".txt"
			sys.stdout = open(filename,"a")
			print(flag,"\n",end="",sep="")
			sys.stdout.close()
			sys.stdout = orig_stdout
			# filename = 
			sys.stdout = open("n/line.txt","a")
			print(line,"\n",end="",sep="")
			sys.stdout.close()
			sys.stdout = orig_stdout
			x = content[0]
				

