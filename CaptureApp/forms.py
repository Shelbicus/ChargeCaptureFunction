from django import forms 
#add email intry/flat rate cost values 

modalList = (
    ("200", "CT Scan"),
    ("300", "X-ray"),
    ("400", "MRI"))
timeList = (
    ("100", "30 min"),
    ("150", "60 min"),
    ("200", "120 min"))

class ChargeForm(forms.Form):
    '''charge capture form'''
    patient_email = forms.CharField(label='Enter patient email', max_length=50)
    modal_type = forms.ChoiceField(label='Please enter modal type',
    choices=modalList)
    time_amount = forms.CharField(label='Please enter the amount of time',
    widget=forms.Select(choices=timeList))
 
    def calcPrice(self):
        """calcPrice : calculate the price
            returns: Total cost of visit(int)"""
        cost = int(self.cleaned_data["modal_type"]) + int(self.cleaned_data ["time_amount"])
        print(cost)
        return(cost)

        