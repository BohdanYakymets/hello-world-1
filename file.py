
import os


class File:

  def __init__(self, name:str):
      self.f = name

  def file_exist(self):
    if os.path.exists(self.f) and os.path.getsize(self.f) > 0:
      
          return True
    else:
      return False

  def file(self):
    while self.file_exist() == False:
        f = str(input(" error, file doesn`t exist or is empty \ninput new name of file "))
    return self.f


