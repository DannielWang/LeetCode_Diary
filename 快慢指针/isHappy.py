class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum


        turtle = n
        rabbit = get_next(n)
        while rabbit != 1 and turtle != rabbit:
            turtle = get_next(turtle)
            rabbit = get_next(get_next(rabbit))
        return rabbit == 1

