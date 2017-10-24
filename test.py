import re

fo = open("source.txt","r+")
fi = open("destination.txt","wb")

def myfun(model):
    return "\r\n"+model.group(0)
str = fo.read()
str =  re.sub(r'-'," -",str)
str =  re.sub(r'[A-Z][A-Z]  -',myfun,str)

print str

fi.write(str)
fo.close()
fi.close()

