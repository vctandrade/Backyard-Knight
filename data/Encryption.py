
defaultKey = 'f0ajUisj-1892*#(@naidaiSIAM2'

def encrypt(string, key=defaultKey):
	i = 0
	pString = [ord(c) for c in list(string)]
	
	for c in range(len(pString)):
		pString[c] += ord(key[i])
		
		i += 1
		if i >= len(key): i = 0
		
	result = [chr(c % 256) for c in pString]
	return ''.join(result)

def decrypt(string, key=defaultKey):
	i = 0
	pString = [ord(c) for c in list(string)]
	
	for c in range(len(pString)):
		pString[c] -= ord(key[i])
		
		i += 1
		if i >= len(key): i = 0
		
	result = [chr(c % 256) for c in pString]
	return ''.join(result)
