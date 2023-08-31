from django_filters import FilterSet, DateTimeFilter
from django.forms import DateInput
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title',#: ['exact'],
            'author',#: ['exact'],
            'postCategory',#: ['exact'],

        }

    time_in = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Publication date from:',
        widget=DateInput(format='%Y-%m-%d',
                         attrs={'type': 'datetime-local'}
                         )
    )