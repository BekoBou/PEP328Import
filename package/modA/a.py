from ..modB.b import SECRET
from ..c import ANOTHER_SECRET
from .d import QUESTION
from .modAX.x import say_answer

def say_secret():
    print(SECRET + " " + ANOTHER_SECRET)
    print("The " + QUESTION + ' is ' + str(say_answer()))
