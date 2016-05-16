import re 

def seq_valid(seq):
	seq=seq.replace('\n', '').replace('\r', '')
	if re.findall(r'^>', seq):
		if not re.findall(r'[^(A,G,T,C,a,g,t,c)]', seq[1:]):
			return True 
		else : 
			return 'it\'s not a valid DNA sequence'
	else:
		return " Please add \'>\' before sequence"

	
if __name__ == '__main__':
	seq_valid()


# a='AGTAGTCffCCCGGG\nGTTTTG'

# print seq_valid(a)
# b=a.replace('\n', '').replace('\r', '')
# print a 
# print b

# print re.findall(r'[^(A,G,T,C)]', a[1:])