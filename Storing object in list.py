class Movie(object): 
    def __init__(self,title,mins,hero): 
        self.title=title
        self.mins=mins 
        self.hero=hero
    def printer(self): 
        print(f"Title is :{self.title}\n run time is:{self.mins} \n hero is :{self.hero}")

list_of_movies=[]
while True:
    title =input("Enter the title of movies: ")
    mins=input("Enter the mimuts of movies :")
    hero=input("Enter the name of the hero: ")
    obj=Movie(title,mins,hero)
    list_of_movies.append(obj)
    print("Movies added to the list ")
    ans=input("do you want to add another movies (y/n)")
    if ans!="y": 
        break
    print("All movies information: ")
    for obj in list_of_movies: 
        obj.printer()   

