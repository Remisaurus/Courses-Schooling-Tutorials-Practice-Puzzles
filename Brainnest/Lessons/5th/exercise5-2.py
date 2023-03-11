def authorize(func):
    def the_return():
        if not check_if_authorized(True):
            print('unauthorized access')
        else:
            print('here is your information:')
            func()
    return the_return
        
def check_if_authorized(boolean):
    return boolean
        
@authorize
def secret_data():
    print("11010001010100001")


secret_data()
        

'''
2.
write a function called authorize(func)
define a wrapper (func inside another func) inside and return
"Unathorized access" if not authorized.
define another function to check whether authorized or not. (True or False)
define the last function named secret_data() 
to say "This is confidential data" if user is authorized.
By calling secret_data you should see if the data is confidential or 
you will provoke the other function that says "Unauthorized access".
'''