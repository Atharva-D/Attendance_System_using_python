# -*- coding: utf-8 -*-

from datetime import datetime

def Mark_Attendance (name):
    with open ('attendance.csv','r+') as f:
        dataList= f.readlines()
        nameList=[]
        for line in dataList:
            entry = line.split(',')
            nameList.append(entry[0])
            d_t = datetime.now()
            date = d_t.strftime('%d.%m.%Y')
            time = d_t.strftime('%H:%M:%S')
            attendance = [name,date,time]
            if(attendance not in f):
                f.writelines("\n")
                f.writelines((",").join(attendance))
                break
        
        

