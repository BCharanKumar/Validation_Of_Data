from django import forms
from app.models import *
class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
    remail=forms.EmailField()
    phone=forms.CharField(min_length=10,max_length=10)
    botcatcher=forms.CharField(max_length=25,widget=forms.HiddenInput,required=False)


    def clean_botcatcher(self):
        bc=self.cleaned_data['botcatcher']
        if len(bc)>0:
            raise forms.ValidationError('error')
    def clean(self):
        se=self.cleaned_data['semail']
        re=self.cleaned_data['remail']
        if se!=re:
            raise forms.ValidationError('hello error here..')