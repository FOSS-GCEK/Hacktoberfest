#!/usr/bin/env python3

def main():
    for i in range(1, 101): 
        print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i))

if __name__ == '__main__':
    main()
