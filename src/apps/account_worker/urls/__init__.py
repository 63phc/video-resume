from .education import urlpatterns as education
from .job import urlpatterns as job
from .skill import urlpatterns as skill
from .resume import urlpatterns as resume
from .question import urlpatterns as question


app_name = 'dashboard_worker'

urlpatterns = resume + skill + job + education + question
