#libraries


#classes
class standard:
    
    def __init__(self,standard):
        self.standard = standard
    
    def tell_standard(self):
        return self.standard

class section(standard):
    
    def __init__(self,standard,section):
        standard.__init__(self,standard)
        self.section = section
    
    def tell_section(self):
        return self.section

class student(section):
    
    def __init__(self,rollno,name,section,standard):
        section.__init__(section,standard)
        self.rollno = rollno
        self.name = name
    
    def tell_student(self):
        return str(self.rollno) + " -- " + self.name

#function
def name(fname,lname):
    return fname.title() + " " + lname.title()


#main

me = student(8,"ashu",'C',12)
print(me.tell_student())
print(me.tell_standard())