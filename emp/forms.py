from django import forms

class Feedback(forms.Form):
    email = forms.EmailField(label = 'Enter you email', max_length = 200)
    name = forms.CharField(label = 'Enter your Name', max_length = 200)
    feedback = forms.CharField(label = 'Enter your Feedback', widget = forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(Feedback, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'