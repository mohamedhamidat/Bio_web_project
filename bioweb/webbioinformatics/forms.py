from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText
from .models import ContactUs


class SeqDnaRna (forms.Form):
	sequence= forms.CharField(widget=forms.Textarea())
	TITLE_CHOICES = (
    ('GC content', 'GC content'),
    ('DNA To RNA', 'DNA to RNA'),
    ('RNA To DNA', 'RNA to DNA'),
    ('Reverse Complement', 'Reverse Complement'),
    ('DNA To Protein', 'DNA to Protein'),
    ('RNA To Protein', 'RNA to Protein'),
    )
	
	# option= forms.CharField(
	# 	widget= forms.Select(choices=TITLE_CHOICES))
	option = forms.ChoiceField(
			choices=TITLE_CHOICES, 
			initial = 'GC content',
			widget = forms.RadioSelect)
	
	Choose_query = forms.ChoiceField(
		choices=(
			('DNA', 'DNA'),
			('RNA', 'RNA')
			),
		initial = 'DNA',
        widget = forms.RadioSelect,
        # help_text = "Please select DNA or RNA query "
		)

	helper = FormHelper()
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-2'
	helper.field_class = 'col-sm-9'
	helper.add_input(Submit('Run', 'Run >>', css_class='btn btn-primary col-sm-2 col-sm-9 active'))
	helper.layout=Layout (
		# Field('sequence', rows=7), # it works only if you put widget in forms 
		# Field('Choose_query', style='background: #FAFAFA; padding: 10px;'),

		Field('sequence', placeholder= '> ATGC ...Please put a valid DNA sequence as shwon'),
		'Choose_query',
		# Field('option', placeholder= 'choose query'),
		'option',
	
		# ButtonHolder(
  #               Submit('Run', 'Run >>', css_class='btn-primary col-sm-3 active')
  #           )
		
		)
	# helper[1].wrap_together(Div, css_class="col-md-6 col-xs-6")
	#helper['option'].wrap(Div, css_class="col-xs-6 col-md-6 col-sm-8")
	# helper[2].wrap(Div, css_class=" col-xs-12")
	# class SeqDnaRna (forms.Form):
	# sequence= forms.CharField(widget=forms.Textarea())
	# TITLE_CHOICES = (
 #    ('GC content', 'GC content'),
 #    ('Dna To Rna', 'DNA to RNA'),
 #    ('DNA To Protein', 'DNA to Protein'),)
	# option= forms.ChoiceField(
	# 	widget= forms.RadioSelect,
	# 	choices=TITLE_CHOICES)

	# helper = FormHelper()
	# helper.form_method = 'POST'
	# helper.form_class = 'form-horizontal'
	# helper.label_class = 'col-sm-2'
	# helper.field_class = 'col-sm-10'
	# helper.add_input(Submit('Run', 'Run', css_class='btn-primary'))
	# helper.layout=Layout (
	# 	Field('sequence', rows=7), # it works only if you put widget in forms 
	# 	'option'
	# 	)
	# def __init__(self, *args, **kwargs):
	# 	super(SeqDnaRna, self).__init__(*args, **kwargs)
	# 	helper1 = FormHelper()
	# 	helper1.form_tag = False
	# 	helper1.layout = Layout(	        
	# 	        Field('sequence') ) 

	# 	helper2 = FormHelper()
	# 	helper2.add_input(Submit('Run', 'Run', css_class='btn-primary'))
	# 	helper2.form_class = 'form-horizontal'
	# 	helper2.label_class = 'col-sm-2'
	# 	helper2.field_class = 'col-sm-4'
	# 	helper2.form_tag = False
	# 	helper2.disable_csrf = True
	# 	helper2.layout = Layout(
	# 	        Field('option') )



class ContactForm(forms.Form):

	full_name = forms.CharField(required=True)
	email = forms.EmailField()
	message = forms.CharField(label="Message", widget=forms.Textarea())

	# helper = FormHelper()
	# helper.form_method = 'POST'
	# helper.form_class = 'form-horizontal'
	# helper.label_class = 'col-sm-2'
	# helper.field_class = 'col-sm-4'
	# helper.add_input(Submit('send', 'send', css_class='btn-primary'))

	# helper.layout=Layout (
	# 	Field('full_name', css_class='input-sm'),
	# 	Field('email', css_class='input-sm'),
	# 	Div (Field('message', rows=5, css_class = 'col-sx-4', css_id = 'special-fields'))
	# 	)
	
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('send', 'send', css_class='btn-primary'))
		self.helper.label_class = 'col-sm-4'
		self.helper.field_class = 'col-sm-6'
		self.helper.layout=Layout (
		Field('full_name'), 
		Field('email'), 
		Field('message', rows=5, css_class = 'col-sx-6', placeholder ="message")
		)

		# self.helper[0:2].wrap_together(Div, css_class="col-sm-12")
		# self.helper['full_name'].wrap(Field, wrapper_class="col-sx-6")
		# self.helper['email'].wrap(Field, wrapper_class="col-sx-6")


# how dsplay in admin with fields order in admin or views
class ContactUsform(forms.ModelForm): 
	class Meta : 
		model = ContactUs
		fields = ["full_name", "email", "message"] 

	def __init__(self, *args, **kwargs):
		super(ContactUsform, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('send', 'send', css_class='btn-primary'))
		self.helper.label_class = 'col-sm-4'
		self.helper.field_class = 'col-sm-6'
		self.helper.layout=Layout (
		Field('full_name'), 
		Field('email', placeholder ="exemple@exemple.com"), 
		Field('message', rows=5, css_class = 'col-sx-6', placeholder ="message")
		)

