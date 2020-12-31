from django.http import HttpResponse
from django.shortcuts import render


def home(response):
    
    dicts={
        "name": { "first" : "Ashwani", "last":"Ahlawat"}
    }
    
    return render(response, 'home.html', dicts)

def links(response):
    return HttpResponse("""<h2><a href="https://www.youtube.com/watch?v=-2uyzAqefyE&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj&index=2"> PyQt5</a><br><br><a href="https://www.youtube.com/watch?v=E-1xI85Zog8"> Djongo</a><br><br><a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> Django</a></h2>""")

