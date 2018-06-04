# basename="20180132-235014"
# print(basename[-2:])
import xlwt

read_files = glob.glob("split_speed/*.txt")
for file in read_files:
    base=os.path.basename(file)
    basename=os.path.splitext(base)[0]
    sheet_name = basename+".xls"
    workbook = xlwt.Workbook(encoding="utf-8")
    sheet1 = workbook.add_sheet("Sheet1")
    for line in file:
        date = int(line[6:][:2]) ##change basename to line
        # print(date)
        time=basename[9:][:6]
        temp = 0
        i=0
        j=0
        while temp<=31:
            temp+=1
            if temp == date:
                i = date
                # print(i)
        time_n = int(time[:2])
        time_compare = int(time[2:])
        if 0<=time_compare and time_compare<1500:
            j = 4*time_n + 1
        elif 1500<=time_compare and time_compare<3000:
            j = 4*time_n + 2
        elif 3000<=time_compare and time_compare<4500:
            j = 4*time_n + 3
        else:
            j = 4*time_n + 4
        # print(j)
        speed_data = line[-2:] ##check for the data once
        sheet1.write(i,j,speed_data)
    workbook.save(sheet_name)