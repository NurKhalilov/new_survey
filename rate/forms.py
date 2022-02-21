from .models import Rating, Salesperson
from django import forms


class RateAddForm(forms.ModelForm):
    class Meta:
        model = Rating
        widgets = {
            'rating': forms.RadioSelect(attrs={'class': 'form-check form-check-inline'}),
            'salesperson': forms.Select(attrs={'placeholder': 'Choose the name of salesman'}),
        }
        fields = "__all__"

    def __init__(self, *args, region_id=None, **kwargs):
        super(RateAddForm, self).__init__(*args, **kwargs)
        self.fields['salesperson'].label = "Xodimni tanlang / Выберите сотрудника: "
        self.fields['price'].label = "Savdo narxi / Цена покупки: "
        self.fields['rating'].label = "Baho / Оценка: "
        if region_id:
            self.fields['salesperson'].queryset = Salesperson.objects.filter(region=region_id)
