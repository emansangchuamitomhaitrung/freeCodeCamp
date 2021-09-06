import copy
import random


class Hat(object):
    def __init__(self, **kwargs):
        self.contents = []
        self.kwargs = kwargs
        for k in kwargs.keys():
            for _ in range(kwargs[k]):
                self.contents.append(k)

    def draw(self, num_to_draw):
        balls = []
        num = min(num_to_draw, len(self.contents))
        if num_to_draw > len(self.contents):
            return self.contents
        else:
            for _ in range(num):
                index = random.randint(0, len(self.contents)-1)
                balls.append(self.contents.pop(index))
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        temp = copy.deepcopy(hat)
        draw = temp.draw(num_balls_drawn)
        correct_color = 0
        for color in expected_balls.keys():
            if draw.count(color) >= expected_balls[color]:
                correct_color += 1
        if correct_color == len(expected_balls):
            success += 1
    return float(success) / num_experiments


## Test Case: 
# 
# hat = Hat(blue=3, red=2, green=6)
# probability = experiment(hat=hat, expected_balls={"blue": 2, "green": 1},\
#                          num_balls_drawn=4, num_experiments=1000)
# print(probability) 