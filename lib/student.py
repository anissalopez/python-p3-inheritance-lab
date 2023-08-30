#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge = None):
        super().__init__(first_name, last_name)
        self.knowledge = [] if knowledge == None else knowledge
    
    def learn(self, str):
        self.knowledge.append(str)
        return self.knowledge