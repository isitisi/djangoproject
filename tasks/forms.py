from django import forms

class newTask(forms.Form):
	new_task = form.CharField(max_length=200)
