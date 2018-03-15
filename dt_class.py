import datetime

class W_data:

    def now(self):
        ''' Zwraca obecny czas  '''
        return datetime.datetime.now(),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")   # datetime object , string
    def teraz_godz(self):
        ''' Zwraca obecna godzine'''
        return datetime.datetime.now().time(),datetime.datetime.now().time().strftime("%H:%M:%S")   # datetime object , string
    def teraz_data(self):
        ''' Zwraca obecna date'''
        return datetime.datetime.now().date(),datetime.datetime.now().date().strftime("%Y-%m-%d")   # datetime object , string
    def data_z_string(self,in_string=str):
        ''' Konwertuje date i godzine z typu string i zwraca jako datetime object i string'''
        try:
            return datetime.datetime.strptime(str(in_string), '%b %d %Y %H:%M:%S'),datetime.datetime.strptime(str(in_string), '%b %d %Y %H:%M:%S').strftime("%Y-%m-%d %H:%M:%S")  # datetime object , string
        except:
            print 'Input format example: Jun 1 2005  1:33:02'
    def data_z_string_data(self,in_string=str):
        ''' Konwertuje date z typu string i zwraca jako datetime object i string'''
        try:
            return datetime.datetime.strptime(str(in_string), '%b %d %Y').date(),datetime.datetime.strptime(str(in_string), '%b %d %Y').date().strftime("%Y-%m-%d") # datetime object , string
        except:
            print 'Input format example: Jun 1 2005'

    def data_z_string_godz(self,in_string=str):
        ''' Konwertuje godzine z typu string i zwraca jako datetime time object i string'''
        try:
            return datetime.datetime.strptime(str(in_string), '%H:%M:%S').time(),datetime.datetime.strptime(str(in_string), '%H:%M:%S').time().strftime("%H:%M:%S") # datetime object , string
        except:
            print 'Input format example: 13:33:00'

    def tdelta_f_string(self,start=str,end=str):  # timedelta from string
        ''' Oblicza roznice czasu z typu string i zwraca jako datetime object i roznice w sekundach'''
        from datetime import timedelta

        try:
            s=datetime.datetime.strptime(str(start), '%b %d %Y %H:%M:%S')
            e=datetime.datetime.strptime(str(end), '%b %d %Y %H:%M:%S')
            return e-s,timedelta.total_seconds(e-s)                         # difference, in seconds

        except:
            print 'Input format example: Jun 1 2005  1:33:02,Jun 2 2005  13:33:03'

    def tdelta_f_dt(self,start=datetime.datetime,end=datetime.datetime):  # timedelta from datetime
        ''' Oblicza roznice czasu z typu datetime i zwraca jako datetime object i roznice w sekundach'''
        from datetime import timedelta

        try:
            return end-start,timedelta.total_seconds(end-start)                         # difference, in seconds

        except:
            print 'Input format example: Jun 1 2005  1:33:02,Jun 2 2005  13:33:03'

    def date_separated(self):       # separated datetime
        ''' Zwraca obecna date i godzine i zwraca w postaci rozbitej jako datetime object'''
        now = datetime.datetime.now()
        return now.hour,now.minute,now.second,now.microsecond,'--',now.day,now.month,now.year

    def time_in_range(start, end, x):
        ''' Sprawdza czy zadana data (x) miesci sie w przedziale czasowym (start, end) '''
        if start <= end:
            return start <= x <= end
        else:
            return start <= x or x <= end

    def dt_to_ts(self,to_timestamp=datetime):             # datetime to timestamp
        ''' converts datetime object to unix timestamp '''
        import time
        v= datetime.date(to_timestamp.year,to_timestamp.month,to_timestamp.day)
        if not to_timestamp.time():
            return time.mktime(v.timetuple())
        else:
            w=datetime.time(to_timestamp.hour,to_timestamp.minute,to_timestamp.second)
            t= datetime.datetime.combine(v,w)
            return time.mktime(t.timetuple())

    def ts_to_dt(self,to_datetime=datetime):             # timestamp to datetime and string
        ''' converts unix timestamp to datetime object to unix timestamp '''
        return datetime.datetime.fromtimestamp(int(to_datetime)), datetime.datetime.fromtimestamp(int(to_datetime)).strftime('%Y-%m-%d %H:%M:%S')


## example

d=W_data()
x= d.dt_to_ts(d.now()[0])
print type(d.ts_to_dt(x)[0]),d.ts_to_dt(x)[0],x




##d=W_data()
##print d.teraz()[0],d.teraz()[1]
##print d.teraz_godz()[0],d.teraz_godz()[1]
##print d.teraz_data()[0],d.teraz_data()[1]
##print d.data_z_string('Jun 1 2005  1:33:00')[0],d.data_z_string('Jun 1 2005  1:33:00')[1]
##print d.data_z_string_data('Jun 1 2005')[0],d.data_z_string_data('Jun 1 2005')[1]
##print d.data_z_string_godz('13:33:00')[0],d.data_z_string_godz('13:33:00')[1]
##
##help(d.data_z_string)
##
###print dir(d)
##
##
##print d.tdelta_f_string('Jun 1 2005  13:33:00','Jun 1 2005  13:34:01')[0],d.tdelta_f_string('Jun 1 2005  13:33:00','Jun 1 2005  13:34:01')[1]
##
##print d.date_separated()