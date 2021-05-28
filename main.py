Python Developer notes
10 May 2021 
________________________________________
# Create a dictionary in a list with specific key and value pair

import itertools as it
headers = [("AlbumId", "AlbumId"), ("ArtistId", "ArtistId"), ("Title", "Title")]
table_headers = []

for i, j in headers:
    t = ("text", i, "value", j)
    table_headers.append(dict(it.zip_longest(*[iter(t)] * 2, fillvalue="")))

print(table_headers)

# Create a dictionary from two lists using zip function

list1 = ['karl', 'lary', 'keera']
list2 = [28934, 28935, 28936]

dict0 = dict(zip(list1, list2))

print(dict0)

# Check if given number is prime

def is_prime(n):
    if n <= 1 or n % 1 > 0:
        return n, print(n, "is not a prime number")
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return n, print(n, "is not a prime number")
    print('\x1b[6;30;42m' + f"{str(n)}" + '\x1b[0m' + " is prime number")

# Find factorial of given number

def factorial(n):
    if n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

# Floating text message

import sys
import time
import datetime

msg1 = '\x1b[6;30;42m' + 'Success!' + '\x1b[0m'
msg2 = '\x1b[6;37;41m' + 'Warning!' + '\x1b[0m'
msg3 = '\x1b[6;30;43m' + 'Caution!' + '\x1b[0m'

def floating(text=msg2, step=175, of=5, c=" "):
    while True:
        for i in range(step):
            # print("\r{0}{1}".format(char*i, text), end="")
            sys.stdout.write("\r{0}{1}".format(c*i, text))
            sys.stdout.flush()
            time.sleep(1 / 2**of)
        print()
        break

floating()
answer = input("All your files will be deleted [y/N]: ")
if answer == "y":
    floating(text=msg1)
elif answer.isdigit():
    floating(text=msg3)
else:
    print("good bye!")

# Highlight an element with selenium

def highlight(self, driver, element, effect_time, color, border):
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    self.take_screenshot(driver)
    time.sleep(effect_time)
    apply_style(original_style)

# Take a screenshot of a web site

def take_screenshot(self, driver):
    filename = datetime.datetime.now().strftime("%d.%B.%Y-%H%M%S")
    driver.save_screenshot(r"Screenshots\{}.png".format(filename))

# Fahrenheit to celsius and celsius to fahrenheit temperature converter

def to_fahrenheit(c):
    return 9 / 5 * c + 32

def to_celsius(f):
    return (f - 32) * 5 / 9
  
celsius_temps = [25, 32, 40]
print(list(map(to_fahrenheit, celsius_temps)))

# Decode and encode given message

def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))

def decode_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if c not in alphabet:
        return c
    rotated_pos = ord(c) - rot_by
    # If the rotation is inside the alphabet
    if rotated_pos >= ord(alphabet[0]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos + len(alphabet))
    
print("".join(map(rotate_chr, "My secret message goes here.")))
print("".join(map(decode_chr, "pb vhfuhw phvvdjh jrhv khuh.")))
print("".join(map(decode_chr, "fxqhbg jxowhnlq ndbd")))

# Making list from a string and removing unwanted char 
def str_to_list(text):
    unwanted_dict = {54: 32, 55: 32, 56: 32, 57: 32}
    return list(text.translate(unwanted_dict).replace(" ", ""))

def str_to_list_with_none(text):
    unwanted_dict = {54: None, 55: None, 56: None, 57: None}
    return list(text.replace(" ", "").translate(unwanted_dict))

# Put underscore for long number

"""
print(a[0:f] + "_" + a[f:f+3] + "_" + a[f+3:f+6] + "_" + a[f+6:f+9] + "_" + a[f+9:f+12])
"""

def factorial(n):
    if n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

def under_scorer(char="_", step=3):
    return char.join(a[i:i + step] for i in range(len(a) % 3, len(a), step))

for j in range(33):
    a = str(factorial(j))
    if len(a) % 3 == 0:
        print(j, "=>", under_scorer())
    else:
        if len(a) > 3:
            res = a[0:len(a) % 3] + "_" + under_scorer()
            print(j, "=>", res)

