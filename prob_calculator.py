import copy
import random


# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for k, v in kwargs.items():
            for i in range(0, v):
                self.contents.append(k)

    def draw(self, no_of_balls):
        removed_balls = list()
        if no_of_balls >= len(self.contents):
            removed_balls = copy.deepcopy(self.contents)
            self.contents.clear()
        else:
            for i in range(0, no_of_balls):
                removed_balls.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_exp = 0
    for i in range(0, num_experiments):
        expected_balls1 = list()
        for k, v in expected_balls.items():
            for j in range(0, v):
                expected_balls1.append(k)
        new_hat = copy.deepcopy(hat)
        actual_balls = new_hat.draw(num_balls_drawn)
        for j in actual_balls:
            if j in expected_balls1:
                expected_balls1.remove(j)
        if len(expected_balls1) == 0:
            successful_exp += 1
    return successful_exp / num_experiments
