# video-resume

How to switch settings from development to production and back:
in the folder scr/settings/environments you need to have a file named 
local.py (which is excluded from git-repo) where you may choose
what settings you want to load - development or production:

```from src.settings.environments.development import *```   


```
# ALL Docker
docker-compose -f docker/docker-compose.local.yml up 
# ONLY db
docker-compose -f docker/docker-compose.local.yml up postgresql
python manage.py runserver
```