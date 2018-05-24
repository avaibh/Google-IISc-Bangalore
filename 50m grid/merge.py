import glob

read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

import hashlib
#1
output_file_path = "placeId_unique.txt"
input_file_path = "result.txt"
#2
completed_lines_hash = set()
#3
output_file = open(output_file_path, "w")
#4
for line in open(input_file_path, "r"):
  #5
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  #6
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
#7
output_file.close()

count=0
with open ('placeId_unique.txt','rb') as f:
    for line in f:
        count+=1

print(count)