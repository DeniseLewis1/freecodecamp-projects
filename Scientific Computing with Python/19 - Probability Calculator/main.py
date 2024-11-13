import copy
import random

class Hat():
    pass

    def __init__(self, **kwargs):
        self.contents = []

        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number):
        balls_drawn = []

        if number > len(self.contents):
            number = len(self.contents)

        for i in range(number):
            ball = self.contents.pop(random.randrange(len(self.contents)))
            balls_drawn.append(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        
        colors_matched = 0
    
        for key, value in expected_balls.items():
            if balls_drawn.count(key) >= value:
                colors_matched += 1

        if colors_matched == len(expected_balls):
            count += 1

    return count / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
