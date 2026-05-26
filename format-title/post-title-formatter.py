#!/usr/bin/env python3
import sys

def post_title_formatter(input_string):
    """
    Converts a string to lowercase and replaces spaces with hyphens.
    """
    return input_string.lower().replace(' ', '-')

if __name__ == "__main__":
    input_string = input("Please enter the title of your post:")
    print(post_title_formatter(input_string))
