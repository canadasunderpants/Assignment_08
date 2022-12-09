#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# jdenhaan, 2022-Dec-4, added code to complete assignment 08
#------------------------------------------#

import pickle 

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        ID: (int) with CD ID
        Title: (string) with the title of the CD
        Artist: (string) with the artist of the CD
    methods:

    """
    # TODONE Add Code to the CD class
    
    # -- Fields -- #
    ID = ''
    Title = ''
    Artist = ''
    
    # -- Constructor -- #
    def __init__(self, I, T, A):
        self.__ID = I
        self.__Title = T
        self.__Artist = A
    
    def disp (self, ID, Title, Artist):
        return '{}\t{} (by:{})'.format(self.ID, self.Title, self.Artist)
    
    # -- Properties -- #
    #getters
    @property
    def ID(self):
        return self.__ID
    @property
    def Title(self):
        return self.__Title
    @property
    def Artist(self):
        return self.__Artist
    
    #setters
    @ID.setter
    def set_ID(self, value):
        if str(value).isnumeric():
            self.__ID = value
        else:
            raise Exception ('the ID must be numeric')
    
    @Title.setter    
    def set_Title(self, value):
        if str(value).isalnum():
            raise Exception('title cannot be a number')
        if value == '':
            raise Exception ('title cannot be blank')
        else:
            self.__Title = value
    
    @Artist.setter    
    def set_Artist(self, value):
        if value == '':
            raise Exception ('Artist cannot be blank')
        else:
            self.__Artist = value
        
    # -- Methods -- #


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:
        

    properties:

    methods:
        write_file(file_name, table): -> None
        read_file(file_name): -> (a list of CD objects)

    """
    # TODONE Add code to process data from a file
    @staticmethod
    def read_file(file_name):
        """Function to manage data ingestion from a binary file to a list of objects

        Reads the data from file identified by file_name into a 2D table
        (list of objects) table one line in the file represents one object in the table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            Table: 
        """
        lstOfCDObjects.clear()  
        try:
            with open (file_name, 'rb') as fileObj:
                table = pickle.load(fileObj)  
        except FileNotFoundError as e:
            print('that file does not exist')
            print(e)
            print('Let me create that file for you!')
            fileNew = open(file_name, 'wb')
            fileNew.close()
            print('The file {} has now been created'.format(file_name))
        except Exception as e:
            print('General Error!')
            print(e.__doc__)
        return table
        
     # TODONE Add code to process data to a file
    @staticmethod
    def write_file(file_name, table):
        """
        writes data entered by user to a binary file for permanent storage

        Args:
            file_name (string): name of file to write data to
            table (list of objects):2D data structure (list of objects) that holds the data during runtime,
            holds data to be written to file

        Returns
            None.

        """
        try:
            with open(file_name, 'wb') as fileObj:
                pickle.dump(table, fileObj)
        except Exception as e:
            print('General Error!')
            print(e.__doc__)
            

# -- PRESENTATION (Input/Output) -- #
class IO:
    """ Main input/output class of functions. Gives users choices and accepts their inputs. Displays current 
    inventory"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
        
    # TODONE add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def CD_IO():
        """Gets user input for a new CD

        Args:
            None.

        Returns:
            ID, Artist, Title (strings):a tuple of CD info that is used to populate a new CD object instance

        """
        
        ID = input('id:')
        Artist = input('artist:')
        Title = input('title:')
        return (ID, Artist, Title)
    
    
    # TODONE add code to get CD data from user 
    @staticmethod
    def AddCD(new_cd, table):
        """Gets user input for a new CD

        Args:
            new_cd: a tuple containg ID, Artist and Title 
            table: list of objects containing CD info, function appends a new object to this table

        Returns:
            table (list of objects):a list of CD objects with the latest CD appended to it. 

        """
        new_cd = CD(ID, Artist, Title)
        table.append(new_cd)
        return table

    
    # TODONE add code to display the current data on screen
    @staticmethod
    def ShowCD(table):
        """displays current inventory for user

        Args:

            table: list of objects containing CD info

        Returns:
            none. 

        """
        for cd in table:
            print('{}\t{} (by: {})'.format(cd.ID, cd.Artist, cd.Title))
    
# -- Main Body of Script -- #
while True:
    IO.print_menu()
    print('Current Inventory: ')
    IO.ShowCD(lstOfCDObjects)
    strChoice = IO.menu_choice()
    
    if strChoice == 'x':
        print('program ending. . .')
        break
    if strChoice == 'l':
        print('Warning: If you continue, all unsaved data will be lost and the inventory re-loaded from file.')
        strYesNo = input('type\'yes\' to continue and reload from file. Otherwise reload will be cancelled. ')
        if strYesNo.lower() == 'yes':
            print('Reloading. . .')
            lstOfCDObjects = FileIO.read_file(strFileName)
            IO.ShowCD(lstOfCDObjects)
        else:
            input('Canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            continue
    elif strChoice == 'a':
        ID, Artist, Title = IO.CD_IO()
        NewCD = ID, Artist, Title
        IO.AddCD(NewCD, lstOfCDObjects)
        IO.ShowCD(lstOfCDObjects)
    elif strChoice == 'i':
        IO.ShowCD(lstOfCDObjects)
    elif strChoice == 's':
        IO.ShowCD(lstOfCDObjects)
        strYesNo = input('save this inventory to file? [y/n]').strip().lower()
        if strYesNo == 'y':
            FileIO.write_file('cdInventory.txt', lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [Enter] to return to the menu.')
        continue
    else:
        print('General Error')