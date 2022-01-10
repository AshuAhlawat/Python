//can be skipped
# Creating Virtual Enviornment

    pip install pipenv
    pipenv install django//in the repo directory to create a pipfile recording all versions
    pipenv shell// to start using versions wrote in pipfile 

# Django commands
    //write django-admin to see all

    django-admin startproject <projectname> <dir>//if not mentioned creates a subfolder and the project in it/ use . instead
    
# Running Server
    // after we are already in the project use the manage.py file instead as it takes our project in account instead of django-admin
    
    python3 manage.py// to see all commands

    python3 manage.py runserver <port>//uses 8000 by default
    // now you can see the app in browser at the given port

# Creating Apps

    python3 manage.py startapp <appname>//should be then added in settings.py in installed apps : <name>

# Creating Request Handlers in View.py

    // add functions that take request as a parameter say
    def hello(request):
        return HttpResponse("<h1>Hello</h1>")

# Now associating the request handlers with a url
    // create a urls.py and import path and the views.py in it to use the funcs

    urlpatterns = [
    path("hello/", views.hello),
    ]

    // now go to the <projectname>/urls.py and import include to add the redirect to the app

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('<appname>', include("<appname>.urls")),
    ]

# Templates

    // add templates folder in the app for which the templates are
    // now create .html files there 
    // now we can return/ render .html files in the views.py for specific requests
    return render(request, "<filename>.html", dicts)
    //these dicts can be used to parse info from backend to frontend