#!/usr/bin/python

class student(object):
    name = 'student'
    def __init__(self, name):
        self.name = name
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score is not int')
        if value < 0 or value > 100:
            raise ValueError('score is not invalid')
        self._score = value


s = student("a")
s.score = 60
t = student("t")
t.score = 61

print s.score, s.name, t.score, t.name, student.name
