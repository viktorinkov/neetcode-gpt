class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x_old = x_new = init
        for i in range(iterations):
            x_new = x_old - learning_rate * 2 * x_old
            x_old = x_new

        return round(x_old, 5)