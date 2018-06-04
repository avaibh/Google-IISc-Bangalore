import sys
import json
import glob
import os

orig_stdout = sys.stdout
# read_files = glob.glob("split_placeID/*.txt")
# for f in read_files:
with open("total_placeId.txt", 'r', encoding="utf-8") as myfile:
	base=os.path.basename(f)    
	basename=os.path.splitext(base)[0]
	content = myfile.readlines()
	content = [x.strip() for x in content]
	for x in content:
		flag=0
		with open("filename_currentSpeeds.txt",encoding="utf-8") as speed_ref:
			for line in speed_ref:
				flag+=1
				line.strip()
				if flag == int(x):
					line = line[:-1]
					print(flag,line,"\n",end="")	
					filename = "split_speed/"+ basename + ".txt"
					sys.stdout = open(filename,"a")
					print(line,"\n",end="",sep="")
					sys.stdout.close()
					sys.stdout = orig_stdout
					break
	del x
	sys.stdout = open("file_completed.txt", "a")
	print(basename)
	sys.stdout.close()
	sys.stdout=orig_stdout
	del basename
			

