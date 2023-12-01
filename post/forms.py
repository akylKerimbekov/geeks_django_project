from django import forms

from post.models import Post, Product


class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    rate = forms.IntegerField(min_value=1, max_value=5)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if len(title) < 10:
            raise forms.ValidationError("Title to short!")
        return cleaned_data

    def clean_content(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if len(content) < 40:
            raise forms.ValidationError("content to short!")
        if not content:
            raise forms.ValidationError("content is required!")
        return cleaned_data


class PostCreateForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'rate']


class ProductCreateForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    price = forms.FloatField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('name')
        if len(title) < 10:
            raise forms.ValidationError("Name to short!")
        return cleaned_data

    def clean_content(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if len(description) < 40:
            raise forms.ValidationError("description to short!")
        if not description:
            raise forms.ValidationError("description is required!")
        return cleaned_data


class ProductCreateForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price']
