import memento
import classShip
import file
import classCont
import os
import copy

name1 = file.File("input.txt")
name2 = file.File("write.txt")
wr = name2.file()
inp = name1.file()
f = open(inp)
write = open(wr,"a")
b = classShip.Ship()
l = classCont.ShipContainer()
l.create_list(f)
action = 1
originator = memento.Originator(l)
caretaker = memento.Caretaker(originator)
while action != 0:
    print ("Choose the action and write it`s number ")
    print("1.print ")
    print("2.sort")
    print("3.delete ")
    print("4.add new item")
    print("5.edit one item")
    print("6.find item")
    print("7.undo")
    print("8.redo")
    print("9.history")
    print("0.exit")
    action = int(input())
    if action == 1:
        caretaker.backup()
        originator.do_something(classCont.pr_wr(l,write))
        
    elif action == 2:
        a = 1
        while a != 0:
            print("Select one item of the list and write it`s number")
            print("1.Sort by name")
            print("2.sort by place of registration")
            print("3.sort by freight")
            print("4.sort by departure")
            print("5.sort by number of personnel")
            print("To return press 0\n")
            a = int(input())
            if a == 0:
                break
            caretaker.backup()
            originator.do_something(l.sort_by_attr(a))
            classCont.pr_wr(l,write)               
                    
    elif action == 3:
        name = str(input("input name of element "))
        caretaker.backup()
        originator.do_something(l.delete_by_name(name))
        classCont.pr_wr(l,write)
    elif action == 4:
        caretaker.backup()
        originator.do_something(l.add_new())
        classCont.pr_wr(l,write)
    elif action == 5:
        name = str(input("input name of element "))
        caretaker.backup()
        originator.do_something(l.edit_by_name(name))
        classCont.pr_wr(l,write)
    elif action == 0:
        break
    elif action == 6:
        name = str(input("input data for searching "))
        l.find_obj(name)
    elif action == 7:
        caretaker.undo()
    elif action == 8:
        caretaker.redo()
    elif action == 9:
        caretaker.show_history()
    else:
        print("incorrect number")
        continue


