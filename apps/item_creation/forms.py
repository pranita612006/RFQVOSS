from django import forms


class SendItemEmailForm(forms.Form):
    recipient_email = forms.EmailField(
        label="Recipient Email",
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter recipient email address",
                "required": True,
            }
        ),
    )
