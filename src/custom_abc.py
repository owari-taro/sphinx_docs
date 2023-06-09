'''
this is a test module

'''
from sub_module.utils import fetch_data


def hoge(num: int):
    """
    akdfjalkdjfalkdfjalsdf7
    aslkdjfalksdfjlaskdjf
    """
    print("hgoehoghgoeg")


def play(num: int):
    """
    this is a function just printing
    
    :param int num: _description_

    """

    print(num)


def shout(comment: str):
    """
    three thigs to remember

    * error handling
    * clean coding
    * logging!
    
    just shouting
    
    ex:
        shout("test")
        >test


    :param str comment: _description_
    """
    print(comment)



class Person:
    """
    generating person

    | person=Person("test",123)
    | person.walk()
    """    
    def __init__(self, name:str,age:int):
        """
        example usage
        This is a sphinx documentation practice

        person=Person("hoge",10)
        person.walk()
        >


        :param str name: _description_
        :param int age: _description_
        """        
        self.name=name
        self.age=age

    def walk(self):
        """
        just printing out walking 
        """                
        fetch_data("adlfkasjdlfk")

        print("walking")
        print("walking")