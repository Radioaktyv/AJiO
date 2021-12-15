from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)


class CreateNewDish(forms.Form):
    name = forms.CharField(label="Name", max_length=40, required=False)
    description = forms.CharField(label="Description", max_length=200, required=False)
    price = forms.FloatField(label="Price", min_value=0, required=False)
