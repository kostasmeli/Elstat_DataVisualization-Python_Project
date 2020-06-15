import urllib.request
file = open("NewUrl.txt","r") # anoigei to arxeio kai to diavazei
urlarray=[] #arxikopoiw ena array
for line in file.readlines():
    urlarray.append(line)  # gia kathe grammh sto arxeio , thn pernaei sto array
for url in range(len(urlarray)):
        urllib.request.urlretrieve(urlarray[url], f"afikseis_kai_mesa_metaforas{url}.xls") #gia kathe url sto array, apothikeuei to arxeio excel
        print(f"file {url} downloaded")
file.close # kleisimo arxeiou