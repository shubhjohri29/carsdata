from random import choices
from django import forms

BUDGET_data = ( 
        ("1", "200000 - 500000"), 
        ("2", "500000 - 1000000"), 
        ("3", "1000000 - 2000000"), 
        ("4", "2000000 - 3000000"), 
        ("5", "3000000 - 4000000"),
        ("6", "4000000 - 5000000"),
        ("7", "5000000 - 7000000"),
        ("8", "7000000 - 10000000"),
        ("9", "10000000 - 50000000"),
        ("10", "50000000 - 100000000"),
        ("11", "100000000 - 200000000"),
        ("12", "200000000 - 250000000")
    ) 
    
BODY_TYPE = (
    ("1", "Hatchback"),
    ("2", "SUV"),
    ("3", "MPV"),
    ("4", "Sedan"),
    ("5", "Coupe"),
    ("6", "Crossover"),
    ("7", "Sports"),
    ("8", "MUV"),
    ("9", "Pick-up")
)

SEATS = (
    ("1", "2"),
    ("2", "4"),
    ("3", "5"),
    ("4", "6"),
    ("5", "7"),
    ("6", "8"),
    ("7", "9")
)

MILEAGE_data = (
    ("1", "0-5"),
    ("2", "5-10"),
    ("3", "10-15"),
    ("4", "15-20"),
    ("5", "20-25"),
    ("6", "25-30"),
    ("7", "30-35")
)
# creating a form
class InputForm(forms.Form):
    # name = forms.TextInput()
    # age = forms.EmailInput()
    BUDGET = forms.ChoiceField(choices = BUDGET_data)
    BODY_TYPE = forms.ChoiceField(choices = BODY_TYPE)
    SEATING_TYPE = forms.ChoiceField(choices = SEATS)
    MILEAGE = forms.ChoiceField(choices = MILEAGE_data)


from .models import UserData


class UserDataFrom(forms.ModelForm):
    # BUDGET = forms.CheckboxInput(choices = BUDGET_data)
    class Meta:
        model = UserData
        fields = ['username','email','password']
