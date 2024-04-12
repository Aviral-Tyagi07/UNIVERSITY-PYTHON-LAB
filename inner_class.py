class Employee:
    def __init__(self):
        self.name = "Aviral"
        self.sapid = 500121824
        self.AC= self.activity_coordinator()
    def info(self):
        print(self.name, self.sapid)
        
    class activity_coordinator:
        def info(self):
            print("Now I Become Death ")
            
E1=Employee()
E1.info()
E2=E1.AC
E2.info()



class assistant_prof:
    def __init__(self, name, id):
        self.name=name
        self.id=id
    def show(self):
        print(f"My name is: {self.name}")
        print(f"My id is: {self.id}")
    class member:
        def show(self):
            print("Destroyer of the world")
            
AP= assistant_prof.member()
AP.show()
AP1= assistant_prof("Aviral", 500121824)
AP1.show()
AP2=AP1.member()
AP2.show()
