def is_leap(year):
    leap = False
    if(year%4==0):
        if(year%400!=0 and year%100==0):
            leap=False
        else:
            leap=True
    else:
        leap=False
    return leap

year = int(input())
