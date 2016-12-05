# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].

def even_elements(input_list):
    if type(input_list) == list:
        return [input_list[i] for i in range(len(input_list)) if i % 2 == 1]
    else:
        raise TypeError
