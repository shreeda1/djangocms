from mediumeditor.widgets import MediumEditorTextarea

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        widgets = {
            'my_text_field': MediumEditorTextarea(),
        }