from django.views import generic

from .models import Resume


class ResumeDetailView(generic.DetailView):
    template_name = 'resume/detail_nouser.html'
    model = Resume
