# declaring a function
def myFunction(arg):
  print(arg)

a = 1
myFunction(a)


# default argument values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
  while True:
    ok = input(prompt)
    
    if ok in ('y', 'ye', 'yes'):
      return True
    
    if ok in ('n', 'no', 'nop', 'nope'):
      return False
    
    retries = retries - 1
    
    if retries < 0:
      raise ValueError('invalid user response')
    
    print(reminder)

"""
The default value is evaluated only once. This makes a difference when 
the default is a mutable object such as a list, dictionary, or instances 
of most classes. For example, the following function accumulates the arguments 
passed to it on subsequent calls:
"""
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# arbitrary argument lists
"""
  ***keywords = keyword1=value1, keyword2=value2
"""
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# unpack arguments lists
list(range(3, 6))            # normal call with separate arguments
# output = [3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
# output = [3, 4, 5]