from django import forms
from .models import FeedbackForm
from django.core.exceptions import ValidationError

class FieldForm(forms.ModelForm):
    def validate_Comment(value):
        comment_field = value
        if comment_field.isdigit():
            raise forms.ValidationError("Please enter combination of number and letter")
        else:
            return value
    
    Comment = forms.CharField(
        validators = [validate_Comment],
        widget = forms.Textarea(
            attrs = {
                'class':'form-control', 'id': 'comment', 
                'placeholder' : "Enter your suggestion or comment",
            }
        )
    )

    class Meta:
        model = FeedbackForm
        fields = [
            'Faculty',
            'Satisfaction',
            'Comment',
        ]

        widgets = {

            'Faculty' : forms.Select(
                attrs = {
                    'type' : 'datalist', 'id':'faculty', 'class':'form-control',
                }
            ),

            'Satisfaction' : forms.NumberInput(
                attrs = {
                    'type':'number', 'step': '1', 'min': '1', 'max': '10', 'id':'satisfaction',
                    'class':'form-control', 'placeholder' : "Scale 1 - 10",
                }
            ),
        }
