## Author: Vinoth D
##def gift():
##    print("transaction successful")
####    return gift

def shopkeeper(fp):
    def wrap(*args,**kwds):
        import time
        start=time.time()
        i=fp(*args,**kwds)
        end=time.time()
        print("time taken for transaction",end-start)
        return i
    
    return wrap
def shopkeeper2(fp):
    def wrap(*args,**kwds):
        print("Function started")
        i=fp(*args,**kwds)
        print('function ended')
        return i
    
    return wrap

        
@shopkeeper2
@shopkeeper
def funcall(a):
    if a>1000:
        print("transaction done")
    else:
        print("transaction failed")
            



    
