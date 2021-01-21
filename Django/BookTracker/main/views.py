from django.shortcuts import render
import pymongo
import pandas

myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["BookTracker"]
books = mydb["main_book"]

def base(response):
    return render(response, 'main/base.html')

def home(response):
    #get responses
    
    
    #backend
    all_books = pandas.DataFrame(books.find({}))

    length = len(all_books)
    c=1
    uc=1
    djbooksc=[]
    djbooksuc=[]
    for i in range(length):
        if all_books["name"][i]!="None":
            if all_books["completed"][i] in ('on',True):
                djbooksc.append({"id":c, "name":all_books["name"][i], "completed":"Yes"})
                c+=1
            else:
                djbooksuc.append({"id":uc, "name":all_books["name"][i], "completed":"No"})
                uc+=1
    
    
        
    #passing values
    dicts={
        "name": { "first" : "Ashwani", "last":"Ahlawat"},
        "booksc":djbooksc,
        "booksuc":djbooksuc,
    }
        
    return render(response, 'main/home.html', dicts)

def add(response):
    #get responses

    bookname = response.GET.get('bookname','None')
    bookstatus = response.GET.get('status',False)
    
    all_books = pandas.DataFrame(books.find({}))
        
    i=max(all_books["id"])+1            
        
    books.insert_one({"id":i, "name":bookname, "completed":bookstatus})
    #backend
    
    
    #passing values
    dicts={
        "name": { "first" : "Ashwani", "last":"Ahlawat"},
        "books":"",
        "statuses":"",
        "length": ""
    }
    
    return render(response, 'main/add.html', dicts)

def about(response):
    
    #backend
    var = ""
    for i in range(11):
        for j in range(i):
            var += str(j+1)
        var+="\n"
    
    
    #passing values
    dicts={
        "var":var
    }
    
    return render(response, 'main/about.html',dicts)

