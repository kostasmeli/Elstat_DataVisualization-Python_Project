import urllib.request
file = open("NewUrl.txt","r")
urlarray=[]
for line in file.readlines():
    urlarray.append(line)
for url in range(len(urlarray)):
        urllib.request.urlretrieve(urlarray[url], f"afikseis_kai_mesa_metaforas{url}.xls")
        print(f"file {url} downloaded")
file.close