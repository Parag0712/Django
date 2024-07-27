from django import forms
from .models import ChaiVarity

class ChaiVarityForm(forms.Form):
    # get all varityes of chai
    chai_varity = forms.ModelChoiceField(
        queryset=ChaiVarity.objects.all(),
        label="Select Chai Varity"
    )
    # chai_varity = forms.CharField()
