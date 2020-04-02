class Ship:
    def __init__(self, n:str = "none", p:str = "none", f:float = 0, p2:str = "none", c:int = 0 ):
        self.name = n
        self.registration = p
        self.freight = f
        self.departure = p2
        self.personnel = c
    def get_name(self):
        return self.name
    def get_reg(self):
        return self.registration
    def get_freight(self):
        return self.freight
    def get_dep(self):
        return self.departure
    def get_pers(self):
        return self.personnel
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.name, self.registration,self.freight,self.departure,self.personnel)
    def words(self, word):
                while word.isalpha() == False:
                    print("Error. Wrong word in object with name ", self.name, " ")
                    word = str(input("Enter another word "))
                return word
    def numbs(self,num):
        while self.isfloat(num) == False or num[0] == "-":
            print("Error. Wrong number in object with name ", self.name, " ")
            num = str(input("Enter another number "))
        return float(num)
    
    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
    def numbsint(self, num):       
                while num.isdigit() == False:
                    print("Error. Wrong number in object with name ", self.name, " ")
                    num = str(input("Enter another number "))
                return int(num)
    def inp_from_file(self, line):
        
        a = line.split()

        self.name = self.words(a[0])
        self.registration = self.words(a[1])
        self.freight = self.numbs(a[2])
        self.departure = self.words(a[3])
        self.personnel = self.numbsint(a[4])
    def __getitem__(self, key):
        if key == 1:
          return getattr(self, "name")
        elif key == 2:
          return getattr(self, "registration")
        elif key == 3:
          return getattr(self, "freight")
        elif key == 4:
          return getattr(self, "departure")
        elif key == 5:
          return getattr(self, "personnel")
        else:
            print("no such attribute!")
    def __copy__(self):
        my_copy = self
        return my_copy
    def input_new(self):
        self.name = self.words(str(input("input new name ")))
        self.registration = self.words(str(input("input new registration ")))
        self.freight = self.numbs(str(input("input new freight ")))
        self.departure = self.words(str(input("input new departure ")))
        self.personnel = self.numbsint(str(input("input new personnel ")))
    
    
   
        
    
   


