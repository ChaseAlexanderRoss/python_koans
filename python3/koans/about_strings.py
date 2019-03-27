#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, str))
#So I want to make this comment here so I can clarify. I understand what the point of these test are, and am learning neat things about Python, but I don't actually understand how to get the tests to pass. I can read the test name and understand that what you're telling me is that I can make a string with double quotes in it as long as I put single quotes outside it, and vice versa, but I don't understand how to make the tests pass without just copying the original since that's what I have to set it equal to. I don't want to learn how to game tests, I want to learn Python.
    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        new_string = 'He said, "Go Away."'
        self.assertEqual(new_string , string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        this_string = "Don't"
        self.assertEqual(this_string, string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(52, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        self.assertEqual(15, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(True, (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        that_string = """Hello "world\""""
        self.assertEqual(that_string, string)

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual("Hello, world", string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))
