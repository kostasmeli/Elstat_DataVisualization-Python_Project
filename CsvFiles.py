#import data to csv files
import csv

from ExcelCalc import year, TouristsPerYear, values, countries, transport, TransportArray, trimina

with open("TouristPerYear.csv",mode="w") as TouristsPerYearfile:
    TouristsPerYear_write=csv.writer(TouristsPerYearfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    TouristsPerYear_write.writerow(year)
    TouristsPerYear_write.writerow(TouristsPerYear)

with open("TopCountries.csv",mode="w") as Topcountriesfile:
    Topcountries_write=csv.writer(Topcountriesfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    Topcountries_write.writerow(year)
    Topcountries_write.writerow(countries)
    Topcountries_write.writerow(values)

with open("TouristsPerTransport.csv",mode="w") as TouristsPerTransportfile:
    TouristsPerTransport_write=csv.writer(TouristsPerTransportfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    TouristsPerTransport_write.writerow(year)
    TouristsPerTransport_write.writerow([transport,transport,transport,transport])
    TouristsPerTransport_write.writerow(TransportArray)

with open("TouristsEvery3months.csv",mode="w") as TouristsEvery3monthsfile:
    TouristsEvery3months_write=csv.writer(TouristsEvery3monthsfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    TouristsEvery3months_write.writerow(year)
    TouristsEvery3months_write.writerow(trimina)