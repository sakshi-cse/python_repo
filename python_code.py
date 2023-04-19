year = 2000
m = 2
 if m > 12:
     print("retry")
 else:
     if m == 2:
         if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
             d = 29
         else:
             d = 28
     elif m in [4, 6, 9, 11]:
         d = 30
     else:
         d = 31
     print("No. of days :", d)
