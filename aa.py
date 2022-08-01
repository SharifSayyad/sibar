class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def description(self):
        print(f'hi may name is {self.name} I am a {self.gender} and i am {self.age} years of old')
    
    
    
class Boy(Human):
    def __init__(self,abc):
        try:
            a,b,c = input('Enter name , age, gender').split()
            super().__init__(a,b,c)
            self.abc = abc
        except Exception:
            print('enter only three value')
            a,b,c = input('Enter name , age, gender').split()
            super().__init__(a,b,c)
            
    def schoolName(self,schollname):
        print(f'i study in {schollname}')
        
b = Boy('aa')
b.description()
#b.schoolName('abc')