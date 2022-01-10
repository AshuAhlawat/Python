import requests

#get
post1 = {'name' : "Ashwani Ahlawat", 'class' : "1st Year"}
r = requests.get("https://httpbin.org/get",params=post1)

print(r,'\n')
print(dir(r),'\n')
# print(help(r))
print(r.url,'\n')
print(r.content,'\n')
print(r.headers,'\n')
print(r.text,'\n')

#post
post2 = {'username' : "Ashwani Ahlawat", 'password' : "1stYear"}
r = requests.get("https://httpbin.org/get",data=post2)

r_dict = r.json()
print(r_dict,'\n')

#put
user = str(input("Username : "))
password = str(input("Password : "))

r = requests.get('https://httpbin.org/basic-auth/ashua/1234', auth=(user,password))

print('\n\n',r,'\n')
print(r.text,'\n')

#timeout
timeout = int(input("How many secs does your sites load in? -- "))
try:
    r = requests.get('https://httpbin.org/delay/5', timeout=timeout)
    
    print(r)
except:
    print("Error : ",r.status_code)