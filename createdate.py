from datetime import datetime
strftime = datetime.strftime

class PublishDate:
    dd: int
    mm: int
    yyyy: int

    def __init__(self,dd,mm,yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    def __str__(self):
        return strftime(datetime(self.yyyy,self.mm,self.dd),'%d%b%Y')
    
    def get_date(self):
        return strftime(datetime(self.yyyy,self.mm,self.dd),'%d%b%Y')


if __name__=='__main__':
   print(PublishDate(12,5,2025))
