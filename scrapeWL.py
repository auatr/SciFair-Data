import urllib.request
for i in range (56,57):
    opener = urllib.request.build_opener()
    url = f"https://lanier.uslakes.info/Level.asp"
    f = opener.open(url)
    content = f.read()
    G =  open(f"data/{i}.txt", "a")
    G.write(content)
    lines = G.readlines()
    del lines[0]
    del lines[1]
    lines = [f"19{i} " + line for line in lines]
    G.close()