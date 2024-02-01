import time  
def log(func): 
    def wrapper(*args,**kwargs): 
        print(f"Logging: {func.__name__} called")
    return wrapper 
def timer(func): 
    def wrapper(*args,**kwargs): 
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"Time taken:{end_time-start_time} seconds")
        return result
    return  wrapper

@timer 
@log 
def example_function(): 
    print("Ececuting example_function")
example_function()
print(example_function)
