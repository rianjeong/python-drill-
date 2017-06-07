from datetime import datetime, time, tzinfo, timedelta

PdxTime = datetime.now()
##PdxTime =  currTime.strftime("%d %b %Y %I:%M:%S %p")
 
print PdxTime

def closingTime(PdxTime):
    NycTime = timedelta(hours=3)+PdxTime
    Londontime = timedelta(hours=7)+PdxTime
    Nyc1 = NycTime.strftime("%H")
    London1=Londontime.strftime("%H")
##    for closingTime in Londontime: 
    if 16 < London1 > 4:
        print Londontime.strftime("%d %b %Y %I:%M:%S %p")
        print "The London location is closed right now"
    else:
        print Londontime.strftime("%d %b %Y %I:%M:%S %p")
        print "london location is open"
    ##    for closingTime in NycTime:
    if 12 > Nyc1 > 24:
        print NycTime.strftime("%d %b %Y %I:%M:%S %p")
        print " The New York city location is closed right now"
    else:
        print NycTime.strftime("%d %b %Y %I:%M:%S %p")
        print "The New York cit location is open"
            


closingTime(PdxTime)

