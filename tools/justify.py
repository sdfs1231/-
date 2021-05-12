from _Database import _Database
from datetime import datetime
from datetime import timedelta

if __name__=="__main__":
    d1 = datetime.now();
    d2 = d1 + timedelta(hours =-1);
    print(d1,d2)
    print((d2-d1).seconds)
    pass;
