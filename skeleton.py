# this is the skeleton python code.

# Soma
def getFirstWord(string):
	# Write the code here
   word_list = (string.split())
   return word_list[0]	


# Avantika
def getLastWord(string):
   word_list = str.split()
   return word_list[-1]
	


# Paddy
def getNumWords(string):
	# Write code here
	return(len(string.split()))


def swapCase(string):
    return(str.swapcase())

def exptWork(string):
    return('This is expt ' + string)


str = 'The Good The Bad and The Ugly'
print(str)
print(getFirstWord(str))
print(getLastWord(str))
print(getNumWords(str))
print(swapCase(str))
print(exptWork(str))

str = 'The Shawshank Redumption'
print(str)
print(getFirstWord(str))
print(getLastWord(str))
print(getNumWords(str))
print(swapCase(str))
print(exptWork(str))



