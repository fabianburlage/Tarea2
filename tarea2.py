import re
import yaml
import os 

io = open('/Users/macbookpro/Desktop/data.txt', 'r')

texto = io.read()
correos = re.findall('\S+@\S+', texto)
io.close()

print("Cantidad de correos", len(correos))


print(correos)