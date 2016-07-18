"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Three main design advantages of OO are abstraction, Encapsulation, 
   and Polymorphism. I have explained each concept down below:

   Abstraction: Abstraction helps making things less complicated by hiding
   things that we don't need to know. For example, with a dishwasher we have 
   an interace with buttons to start the machine, select the type of wash, etc..
   These buttons make the machine do different things, but we don't know the
   mechanics behind it. In python's case, we don't need to know information a
   method uses internally.

   Encapsulation: Encapsulation helps keeping like things together. It helps
   organize data where it is used. In python's case, a class encpsulates it's
   attributes and methods so when the program is running they can be grabbed
   from the class itself. If we have child classes the child classes can easily
   access these things from the parent class. 

   Polymorphism: Polymorphism helps making different types of one thing, without
   creating new things scratch - especially if they have interchangable 
   qualities. Polymorphism allows one class to use components from their parent
   class. Using inheritence while creating subclasses, a paves the way for 
   Polymorphism.

2. What is a class?

    A class is type of thing - a framework that basically says here are
    a few general qualities of this thing and a few actions the thing can do.
    For example, there can be a car class with make, model, vin number, license
    plate -- all attributes of the car class.

3. What is an instance attribute?

    An individual instance of a class is a version of that 'thing'. You need to
    call the class to create an instance since it's dependent on whatever
    attributes and methods the class has to offer. There are class and
    attribute instances. An instance attribute is used to replace class
    attributes. An instance attribute can also be a new attirubte particular for 
    that instance.

4. What is a method?

    A method is a function that's been stragetically placed under a class. At
    least one parameter must be passed for each method. Methods usually pass
    different class attributes depending on method, though only passing self
    is very common.

5. What is an instance in object orientation?
    
    Instance and object are interchangable when talking about OO. An instance is
    a version of the class, taking attributes and methods from the class to define
    itself. It's a particular thing rather than the general thing. For instance
    (pun intended), if you take a class called Student, you could have attributes
    such as name, graduation_year, address, student_id, age, major, etc... An instance 
    of this class would be sanchita = Student(), so sanchita.name = 'Sanchita', 
    sanchita.address = '1221A Divisadero', sanchita.student_id = None, and so on... 
    sanchita is now an instance of the class Student.


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is a piece of data on the class itself. An instance will 
   find the data from the class when an instance attribute isn't set directly on
   the instance/object. 

   For example, if a class attribute sets the age of a Hackbrighter to be 
   age = 23, and I passed an object sanchita = Student(), I would make sure to
   create an instance attribute on the object sanchita as sanchita.age = 25. 
   That way, I am overriding the class attribute value of 23 and providing 
   the correct info for that particular instance.


"""


# Parts 2 through 5:
# Create your classes and class methods


######################################PART 2####################################

class Student(object):
    def __init__(self, first_name, last_name, address): # 2 arguements, 3 parameters
        self.first_name = first_name # attribute for first name
        self.last_name = last_name # attribute for last name
        self.address = address # attribute for address

    def StudentInfo(self): # just to confirm if the function works :)
        print self.first_name + " " + self.last_name + " lives at " + self.address

# Question class stores questions and answers for the exam class.
# The Exam class has a method create exam, which takes the questions from the
# question class and puts them in an empty list - initialize the list within
# the Exam class


# class Question creates questions with parameters question and correct answer
class AbstractQuestion(object):
    def __init__(self, question, correct_answer):  # parameters asked from user
        self.question = question  # question class attribute
        self.correct_answer = correct_answer  # answer class attribute


class Exam(object):
    def __init__(self, question, correct_answer, exam_name, questions):
        self.question = question
        self.correct_answer = correct_answer
        self.exam_name = exam_name
        self.questions = []

# keep at it at home -- 
    def CreateExam(self):
        exam_dict = {}

        for exam_name not in exam_dict.keys():

            

    return exam_dict
      





######################################PART 3####################################



######################################PART 4####################################
