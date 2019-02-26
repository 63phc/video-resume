from .education import urlpatterns as education
from .job import urlpatterns as job
from .skill import urlpatterns as skill
from .resume import urlpatterns as resume


app_name = 'dashboard_worker'

urlpatterns = resume + skill + job + education

