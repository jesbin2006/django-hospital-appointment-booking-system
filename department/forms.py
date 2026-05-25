from django import forms
from home.models import Appointment
from doctors.models import Doctors


class DateInput(forms.DateInput):
    input_type = 'datetime-local'


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            'name',
            'phone',
            'age',
            'department',
            'doctor',
            'date',
            'person_type',
            'payment_method'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'person_type': forms.Select(attrs={'class': 'form-select'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # -----------------------------------
        
        # -----------------------------------
        self.fields['doctor'].queryset = Doctors.objects.none()

        # -----------------------------------
    
        # -----------------------------------
        if 'department' in self.data:
            try:
                dept_id = int(self.data.get('department'))
                self.fields['doctor'].queryset = Doctors.objects.filter(
                    department_id=dept_id,
                    active=True
                )
            except (ValueError, TypeError):
                pass

        # -----------------------------------
        
        # -----------------------------------
        elif self.instance.pk:
            self.fields['doctor'].queryset = Doctors.objects.filter(
                department=self.instance.department,
                active=True
            )