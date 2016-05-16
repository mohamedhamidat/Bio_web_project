import re

class Dnahandl () :
	""" this class is going to perfrmor basic  
	bioinformatics task """

	def __init__(self, dna):
		self.dna = dna


	def dna_is_valid(self):

		self.dna=self.dna.replace('\n', '').replace('\r', '')
		if re.findall(r'^>', self.dna):
			if not re.findall(r'[^(A,G,T,C,a,g,t,c)]', self.dna[1:]):
				return True 
			else : 
				return 'Please put valid DNA sequence (ATGC)'
		else:
			return " Please add \'>\' before sequence"

	def gc_content(self):
		if self.dna_is_valid()==True: 
			seq_raw=self.dna.split('>')
			# print seq_raw
			seq = seq_raw[1].upper()
			# print seq.count('G')
			gc = float ((seq.count('G') + seq.count('C'))) / len(seq)
			return "%.2f" % gc
		else: 
			return self.dna_is_valid()

	def reverseDnaToRna(self):
		"""reverse complement""" 
		if self.dna_is_valid()==True:
			seq_raw=self.dna.split('>')
			# print seq_raw
			dna = seq_raw[1].upper()
			rna = dna.replace('T', 'U')#[::-1]
			return rna

		else: 
			return self.dna_is_valid()

	def reversecomplement(self):
		seq_rev=''
		basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
		if self.dna_is_valid()==True:
			seq_raw=self.dna.split('>')
			seq = seq_raw[1].upper()
			word=[basecomplement[i] for i in seq.strip()]
			word.reverse()
			seq_rev=''.join(word)
		else :
			seq_rev= self.dna_is_valid()
		return seq_rev

# d =">aaggggttttcc"
# se = Dnahandl(d)
# print se.reversecomplement()

class Rnahandl () :
	""" this class is going to perfrmor basic  
	bioinformatics task """

	def __init__(self, rna):
		self.rna = rna


	def rna_is_valid(self):

		self.rna=self.rna.replace('\n', '').replace('\r', '')
		if re.findall(r'^>', self.rna):
			if not re.findall(r'[^(A,G,U,C,a,g,u,c)]', self.rna[1:]):
				return True 
			else : 
				return 'Please put valid RNA sequence (AUGC)'
		else:
			return " Please add \'>\' before sequence"

	def gc_content(self):
		if self.rna_is_valid()==True: 
			seq_raw=self.rna.split('>')
			# print seq_raw
			seq = seq_raw[1].upper()
			# print seq.count('G')
			gc = float ((seq.count('G') + seq.count('C'))) / len(seq)
			return "%.2f" % gc
		else: 
			return self.rna_is_valid()

	def reverseRnaToDna(self):
		"""reverse complement""" 
		if self.rna_is_valid()==True:
			seq_raw=self.rna.split('>')
			# print seq_raw
			rna = seq_raw[1].upper()
			dna = rna.replace('U', 'T')#[::-1]
			return dna

		else: 
			return self.rna_is_valid()

	def reversecomplement(self):
		seq_rev =''
		basecomplement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
		if self.rna_is_valid()==True:
			seq_raw=self.rna.split('>')
			seq = seq_raw[1].upper()
			word=[basecomplement[i] for i in seq.strip()]
			word.reverse()
			seq_rev=''.join(word)
		else :
			seq_rev= self.rna_is_valid()
		return seq_rev

# d =">aaggggucc"
# se = Rnahandl(d)
# print se.reversecomplement()
# print se.rna_is_valid()
# print se.gc_content()
# print se.reverseRnaToDna()

