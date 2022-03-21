from django import forms


class AgreeForm(forms.Form):
    agree = forms.BooleanField(required=True, error_messages={'required': "동의해주세요."})

    class Meta:
        fields = ['agree']
        labels = {'agree': '동의'}
