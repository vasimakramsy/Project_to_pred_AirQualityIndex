import os
import time
import requests
import sys


def scrap_htmldata():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10):
                url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            else:
                url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            text=requests.get(url)
            text_utf=text.text.encode('utf=8')
            
            if not os.path.exists("Data/Html_RAW_Data/{}".format(year)):
                os.makedirs("Data/Html_RAW_Data/{}".format(year))
            with open("Data/Html_RAW_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
        
if __name__=="__main__":
    start_time=time.time()
    scrap_htmldata()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))
        
    
