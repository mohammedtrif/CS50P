
months = {"January": 1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October": 10,
    "November":11,
    "December":12,

}

while True :
    try :
        date = input("Date: ")
        if "/" in date :
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if 0 < day < 32 and 0 < month < 13 :
                print(f"{year}-{month:02d}-{day:02d}")
                break
            else : pass
        if "," in date  :
            month_day, year = date.split(",")
            month, day = month_day.split(" ")
            day = int(day)
            year = int(year)
            if 0 < day < 32 and month in months :
                print(f"{year}-{months[month]:02d}-{day:02d}")
                break
            else: pass

    except ValueError :
        pass