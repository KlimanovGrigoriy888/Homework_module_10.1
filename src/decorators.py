from functools import wraps


def log(filename: str = None) -> None:
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("my_function ok\n")
                else:
                    print("my_function ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"my_function error: {e}. Inputs: {args}, {kwargs}")
                # raise e

        return inner

    return wrapper


if __name__ == "__main__":

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(2, 0)
