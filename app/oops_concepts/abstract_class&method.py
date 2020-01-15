from abc import ABC, abstractmethod

"""
 Case 1:
     We can't create a object of any class directly which is inherited class ABC from abc built-in module.
     
 Case 2: 
     We can create an object of any non-inherited ABC class in which any of the method is abstractmethod
     but if you try to access abstract method through object it will through an error.
 
 Case 3:
    If any class has been inherited any abstract class then child class must have to implement the abstract method 
    otherwise it will throw an error while create an object. 
   
   So we can't create object of any class while inherit ABC class from this class(create object through other class
    & implement abstract method also) but if declare any abstract method inside of any normal class then you can 
    create object of this class without raise any error but error will come when you will try to access this abstract 
    method through created object.  
"""

class Animal():

    @abstractmethod
    def move(self):
        raise NotImplementedError

    def a(self):
        print("normal method")

class Human(Animal):

    def move(self):
        print("I can walk & run....")
    # pass

class Snake(Animal):

    def crawl(self):
        print("I can  crawl soo fast....")


def main_v1():
    animal = Animal()
    animal.a()
    # animal.move()

    human = Human()
    human.move()

    snake = Snake()
    snake.crawl()

class Automobile(ABC):

    @abstractmethod
    def mobile_model(self):
        raise NotImplementedError


class Mobile(Automobile):

    def mobile_model(self):
        print("APPLE A7")


def main_v2():
    mobile = Mobile()
    mobile.mobile_model()

if __name__  ==  "__main__":
    main_v1()
    main_v2()

