import datetime

def __inner_time_change(base_time, time_delta_days, time_delta_seconds, future_or_not):
    if future_or_not:
        return base_time + datetime.timedelta(time_delta_days, time_delta_seconds)
    else:
        return base_time - datetime.timedelta(time_delta_days, time_delta_seconds)

def __outer_time_change(date1,time1,days2,time2,operator):
    o = False
    date1 = date1.split('-')
    time1 = time1.split(':')
    time2 = time2.split(':')
    base_time = datetime.datetime(int(date1[0]),int(date1[1]),int(date1[2]),int(time1[0]),int(time1[1]),int(time1[2]))
    if operator == '+':
        o = True
    elif operator == '-':
        o = False
    new_time = __inner_time_change(base_time,int(days2),int(time2[0])*60*60+int(time2[1])*60+int(time1[2]),o)
    return str(new_time)

def time_change(t1,t2,o):
    t1 = t1.split(' ')
    t2 = t2.split(' ')
    return __outer_time_change(t1[0],t1[1],t2[0],t2[1],o)

