items = ['first string', 'second string','third option']
html_str = "<ul>\n"


for item in items:
    html_str += "<li>"+item+"</li>\n"

html_str +=  "</ul>"
print(html_str)