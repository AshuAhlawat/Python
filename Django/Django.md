# Django

(Based on the MTV approach)

## Basic

- Creating Projects  
` django-admin startproject {name} `
- Starting projects  
` python manage.py runserver `
- Creating Apps and adding them in Settings  
` python manage.py startapp {name} `

## Urls

```python
#urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # for redirect to an app's url
    path('', include('{name}.urls')),
    # for redirect to a certain function in views file
    path('someurl/', views.function)
    # for carrying data to a fucntion
    path('xyz/<str: name>/<int: age>', function)
]
```

## Views

- Urls.py  
` form . import views `
- Views.py  
` def name(request) -> render/request: ... `
- HttpResponse  
` from django.http import HttpResponse `
- Render function  
` from django.shortcuts import render,redirect `
- Variable Url

```python
def func(request):
    # now we can use the url data
    name = request.name
    age = request.age
    # http response code
    request_type = request.status_code
    print(name,age,request_type)

    return render(request, "temp.html", data)
```

## Templates

- Creating Templates folder and adding it in settings
- Hyper linking the html files
- Django Template Language

```html
<!-- Variables from backend to front -->
{{ data }}

<!-- conditionals -->
<div>
{% if list %}
    Number of athletes: {{ list|length }}
{% elif backup_list %}
    {{ backup_list }}
{% else %}
    No list given.
{% endif %}
</div>

<!-- to make lists -->
<ul>
{% for item in list %}
    <li>{{ item }}</li>
{% endfor %}
</ul>

{% with greeting="hello" name="Ashu"%}
{{greeting}} {{name}}
```

- Template Inheritence

```html
<!--  to make blocks -->
{% block name %}
{% endblock %}

<!-- to inherit blocks -->
{% extends "base.html" %}
```

- Static Files

```python
# add this in settings.py
STATICFILES_DIRS = [
    # str(BASE_DIR) + "/static/"
    BASE_DIR / 'static'
]

# and this in project_home.urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
```

```html
{% load static %}
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="{% static 'base.css' %}">
</head>

<body>
    <img src="{% static 'image.jpg' %}" alt="">
</body>

</html>
```

- GET Forms (data from front-end to backend)  

```html
<form action="/url" method="GET">
    <!-- Input  -->
    <input type="text" name="bookname" placeholder="Harry" required>
    <input type="checkbox" name="status">
    
    <!-- Submit -->
    <input type="submit" value="Add">
</form>
```

- POST Form : just add the {% csrf_token %}  
then in the views we use the data of these forms

```python

def create(request):
    # now the form data is stored in the request argument
    print(request.GET)
    print(request.POST)
```

## Models

- Create Superuser  
` python manage.py createsuperuser `

- Migrations  
` python manage.py makemigrations `  
` python manage.py migrate `

## Django Form Models

## Users

## Deployment

### Heroku

### Server
