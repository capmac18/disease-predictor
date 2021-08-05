from django import forms

class SymptomForm(forms.Form):
    symptom_1 = forms.CharField(required=False)
    symptom_2 = forms.CharField(required=False)
    symptom_3 = forms.CharField(required=False)
    symptom_4 = forms.CharField(required=False)
    symptom_5 = forms.CharField(required=False)