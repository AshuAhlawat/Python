

menu=int(input("\n-->Forms\n\n(1)Enter  student data\n(2)View   student data\n(3)Delete student data\n  : "))

#ENTRY OF DATA
if menu==1:
    print("\n\n->Enter Data\n")
    f=open("lpu.txt","a+")
    lines=f.readlines()

    switch=1
    while switch == 1:
        regno=str(input("Registeration No : "))
        name=str(input("Name : "))
        for line in lines:
            if regno in line or len(regno)!=8:
                print("\nRegisteration Numbers must be Unique and 8 digits!\n")
                switch=1
            else:
                print("\nSuccessfully Submitted.")
                f.write(regno + "  " + name+"\n")
                f.close()
                switch=0
                break

        if lines==[] and len(regno)==8:
            print("\nSuccessfully Submitted.")
            f.write(regno + "  " + name+"\n")
            f.close()
            switch=0
            break
        else:
            print("\nRegisteration Numbers must be Unique and 8 digits!\n")
            switch=1
            

#VIEW DATA
if menu == 2:
    view_menu=int(input(("\n\n->View Data\n\n(1)View particular student\n(2)View all students\n  : ")))
    if view_menu==1:
        f=open("lpu.txt","r")
        lines=f.readlines()

        switch=0
        while switch == 0:
            regno=str(input("Registeration No : "))
            for line in lines:
                if regno in line:
                    print("\n\n",line)
                    switch=1
                    break
                else:
                    switch=0
            if switch==0:
                print("404 Not Found")
        f.close()
        
    if view_menu==2:
        f=open("lpu.txt","r")
        lines=f.readlines()
        lines.sort()
        print("\n")
        for line in lines:
            print(line)
        f.close

#DELETE DATA
if menu == 3:
    delete_menu=int(input("\n\n->Delete Data\n\n(1)Delete Particular data \n(2)Delete all Data\n  : "))
    
    if delete_menu == 1:
        f=open("lpu.txt","r")
        lines=f.readlines()
        f.close()
        
        for line in lines:
            print("\n\n["+str(lines.index(line))+"] "+line)
        
        index_to_remove=int(input("Enter index number: "))
        del lines[index_to_remove]
        
        f_n=open("lpu.txt","w+")
        for line in lines:
            f_n.write(line)
            
        f_n.close()
        print("\n\nSuccessfully Deleted.")
    if delete_menu == 2:
        
        cmfn=str(input("\nAre you totally sure?(y/n) : "))
        if cmfn=="y":
            f=open("lpu.txt","w")
            f.write(" ")
            f.close()
            print("\nSucessfully Deleted.")
        else:
            print("\nthought so...")
            

#CREDITS : Dingo/Capti