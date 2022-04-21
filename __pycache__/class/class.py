class Person:
    def __init__(this, name, job=None, pay=0):
        this.name = name
        this.job = job
        this.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaiser(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def giveRaiser(self, percent, bonus=0.1):
        Person.giveRaiser(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaiser(0.1)
    print(sue)
    tom = Manager('Tom Jone', 'mgr', 50000)
    tom.giveRaiser(0.1)
    print(tom.lastName())
    print(tom)