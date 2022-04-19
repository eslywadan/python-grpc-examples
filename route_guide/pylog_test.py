from typing import Generator

def isEven(i: int) -> Generator[None, None, None]:
    if i % 2 == 0:
        print(f'{i}-even', end = ', ')
        yield 
    else:
        print(f'{i}-odd', end = ', ')

evens = [i for i in range(10) for _ in isEven(i)]

print(f'\n{evens}')