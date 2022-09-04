# ____________________  String Operations ____________________
"""
     - find index
     - negative indexing
     - Bind a string to another variable
     - Slicing
     - Stride
     - len ()
     - Concatenate or Combine strings
     - Replicate the string
     - Back Slash [\]
     - .upper()
     - .replace()
     - .find()

"""
Name= "Michael Jackson "
# find index
print(Name[0])

#negative indexing
print(Name[-1])

#Bind a string to another variable
First_Name = 'Rashad'
Last_Name = ' K'
print(First_Name + Last_Name)
print(First_Name + ' K')

#Slicing
print(Name[0:4])
print(Name[8:12])

#Stride
print(Name[::2])
print(Name[0:5:2])

#len ()
print(len(Name))

#Concatenate or Combine strings
New_Word = Name + " is the best"
print(New_Word)

#Replicate the string
print( 3 * Name)

#Back Slash [\]
print('last line\nnew line')
print('same line but\ttab distance')
print('print \\ back slash')
print(r'print \ using r')

#.upper()
print(Name.upper())

Cap_Name = Name.upper()
print(Cap_Name)

#.replace()
Rep_Name = Name.replace('Michael','Don')
print(Rep_Name)

#.find()
print(Name.find('M'))
print(Name.find('z'))



