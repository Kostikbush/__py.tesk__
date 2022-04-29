from classTools import AttrDisplay
class Person(AttrDisplay):
    def __init__(this, name, job=None, pay=0):
        this.name = name
        this.job = job
        this.pay = pay
    def lastName(this):
        return this.name.split()[-1]
    def giveRaiser(this, percent):
        this.pay = int(this.pay * (1 + percent))
    def __str__(this):
        for key in this.__dict__:
            print(key, '=>', getattr(this, key)) 
        return '[Person: %s, %s, %s]' % (this.name, this.pay, this.job)

class Manager(Person):
    def __init__(this, name, pay):
        Person.__init__(this, name, 'Manager', pay)
    def giveRaiser(this, percent, bonus=0.1):
        Person.giveRaiser(this, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='Dev', pay=100000)
    print(bob)
    print(sue)
    #print(bob.lastName(), sue.lastName())
    #sue.giveRaiser(0.1)
    #print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaiser(0.1)
    #print(tom.lastName())
    print(tom)
    #print('--All three--')
    #for object in (bob, sue, tom):
        #object.giveRaiser(0.1)
        #print(object)

    class Department:
        def __init__(this, *args):
            this.members = list(args)
        def addMember(this, person):
            this.members.append(person)
        def giveRaises(this, percent):
            for person in this.members:
                person.giveRaiser(percent)
        def showAll(this):
            for person in this.members:
                print(person)
    print('----Class Departament-----')
    development = Department(bob, sue) # Встраивание объектов в составной объект
    development.addMember(tom)
    development.giveRaises(.10) # Вызов метода giveRaise вложенных объектов
    development.showAll() # Вызов метода __str__ вложенных объектов
