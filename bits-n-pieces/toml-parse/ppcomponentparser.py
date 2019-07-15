#!/usr/bin/env python3

import toml
import os

class PPResistor(object):
    def __init__(self):
        # Define empty values for all the required parameters. 
        # There is a difference between info that is required for the part
        # and info that is required in the TOML file since some things, like
        # physical dimentions, can be inferred from the footprint. Maybe 
        # have some kind of overlay? Or have a class to provide those pieces?
        self._name = ''
        self._generic = True
        self._symbolfile = ''
        self._footprintfile = ''
        self._package = ''

    def __init__ (self, filename):
        self.rawdict = 

    def read_toml(self, filename):
        self.rawdict = read(filename)

    def main(self):
        print('sup\n')

if __name__ == '__main__':
    # Read in a list of files from stdin and print their contents
    PPResistor().main()

#with open('RES_10k_0.1%_63mW_0402_Thin_50ppm_-55-155C.toml', 'r') as cmpfile:
#    parsed_toml = toml.loads(cmpfile.read())

#new_toml_string = toml.dumps(parsed_toml)
#print(new_toml_string)

