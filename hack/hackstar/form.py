from django import forms
from .models import cleanliness_model, lost_found_model, contact_model,Order

x = forms.TextInput(attrs={'class':"form-control"})


class cleanliness_form(forms.ModelForm):
    name = forms.CharField(required=True, widget=x)
    description = forms.CharField(required=True, widget=x)
    pnr = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':"form-control"}))
    building_name = forms.CharField(required=True, widget=x)
    class_no = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':"form-control"}))
    cleaned = forms.CharField(required=True, widget=x)

    class Meta:
        model = cleanliness_model
        fields = ['name', 'description', 'pnr', 'building_name', 'class_no','cleaned']


x1 = forms.TextInput(attrs={'class': "form-control"})


class lost_found_form(forms.ModelForm):
    name = forms.CharField(required=True, widget=x1)
    description = forms.CharField(required=True, widget=x1)
    pnr = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':"form-control"}))
    building_name = forms.CharField(required=True, widget=x1)
    class_no = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':"form-control"}))
    item = forms.CharField(required=True, widget=x1)
    date_time = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(2000,2030)))
    found = forms.CharField(required=True, widget=x1)
    image = forms.FileField(required=True, widget=forms.FileInput(attrs={'class':"form-control"}))

    class Meta:
        model = lost_found_model
        fields = ['name', 'description', 'pnr', 'building_name', 'class_no', 'item','date_time','image','found']


class contact_form(forms.ModelForm):
    class Meta:
        model = contact_model
        fields = ['name', 'email', 'message']


class order_form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'tprice', 'items_json','time', 'phone', 'status']