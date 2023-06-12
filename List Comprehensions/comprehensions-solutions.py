# Complete the following list comprehensions. Use the assertions to verify the code is working correctly.

# 1. In the function cubed, take the list and create a list comprehension that will cube each number in the list.
def cubed(my_list):
    return [item ** 3 for item in my_list]


assert cubed([1, 2, 3, 4, 5]) == [1, 8, 27, 64, 125]
assert cubed([25, 3, 9, 21, 55]) == [15625, 27, 729, 9261, 166375]


# 2. In the function convert_to_string, take the list as a parameter, and convert each item in the list to a string
def convert_to_string(my_list):
    return [str(item) for item in my_list]


assert convert_to_string([1, 5, 2, 3, 7, 22343]) == ['1', '5', '2', '3', '7', '22343'];
assert convert_to_string([323334, "Hello", True, False, 3.14159]) == ['323334', 'Hello', 'True', 'False', '3.14159']


# 3. In the function is_div_11, from the given list create a list using list comprehension that
# contains only numbers divisible by 11
def is_div_11(my_list):
    return [item for item in my_list if item % 11 == 0]


assert is_div_11([1, 7, 11, 22, 23, 33, 50, 55]) == [11, 22, 33, 55]


# 4. Given a dictionary of integers to integers, return the list of keys whose values are even.
# Note: I found you have to use the items() or keys function. It won't let you iterate directly on the dictionary.

def comp4(my_dict):
    return [key for key, value in my_dict.items() if value % 2 == 0]


assert comp4({4: 5, 3: 4, 6: 88, 90: 78, 23: 23, 21: 46}) == [3, 6, 90, 21]


# 5. Given a tuple of strings.  Make a list of the strings from the tuple whose length is 5.
# In the first assert, note that the length (or number of characters) of three, seven, and eight is 5
def list_of_5(my_tuple):
    return [item for item in my_tuple if len(item) == 5]


assert list_of_5(("three", "four", "five", "six", "seven", "eight", "ten")) == ["three", "seven", "eight"]
assert list_of_5(('then', 'she', 'looked', 'at', 'the', 'sides', 'of', 'the', 'well', 'and', 'noticed', 'that',
                  'they', 'were', 'filled', 'with', 'cupboards', 'and', 'book-shelves', 'here', 'and', 'there',
                  'she', 'saw', 'maps', 'and', 'pictures', 'hung', 'upon', 'pegs')) == ["sides", "there"]

# bonus - Create list comprehension that finds the product of adjacent elements in a tuple
def tuplipy(my_typle):
    return tuple([my_typle[i] * my_typle[i + 1] for i in range(len(my_typle) - 1)])

assert tuplipy((1, 2, 3, 4, 5, 6, 7)) == (2, 6, 12, 20, 30, 42)
assert tuplipy((2, 4, 6, 8)) == (8, 24, 48)
assert tuplipy((36, 4)) == (144,)
