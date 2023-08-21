from datetime import datetime
now = datetime.now()
print(now.year,"%02d"%now.month,"%02d" %now.day,sep='-')