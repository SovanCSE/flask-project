import os




if __name__ == '__main__':
    #This function gives you the name of the operating system dependent module imported
    print(os.name)
    #Get current working directory full path from which directory, you are executing your script.
    print(os.getcwd())
    print(os.path.abspath('.'))
    #get working script file's full directory path.
    print(os.path.dirname(os.path.abspath(__file__)))
    print('oooo', os.path.abspath(__file__))
