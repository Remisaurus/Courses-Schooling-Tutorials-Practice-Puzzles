def myFun(*args):
	for arg in args:
		print(arg)

myFun('Hello', 'welcome', 'to', 'class')


def myFun(arg1, *argv):
  print("First argument :", arg1)
  for arg in argv:
    print("Next argument through *argv :", arg)

myFun('Hello', 'welcome', 'to', 'class')


def myFun(arg1, arg2, arg3):
  print("arg1:", arg1)
  print("arg2:", arg2)
  print("arg3:", arg3)

args = ("This", "is", "demo.")
myFun(*args)

kwargs = {"arg1": "This", "arg2": "is", "arg3": "demo."}
myFun(**kwargs)


def myFun(*args, **kwargs):
  print("args: ", args)
  print("kwargs: ", kwargs)

myFun('This', 'is', 'demo.', first="This", mid="is", last="demo.")


def test_function(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

test_function(name="John", age=30)


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Johnson") 


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 



