def caching_fibonacci():
    cache = {} # словник для зберігання вже обчислених значень

    def fibonacci(n): # внутрішня рекурсивна функція
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n in cache:
                return cache[n]
            else:
                cache[n] = fibonacci(n - 2) + fibonacci(n - 1) # обчислюємо рекурсивно та зберігаємо результат у кеші
            return cache[n] # повертаємо обчислене значення
    return fibonacci # повертаємо рекурсивну функцію

fib = caching_fibonacci()
print(fib(10))
print(fib(15))