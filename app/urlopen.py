from urllib import urlopen

cont = urlopen("http://localhost:3000").readlines()
print cont