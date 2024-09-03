#!/usr/bin/env python3


import re
class MyString:
    def __init__(self, value=''):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value


    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
      
    def is_exclamation(self):
        return self._value.endswith("!")
      
    # import re module
    def count_sentences(self):
      sentences = re.split(r'[.!?]', self._value)
      
      # remove empty strings
      sentences = [sentence for sentence in sentences if sentence.strip()]
      
      # sentence count
      return len(sentences)

    value = property(get_value, set_value)


