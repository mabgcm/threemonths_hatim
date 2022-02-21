from datetime import datetime

from hijri_converter import Hijri, Gregorian
rajab = 30 # number of days in rajab
shaban = 29 # number of days in shaban
ramadan = 29 #number of days in ramadan
daily_page = (604 / (rajab + shaban + ramadan)) # total page numbers of quran / total numbers of days

date = datetime.date(datetime.now()) # bring today's date
date = str(date) # converts the date into string
ucaylar = Gregorian(int(date[0:4]), int(date[5:7]), int(date[8:10])).to_hijri() # takes today's date & converts hijri
ucaylar = str(ucaylar) # converts hijri date to string
# int(ucaylar[5:7])  # indexing the month from hijri calendar
# int(ucaylar[8:10]) # indexing the day from hijri calendar
if int(ucaylar[5:7]) == 7:  # month of rajab
    ay = 0
elif int(ucaylar[5:7]) == 8:  # month of shaban
    ay = rajab  # adds the total number of days of rajab to shaban
elif int(ucaylar[5:7]) == 9:  # month of ramadan
    ay = (rajab + shaban)  # adds the total number of days of rajab & shaban to ramadan
gun = int(ucaylar[8:10])  # number of days at the current date



# # Convert a Hijri date to Gregorian
# g = Hijri(1443, 7, 19).to_gregorian()
# print(g)

# # Convert a Gregorian date to Hijri
# h = Gregorian(2022, 2, 20).to_hijri()
# print(h)


gun_cuz = input("Enter the number of pages you've already read: ") # takes the current total number of pages already read
print("Number of pages that must be read today:", ((ay + gun) * 7)) # states the total number of pages that must be read until that date
hatim = (((ay + gun) * daily_page) - int(gun_cuz)) # calculates the difference btw must-be-read and already-read
hatim = int(hatim) #converts to difference to integer

if hatim > 0:
    print("You' must read", hatim, "pages more to complete on time.")
elif hatim < 0:
    print("You've read", -(hatim), 'pages extra.")
