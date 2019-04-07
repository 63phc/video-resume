from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils.html import escape
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from src.apps.account_hr.models import AccountHr
from .models import Vacancy, Tag


class MultipleSelectWithPop(forms.SelectMultiple):
    def render(self, name, *args, **kwargs):
        html = super(MultipleSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string("form/popupplus.html", {'field': name})

        return html+popupplus


class VacancyDetailView(generic.DetailView):
    template_name = 'vacancy/detail.html'
    model = Vacancy


class VacancyListView(generic.ListView):
    template_name = 'vacancy/list.html'
    model = Vacancy


class VacancyCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=MultipleSelectWithPop
    )

    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'tags',
                  'is_activated', 'account_hr']


class VacancyCreateView(generic.CreateView):
    template_name = 'vacancy/create.html'
    model = Vacancy
    form_class = VacancyCreateForm

    def get_success_url(self):
        return reverse_lazy('dashboard_hr:main')

    def get_initial(self):
        return {'account_hr': AccountHr.objects.get(user=self.request.user),}


class VacancyUpdateView(generic.UpdateView):
    template_name = 'vacancy/create.html'
    model = Vacancy
    form_class = VacancyCreateForm

    def get_context_data(self, **kwargs):
        context = super(VacancyUpdateView, self).get_context_data(**kwargs)
        context['operation'] = 'update'
        return context


class VacancyDeleteView(generic.DeleteView):
    template_name = 'vacancy/delete.html'
    model = Vacancy


# class TagCreate(generic.CreateView):
#     template_name = 'vacancy/create_tag.html'
#     model = Tag
#     fields = ['title', ]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', ]


def handlePopAdd(request, addForm, field):
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            try:
                newObject = form.save()
            except forms.ValidationError as error:
                newObject = None
            if newObject:
                return HttpResponse('<script type="text/javascript">opener.dismissAddRelatedObjectPopup(window, "%s", "%s");</script>' % \
                    (escape(newObject._get_pk_val()), escape(newObject)))
    else:
        form = addForm()
    pageContext = {'form': form, 'field': field}
    return render_to_response("vacancy/add_popup.html", pageContext)


@csrf_exempt
def tag_create_view(request):
    return handlePopAdd(request, TagForm, 'tags')
