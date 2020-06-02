#import data to csv files
with open("TouristPerYear.csv",mode="w") as TouristsPerYearfile:
    TouristsPerYear_write=csv.writer(TouristsPerYearfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    TouristsPerYear_write.writerow(["years",year])
    TouristsPerYear_write.writerow(["TouristsPerYear",TouristsPerYear])

with open()