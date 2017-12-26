# GeoDjango
Quick Stark GeoDjango

# Requirements
PostGIS and Postress
Add a superuser geo with geosint pass in geodjango database

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

# Download and import data
```
cd world/data
wget http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip
unzip TM_WORLD_BORDERS-0.3.zip
cd ../..
python3 manage.py shell
from world import load
load.run()
```

# Create a superuser
```
python3 manage.py createsuperuser
```

# Run 
```
pyton3 managy.py runserver
```
Access <https://127.0.0.1:8000/admin>