# The multiplication table

for i in range(1, 11):
    for j in range(1, 11):
        print('|{0:2d} * {1:2d} = {2:3d}'.format(j, i, j*i), end=" |")
    print("")

# Making three dots moving effect continuously

import sys
import time

def three_dots():
    print("Calling", end="")
    loading = True
    loading_speed = 1
    loading_string = "." * 3
    while loading:
        for index, char in enumerate(loading_string):
            sys.stdout.write(char)  # write the next char to STDOUT
            sys.stdout.flush()  # flush the output
            time.sleep(1.0 / loading_speed)  # wait to match our speed
            index += 1  # lists are zero indexed, we need to increase by one for the accurate count
        sys.stdout.write("\b" * index + " " * index + "\b" * index)
        sys.stdout.flush()  # flush the output

three_dots()

# Class definition and example 

from typing import Optional

class Position:
    MIN_LATITUDE = -90
    MAX_LATITUDE = 90
    MIN_LONGITUDE = -180
    MAX_LONGITUDE = 180

    def __init__(self, longitude: float, latitude: float, address: Optional[str] = None):
        self.longitude = longitude
        self.latitude = latitude
        self.address = address

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float) -> None:
        if not (Position.MIN_LATITUDE <= latitude <= Position.MAX_LATITUDE):
            raise ValueError(f"latitude was {latitude}, but has to be in [-90,90]")
        self._latitude = latitude

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float) -> None:
        if not (Position.MIN_LONGITUDE <= longitude <= Position.MAX_LONGITUDE):
            raise ValueError(f"longitude was {longitude}, but has to be in [-180,180]")
        self._longitude = longitude


pos1 = Position(49.0127913, 8.4231381, "Elm Street")
pos2 = Position(42.1238762, 9.1649964)

# Fibonacci example

import sys

table = [0]*1000

def fast_fib(n):
    if n <= 1:
        return n
    else:
        if table[n-1] == 0:
            table[n-1] = fast_fib(n-1)
        if table[n-2] == 0:
            table[n-2] = fast_fib(n-2)
        table[n] = table[n-1] + table[n-2]
        return table[n]

def main():
    print('Enter a number : ')
    num = int(sys.stdin.readline())
    print(fast_fib(num))


if __name__ == '__main__':
    main()

# Datetime example with object creation with regex control

import datetime
import re

class Human(object):
    def __init__(self, initial, second, last, birthday, country):
        self.initial = initial
        self.second = second
        self.last = last
        self.birthday = birthday
        self.country = country
        self.age = 0

    def __str__(self):
        full_name = self.initial + " " + self.second + " " + self.last
        print(f"Hello {full_name}!, You are {int(self.age)} years old. You are from {self.country}")

    def age_calculator(self, year):
        now = datetime.datetime.now()
        birth_day = datetime.datetime(int(year[0]), int(year[1]), int(year[2]), 0, 0, 0)
        delta_in_milliseconds = (now - birth_day).total_seconds()

        age = ((((delta_in_milliseconds / 60) / 60) / 24) / 365)
        days = (((delta_in_milliseconds / 60) / 60) / 24)
        hours = ((delta_in_milliseconds / 60) / 60)
        seconds = (delta_in_milliseconds / 60)
        print(int(age), "years")
        print(int(days), "days")
        print(int(hours), "hours")
        print(int(seconds), "seconds")
        print(int(delta_in_milliseconds), "milliseconds")
        self.age = age

    def regex_control(self, birthday):
        while True:
            result = re.search("^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)"
                      "([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])"
                      "$|^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)"
                      "([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$", birthday)
            if result.string:
                c = ["/", "-", "."]
                char = [char for pos, char in enumerate(result.string) if char in c]
                return self.age_calculator(result.string.split(char[0]))

if __name__ == '__main__':
    h1 = Human("Ali", "Veli", "Küp", "1980/1/1", "Turkey")
    h1.regex_control(h1.birthday)
    h1.__str__()

# Check if file exists 

from os import path

def check_for_file():
    print("File exists: ", path.exists("source.txt"))

if __name__ == "__main__":
    check_for_file()
