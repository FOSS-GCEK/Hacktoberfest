#!/usr/bin/env python3

def main():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    
    print(f'{fahrenheit:.2f} Fahrenheit is {celsius:.2f} Celsius')

if __name__ == '__main__':
    main()
