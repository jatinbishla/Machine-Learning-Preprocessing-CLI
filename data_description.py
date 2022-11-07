import pandas as pd

class DataDescription:

    #Tasks for Data Description
    tasks = [
        '\n1. Describe a specific column',
        '2. Show properties of each column',
        '3. Show the Dataset'
    ]

    def __init__(self,data):
        self.data = data

    #Fuction to print the whole data set
    def showDataset(self):
        while(1):
            try:
                rows = int(input("\nHow many rows want to print? or press -1 to go back.: "))
                if rows == -1:
                    break
                if rows <= 0:
                    print("Number of rows given must be +ve....\U0001F974")
                    continue
                print(self.data.head(rows))
            except ValueError:
                print("\nNumeric value is required. Try Again.....\U0001F974")
                continue
            break
        return

    #Function to print the columns
    def showColumns(self):
        for column in self.data.columns.values():
            print(column, end=' ')
    
    #Fuction for describing dataset or any specific column
    def describe(self):
        while(1):
            print("\nTasks (Data Description)......\U0001F974")
            for task in self.tasks:
                print(task)
            
            while(1):
                try:
                    choice = int(input("\nWhat do you want to do? or press -1 to go back.: "))
                except ValueError:
                    print("Integer value required. Try Again.....\U0001F974")
                    continue
                break
            
            if choice == -1:
                break
            
            elif choice == 1:
                self.showColumns()
                while(1):
                    describecolumn = input("\n\nWhich column? ").lower()
                    try:
                        print(self.data[describecolumn].describe())
                    except KeyError:
                        print("\nNo column present with this name. Try Again....\U0001F974")
                        continue
                    break
            
            elif choice == 2:
                print(self.data.describe())
                print("\n\n")
                print(self.data.info())

            elif choice == 3:
                self.showDataset()

            else:
                print("\nWrong integer value entered. Try Again....\U0001F974")