from django.contrib import admin

from . import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from pereval.models import Perevals, Images

admin.site.register(Perevals)
admin.site.register(Images)


class ImagesAdminForm(forms.ModelForm):
    Image = forms.CharField(label='изображение', widget=CKEditorUploadingWidget())

    class Meta:
        model = Images
        fields = '__all__'