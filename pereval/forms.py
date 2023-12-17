from django import forms

from pereval.models import Images

from ckeditor.fields import RichTextFormField


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']


        class Meta:
            model = Images
            fields = ['image']
            widgets = {
                'image': RichTextFormField(),
            }
