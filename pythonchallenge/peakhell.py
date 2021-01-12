from urllib.request import urlopen
import  pickle

raw = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for line in raw:
    print("".join([k * v for k, v in line]))