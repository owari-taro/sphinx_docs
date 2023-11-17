import time
class Date:
    def __init__(self,year,month,date):
        self.year=year
        self.month=month
        self.date=date

    @classmethod
    def today(cls):
        _local=time.localtime()
        print(cls)
        return cls(year=_local.tm_year,month=_local.tm_mon,date=_local.tm_mday)
    


print(Date.today().year)