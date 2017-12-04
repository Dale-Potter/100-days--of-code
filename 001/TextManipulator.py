#TEXT MANIPULTOR 

#Character change function
def CharChange(data,x,y):
	NewData = data.replace(x,y)
	return NewData

#Replace a character with a space function
def Space(data,x):
	NewData = data.split(x)
	String = '' 
	for i in NewData:
		String = String + ' ' + i
	return String

#Request user for what function is needed function
def Input():
	print ("Select what operation is needed:")
	print (" #1 - Text, replace character with another character ")
	print (" #2 - Text, replace character with space ")
	return raw_input('>>')

#Request function for adding how the user wants their data output - For future project
def Output():
	print ('Output data: ')
	print ("	Type 'T' for Text file")
	print ("	Type 'E' for Excel file")
	print ("	Type 'C' for output to console")
	return raw_input('>>')
	
In = Input()

print ('Paste in data')
data = raw_input('>>')

if In == '1':
	InChar = raw_input('What character would you like replacing:  ')
	OutChar = raw_input('What character should replace it:  ')
	NewData = CharChange(data,InChar,OutChar)
			
elif In == '2':
	InChar = raw_input('What character would you like to replace with space:  ')
	NewData = Space(data,InChar)
		
elif In == '3':
	NewData = data 
	
print('-----------------------------------------------------------')
print ('Here is your origional data:')
print (data)
print('-----------------------------------------------------------')
print ('Here is your new data:')
print (NewData)
