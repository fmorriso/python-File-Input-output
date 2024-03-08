import sys
from pathlib import Path
import os

@staticmethod
def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def write_text_file(filename: str) -> None:
    sentences = ['The quick brown fox', 'jumps over the', 'lazy dog.']
    with open(filename, 'w') as f:
        for line in sentences:
            f.write(f'{line}\n')


def read_text_file(filename: str) -> None:
    with open(filename, 'r') as f:
        print(f'{Path(f.name)}')
        while True:
            line: str = f.readline()
            if len(line) == 0:
                break
            else:
                # NOTE: if we want to print() the line, we must either:
                # 1. strip the '\n' off before issuing a regular print()
                #    or
                # 2. use the end='' feature of print
                # otherwise, the output will appear to be vertically double-spaced
                print(line, end='')


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'home path: {Path.home()}')
    print(f'current working directory: {os.getcwd()}')
    filename: str = 'simple.txt'
    full_path: str = f'{Path.home()}\\{filename}'
    print(f'file will be written to {full_path}')
    write_text_file(full_path)
    read_text_file(full_path)
