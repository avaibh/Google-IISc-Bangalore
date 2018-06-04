import sys
import json
import glob
import os
count = 0
orig_stdout = sys.stdout
# read_files = glob.glob("split_placeID/*.txt")
# for f in read_files:
# with open(f, 'r', encoding="utf-8") as myfile:
# 	base=os.path.basename(f)    
# 	basename=os.path.splitext(base)[0]
# 	content = myfile.readlines()
# 	content = [x.strip() for x in content]
# 	for x in content:
# 		count+=1
# 		basename.strip()
# 		x.strip()
# 		sys.stdout = open("total_placeId.txt","a")
# 		print(basename,",",x,sep="")
# 		sys.stdout.close()
# 		sys.stdout = orig_stdout
with open("total_placeId.txt", 'r') as file:
	sorted_data=sorted(file.readlines(), 
					   key=lambda item: int(item.rsplit(',',1)[-1].strip()))
	for x in sorted_data:
		sys.stdout = open("total_placeId_sorted.txt","a")
		if x.rstrip():
			print(x)
		sys.stdout.close()
		sys.stdout = orig_stdout

with open('total_placeId_sorted.txt') as infile, open('total_placeId_output.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line) 
