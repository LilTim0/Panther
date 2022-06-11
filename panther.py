'''
 >>> Code by Lil_Tim
 >>> Panther Ransomware
'''

import os

class Ransomware:
    '''
    This class is a ransomware instance (for education purposes only)
    '''
    def __init__(self,start_file:str=None,encryption_key:str=None,max_infections:int=0,number_of_infections:int=1):
        
        print('>>> Ransomware initialized...')
        self.file_list = []
        self.start_file = start_file
        self.encrypt_key = encryption_key
        self.max_infect = max_infections
        self.number_of_infect = number_of_infections
        
    def get_parameters(self):
        print(self)
        print(self.start_file)
        print(self.encrypt_key)
        print(self.max_infect)
        print(self.number_of_infect)