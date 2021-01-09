from datetime import datetime 
todays_date = datetime.now()
x = todays_date.second
print(x)
if (x%2==0):
    print("even")
else:
    print("odd")
    
