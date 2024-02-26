from django import forms
from documents.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ("file", "name", "description")

    widgets = {
        "name": forms.TextInput(attrs={"class": "form-control"}),
        "description": forms.Textarea(attrs={"class": "form-control"}),
        "file": forms.FileInput(attrs={"class": "form-control-file"}),
    }
