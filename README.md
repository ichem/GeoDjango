# GeoDjango
Quick Stark GeoDjango

# Install 
```
django-admin startproject geodjango
cd geodjango
python3 manage.py startapp world
```

# See data info
```
ogrinfo -so world/data/TM_WORLD_BORDERS-0.3.shp TM_WORLD_BORDERS-0.3
```

# Migration 
```
python3 manage.py makemigrations
python3 manage.py migrate
```

