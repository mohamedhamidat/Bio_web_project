import re 

def seq_valid(seq):
	seq=seq.replace('\n', '').replace('\r', '')
	if re.findall(r'^>', seq):
		if not re.findall(r'[^(A,G,T,C,a,g,t,c)]', seq[1:]):
			return True 
		else : 
			return 'it\'s not a valid DNA sequence'
	else:
		return " Please add\'>\' before sequence"
    

def gc_content(base_seq):
	if seq_valid(base_seq)==True: 
		seq_raw=base_seq.split('>')
		# print seq_raw
		seq = seq_raw[1].upper()
		# print seq.count('G')
		return float ((seq.count('G') + seq.count('C'))) / len(seq)
	else: 
		return seq_valid(base_seq)


def main (): 
	gc_content()
	seq_valid()
	
if __name__ == '__main__':
	os.exit(main())


