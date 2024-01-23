from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Version, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ("product_name", "product_description", "product_image", "category", "product_price", "in_stock")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_product_name(self):
        name = self.cleaned_data['product_name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in name:
                raise ValidationError("Нельзя добавлять запрещенные слова в название продукта.")
        return name

    def clean_product_description(self):
        description = self.cleaned_data['product_description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in description:
                raise ValidationError("Нельзя добавлять запрещенные слова в описание продукта.")
        return description


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        # fields = '__all__'
        fields = ('product', 'version_number', 'version_name', 'is_active', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'\

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ("category_name", "category_description",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


