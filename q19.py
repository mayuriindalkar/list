name=["snowball" ,"chewy" ,"bubbles" ,"gruff" ]
animal=["cat" ,"dog" ,"fish" ,"goat" ]
age=["1" ,"2" ,"2" ,"6" ]
a=[]
i=0
while i<len(name):
    a.append(name[i]+animal[i]+age[i])
    i=i+1
print(a)