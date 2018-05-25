import hashlib
#1
a= 1
for i in range(0,400):
	Ifile_name = str(a)+".txt"
	Ofile_name ="unique/"+"new_"+str(a)+".txt"
	a += 1
	# sys.stdout = open(file_name, "w+")
	output_file_path = Ofile_name
	input_file_path = Ifile_name
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