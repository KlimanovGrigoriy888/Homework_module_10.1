from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
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
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    my_function(2, 3)

