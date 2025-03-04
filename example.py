# print(bool(123))
# print(bool([]))
# print(bool("abc"))
# print(bool(" "))
# print(bool(["apple","banana","orange"]))

# for i in range(0,5):
#     print(i)


# def myclass():
#     x="saikumar"
#     print("this is the "+ x)
# myclass()


# class myclass():
#     def __len__(self):
#         return 0
# myobj=myclass()
# print(bool(myobj));


# def myfunction():
#     return False

# if myfunction():
#     print("yes");
# else:
#     print("No");

# list=["saium","ljhj"]
# list.remove("saium")
# print(list)

# thisdict={
#     "brand" : "ford",
#     "model" : "sai",
#     "year" : 1964
# }
# print(thisdict)



# thisdict={
#     "brand" : "ford",
#     "model" : "sai",
#     "year" : 1964
# }
# print(thisdict["brand"])

# myfamily ={
#     "child1": {
#         "name" : "sai",
#         "age" : 21
#     },
#     "child2" : {
#         "name" : "saikumar",
#         "age": 21
#     }
# }

# print(myfamily)


# i=1
# while i<6:
#     print(i)
#     i+=1

# i=1
# while i<6:
#     print(i)
#     if i == 3:
#         break
#     i += 1


# i=1
# while i<6:
#     i += 1
#     if i < 6:
#         print("this is the true");
#     elif 6 == 6:
#         print("this isthe sai")
#     print(i)


# adj=["saikumar","saik","sai"]
# fruits= ["apple","banana","cherry"]
# for i in adj:
#     for j in fruits:
#         print(i,j)


# def my_function(fname):
#     print(fname + "saikumar is the");

# my_function("hero")
# my_function("rebel")
# my_function("rambuddi")


# def my_function(fname,lname,sname):
#     print(fname+ " "+lname+ " "+sname)

# my_function("sai","kumar","rambuddi");



# def my_function(*kids):  #kids is a parameter
#     print("this is the kids section",kids[1]);
# my_function("saikumar","alekhya")

# def my_function(child3,child2,child1):
#     print("the youngest child is "+child3)
# my_function(child1="sai",child2="kumar",child3="rambuddi")

# def my_function(**kid):
#     print("this is the saikumar"+kid["lname"])
# my_function(fname="sai", lname="kumar");

# def my_function(country):
#     print("this is the "+country)
# my_function("india")
# my_function("sweden")
# my_function()
# my_function("Brazil")


# food=[1,2,3,4,5,6];
# for i in food:
#     if i ==3:
#         print("its is true");
#     elif i ==5:
#         print("its a saikumar");
#     else:
#         print("its false");

# def my_function(food):
#     for i in food:
#         print(i);
# fruits=["apples","banana","pineapple"]
# my_function(fruits)

# def myfunction(x):
#     return 5* x;
# print(myfunction(9));

# def myfunction(k):
#     if(k>0):
#         result = k + myfunction(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
# print("recursion example results:")
# myfunction(6)


# class myClass():
#     x=5
# p1= myClass();   #p1 is the object 
# print(p1.x)


# class Person:
#     def __init__(self,name,age):
#         self.name =name
#         self.age =age
# p1= Person("johan",36)
# print(p1.age)
# print(p1.name)


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1 = Person("John",36)
# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}({self.age})"
# p1=Person("john",36)
# print(p1)
        
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("Hello my name is " + self.name)
# p1=Person("sai",23)
# p1.myfunc()

# class Person:  # person is the class
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname   # firstname,lastname is the properties

#     def printname(self):
#         print(self.firstname,self.lastname)
# x=Person("John","Doe")
# x.printname()   # printname is the method


# parent to child class
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def myfunct(self):
#         print(self.firstname,self.lastname)
    
# # child class
# class  Student(Person):
#     pass

# x=Student("john","doe")
# x.myfunct()



#we are adding __init__() function on child class

# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def myfunct(self):
#         print(self.firstname,self.lastname)
# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)

# x=Student("sai","rambuddi")
# x.myfunct()

# by using the super() function,you do not  have to use the name of the parent element,it will automatically inherit the methods and properties from its parent
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def myfunct(self):
#         print(self.firstname,self.lastname)
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
# x=Student("sai","kumar")
# x.myfunct();


#adding the parameter

# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def myfunct(self):
#         print(self.firstname,self.lastname)
# class Student(Person):
#     def __init__(self, fname, lname,year):
#         super().__init__(fname, lname)
#         self.graduationyear=year
# x=Student("sai","kumar",2023)
# print(x.graduationyear)


#adding the method to the child class

# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def myfuncti(self):
#         print(self.firstname,self.lastname)
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear=year
#     def printname(self):
#         print("Welcom",self.firstname,self.lastname,"to the class of ",self.graduationyear)
# x=Student("john","saikumar",2023)
# x.printname()

class Car:
    def __init__(self,brand,model):
        self.brand =brand
        self.model= model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self,brand,model):
        self.brand =brand
        self.model=model
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly!")
car1=Car("ford","saikumar");
boat1= Boat("ford","saikumar")
plane=Plane("ford","saikumar") 

for x in(car1,boat1,plane):
    print(x.brand)
    print(x.model)
    x.move()