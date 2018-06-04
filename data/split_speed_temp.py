import sys
import json
import glob
import os

orig_stdout = sys.stdout
# read_files = glob.glob("split_placeID/*.txt")
# for f in read_files:
with open("total_placeId_output.txt", 'r', encoding="utf-8") as myfile:
	# base=os.path.basename(f)    
	# basename=os.path.splitext(base)[0]
	content = myfile.readlines()
	content = [x.strip() for x in content]
	# for x in content:
myfile.close()
flag=0
with open("filename_currentSpeeds.txt",encoding="utf-8") as speed_ref:
	for line in speed_ref:
		print(line)
		print(line[:-1],line[:-2],"\n","\n")
		flag+=1
		# line.strip()
		if flag>90324:
			i=0
			while len(content)>0:			
			# for x in content:
				# temp = x.rsplit(',',1)
				# print(temp)
				# print(num, basename, basename[:-1], basename[:-2],"\n")
				x = content[0]
				num = int(x.rsplit(',',1)[-1].strip())
				print(x, num)
				if flag == num:
					basename = x.rsplit(',',1)[0].strip()
					line = line[:-1]
					print(num, basename,flag,line,"\n",end="")	
					filename = "split_speed/"+ basename + ".txt"
					# print(filename,"\n")
					sys.stdout = open(filename,"a")
					print(line,"\n",end="",sep="")
					sys.stdout.close()
					sys.stdout = orig_stdout
					del basename
					del content[0]
				elif flag > num:
					del content[0]
					continue
				else:
					break