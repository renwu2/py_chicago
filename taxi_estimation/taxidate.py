def getcount(file):
    with open (file,encoding='utf-8',newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            yield row

counter=np.zeros((14,24,5,5),dtype=int)
i=0
for row in getcount('C:/Users/WURen/Downloads/Taxi_Trips.csv'):
        i+=1
        if i%(10**6)==0:
            print(i)
        if row[8] !='' and row[9]!='':
            pick_up = int(row[8])
            drop_off = int(row[9])
            try:
                str_datetime = datetime.strptime(row[2], '%m/%d/%Y %H:%M').strftime('%Y,%m,%d,%H,%M')
                [year,month,day,hours,minutes]=map(int, re.findall(r'\d+', str_datetime))
            except:
                str_datetime = datetime.strptime(row[2], '%m/%d/%Y %I:%M:%S %p').strftime('%Y,%m,%d,%H,%M')
                [year,month,day,hours,minutes]=map(int, re.findall(r'\d+', str_datetime))
            if year==2013 and month==4 and day<15 and f(pick_up)>=0 and f(pick_up)<5 and f(drop_off)>=0 and f(drop_off)<5:
                counter[day-1,hours,f(pick_up),f(drop_off)] +=1
            else:
                continue

