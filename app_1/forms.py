# from django import forms
# from .models import bookList

# class bookForm(forms.ModelForm):
#     class Meta:
#         model = bookList
#         fields = '__all__'
        
        
#         lables = {
#             'id':'bookId',
#             'bookName':'bookName',
#             'authorName':'authorName',
#             'bookDescription':'bookDescription'
#         }
        
#         widgets  ={
#             'iid' : forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
#             'bookName' : forms.TextInput(attrs={'placeholder': 'eg. book name'}),
#             'authorName' : forms.TextInput(attrs={'placeholder': 'eg. Shil'}),
#             'bookDescription' : forms.TextInput(attrs={'placeholder': 'eg. desc'}),
#         }