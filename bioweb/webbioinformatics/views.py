from django.shortcuts import render
from django.views.generic import FormView


from .forms import SeqDnaRna, ContactForm, ContactUsform
from script import Dnahandl, Rnahandl


# Create your views here.
def index(request):
	return render(request, 'base.html')

def home(request):
	return render(request, 'home.html') 


def contact1(request):
	form= ContactForm(request.POST or None)
	context={
	'form':form,
	}
	return render(request, 'contact.html', context ) 

def contact(request):
	#this one is going to be registrated in db 
	#and displayed 
	title = 'Please fill all fields'
	form = ContactUsform(request.POST or None)
	context = {
	'title':title,
	'form':form,
	}
	url = 'contact.html'
	if form.is_valid():
		#save data 
		form.save()
		full_name = form.cleaned_data.get("full_name")

		context = {
		'form' : form , 
		'full_name' : full_name,
		'title':'Thank You %s, we will get back to you ASAP'%(full_name),
		}
		url = 'contact.html'
		
	return render(request, url, context ) 



def about(request):
	return render(request, 'about.html') 


def query(request):
	return render(request, 'query.html') 


def dnarna(request):
	# title= 'Choose query'
	form = SeqDnaRna(request.POST or None)
	#print form
	context = {
		# 'title':title, 
		"form" : form, 
	}
	
	if form.is_valid():
		if form.cleaned_data.get('Choose_query') == 'DNA':
			dna = form.cleaned_data.get('sequence')
			sequence = Dnahandl(dna)
			option = form.cleaned_data.get('option')
		
			if sequence.dna_is_valid()!= True: 
				error= sequence.dna_is_valid()
				context = {
					# 'title':title, 
					"form" : form, 
					"error" : error
				}

			if sequence.dna_is_valid()==True: 
				query = ''
				problem = ''
				error = ''

				if option == 'GC content':
					query = sequence.gc_content()
				elif option == 'DNA To RNA':
					query = sequence.reverseDnaToRna()
				elif option == 'Reverse Complement':
					query = sequence.reversecomplement()

				elif option == 'RNA To DNA':
					error = 'Sorry this query for RNA sequence'
					
				# elif option == 'RNA To Protein':
				# 	error = 'Sorry this query for RNA sequence'
					

				else: 
					problem='under construction'

				context = {
				'form':form, 
				'sequence':dna[1:], 
				'query' : query,
				'option': option, 
				"error": error, 
				'problem' : problem 
				}
		elif form.cleaned_data.get('Choose_query') == 'RNA':
			rna = form.cleaned_data.get('sequence')
			sequence = Rnahandl(rna)
			option = form.cleaned_data.get('option')
		
			if sequence.rna_is_valid()!= True: 
				error= sequence.rna_is_valid()
				context = {
					# 'title':title, 
					"form":form, 
					"error": error
				}

			if sequence.rna_is_valid()==True: 
				query = ''
				problem = ''
				error = ''

				if option == 'GC content':
					query = sequence.gc_content()
				elif option == 'RNA To DNA':
					query = sequence.reverseRnaToDna()
				elif option == 'Reverse Complement':
					query = sequence.reversecomplement()

				elif option == 'DNA To RNA':
					error = 'Sorry this query for DNA sequence'
					
				# elif option == 'DNA To Protein':
				# 	error = 'Sorry this query for DNA sequence'
					

				else: 
					problem='under construction'

				context = {
				'form':form, 
				'sequence':rna[1:], 
				'query' : query,
				'option': option,
				"error": error, 
				'problem' : problem 
				}

			# problem_rna='sorry this page is under construction'

			# context = {
			# 	'form':form, 
			# 	'sequence':rna[1:], 
			# 	# 'query' : query,
			# 	'option': option, 
			# 	'problem_rna' : problem_rna
			# 	}



	return render(request, 'dnarna.html', context) 


