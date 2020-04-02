import classShip

class ShipContainer:
    def __init__(self):
        self.l = list()
    
    def create_list(self, f):
        i = 0
        for line in f:
          line
          self.l.append(classShip.Ship())
          self.l[i].inp_from_file(line)
          i+=1

    def sort_by_name(self):
      self.l.sort( key = lambda x:(x.name.lower()))
      return self
    def sort_by_reg(self):
      self.l.sort( key = lambda x:(x.registration.lower()))
      return self
    def sort_by_freight(self):
      self.l.sort( key = lambda x:(x.freight))
      return self
    def sort_by_departure(self):
      self.l.sort( key = lambda x:(x.departure.lower()))
    def sort_by_personnel(self):
      self.l.sort( key = lambda x:(x.personnel))
      return self
    def sort_by_attr(self, attr):
        if attr == 3 or attr == 5:
          self.l.sort( key = lambda x: x[attr])
        else:
            self.l.sort( key = lambda x: x[attr].lower())
        return self
    def find_obj(self,word):
      m = 0
      for i in range(len(self.l)):
        if word in self.l[i].name  or word in self.l[i].registration or word in str(self.l[i].freight) or word in self.l[i].departure or word in str(self.l[i].personnel):
            print(str(self.l[i]))
            m+=1
      if m == 0:
         print("There are no such elements in the list:(")
    def __str__(self):
        d = ""
        for i in range(len(self.l)):
            d+=str(self.l[i])
            d+='\n'
        return d
    def print_all(self):
      print("\n")
      for i in range(len(self.l)):
         print(str(self.l[i]))
      print("\n")
    def __copy__(self):
        my_copy = self
        return my_copy
    def delete_by_name(self, name):
      m,i = 0,0
      while i < len(self.l):
        if name == self.l[i].name:
            self.l.pop(i)
            m+=1
        i+=1
      if m == 0:
        print("There are no such elements in the list:(")
      return self
    def add_new(self):
      a = classShip.Ship()
      a.input_new()
      self.l.append(a)
      return self
    def edit_by_name(self, name):
      m = 0
      for i in range(len(self.l)):
        if name in self.l[i].name:
            self.l[i].input_new()
            m+=1
      if m == 0:
        print("There are no such elements in the list:(")
      return self
    def write_all_to_file(self,f):
       for i in range(len(self.l)):
         f.write(str(self.l[i]) + '\n')
       f.write("\n\n")

def pr_wr(l,write):
    l.print_all()
    l.write_all_to_file(write)
