from ckeditor.widgets import CKEditorWidget

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):


    content = forms.CharField(
        widget=CKEditorWidget(),
        label="评论",
        required=True,
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('最小长度为10')
        return content

    class Meta:
        model = Comment
        fields = ['content']
