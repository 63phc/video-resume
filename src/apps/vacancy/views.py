from django import forms
from django.conf import settings
from django.forms import widgets
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views import generic

from src.apps.account_hr.models import AccountHr
from .models import Vacancy, Tag


class RelatedFieldWidgetCanAdd(widgets.Select):
    def __init__(self, related_model, related_url=None, *args, **kw):

        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAdd, self)
                  .render(name, value, *args, **kwargs)]
        output.append('<a href="%s" class="add-another" id'
                      '="add_id_%s" onclick="return showAddAnotherPopup(this)'
                      ';"> ' % (self.related_url, name))
        output.append('<img src="%sadmin/img/icon-addlink.svg" width="10" '
                      'height="10" alt="%s"/></a>' % (
                          settings.STATIC_URL, 'Add Another'))
        return mark_safe(''.join(output))


class VacancyDetail(generic.DetailView):
    template_name = 'vacancy/detail.html'
    model = Vacancy


class VacancyCreateForm(forms.ModelForm):
    tags = forms.ModelChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=RelatedFieldWidgetCanAdd(
            AccountHr, related_url="vacancies:tag_create")
    )

    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'tags',
                  'is_activated', ]

    def get_initial(self):
        account_hr = get_object_or_404(AccountHr, user=self.request.user)
        return {
            'account_hr': account_hr,
        }


class VacancyCreate(generic.CreateView):
    template_name = 'vacancy/create.html'
    model = Vacancy
    form_class = VacancyCreateForm


class TagCreate(generic.CreateView):
    template_name = 'vacancy/create_tag.html'
    model = Tag
    fields = ['title', ]
