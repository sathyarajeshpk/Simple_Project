def my_decorator(fx):
    def mainfunc(*args, **kwargs):
        print("Before calling the function...")
        result = fx(*args, **kwargs)
        print("After calling the function...")
    return mainfunc
