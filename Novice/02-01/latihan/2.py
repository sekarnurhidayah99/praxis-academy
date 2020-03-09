from _functools import partial, reduce

def add(a, b):
    return a + b

plus = add

plus(3, 4)

(lambda a, b: a + b)(3, 4)  # returns 7

addition = lambda a, b: a + b
addition(3, 4)  # returns 7

authors = ['Octavia Butler', 'Isaac Asimov', 'Neal Stephenson', 'Margaret Atwood', 'Usula K Le Guin', 'Ray Bradbury']
sorted(authors, key=len)  # Returns list ordered by length of author name
sorted(authors, key=lambda name: name.split()[-1])  # Returns list ordered alphabetically by last name.

val = [1, 2, 3, 4, 5, 6]

# Multiply every item by two
print(list(map(lambda x: x * 2, val))) # [2, 4, 6, 8, 10, 12]
# Take the factorial by multiplying the value so far to the next item
print(reduce(lambda x,y:x*y,val,1))

def power(base, exp):
     return base ** exp
cube = partial(power, exp=3)
cube(5)  # returns 125

def retry(func):
    def retried_function(*args, **kwargs):
        exc = None
        for _ in range(3):
            try:
               return func(*args, **kwargs)
            except Exception as exc:
               print("Exception raised while calling %s with args:%s, kwargs: %s. Retrying") % (func, args, kwargs)
               raise exc
            return retried_function

@retry
def do_something_risky():
    ...

retried_function = retry(do_something_risky)