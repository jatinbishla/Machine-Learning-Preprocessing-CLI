from data_description import DataDescription
from data_input import DataInput
from imputation import Imputation
from download import Download
from categorical import Categorical
from feature_scaling import FeatureScaling


class Preprocessor:

    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    #Here is the main menu which will be visible to the user
    tasks = [
        '1. Data Description',
        '2. Handling Null Values',
        '3. Encoding Categorical Value',
        '4. Feature Scaling of the Dataset',
        '5. Download the modified dataset'
    ]

    data = 0

    def __init__(self):
        self.data = DataInput().inputFunction()
        print("\n\n" + self.bold_start + "WELCOME TO THE MACHINE LEARNING PREPROCESSING CLI!!!\N {grinning face}" + self.bold_end + "\n\n")
    
    #This function removes the target column of the DataFrame.
    def removeTargetColumn(self):
        print("Columns\U0001F447\n")

        for column in self.data.columns.values:
            print(column, end = " ")

        while(1):
            column = input("\nWhich is the target variable? or press -1 to exit. : ")

            if column == '-1':
                exit()
            choice = input("Are you sure?(y/n) ")

            if choice == 'Y' or 'y':
                try:
                    self.data.drop([column], axis = 1, inplace = True)
                except KeyError:
                    print("No column present with this name. Trye again...... \U0001F974")
                    continue
                print("Done... \U0001F601")
                break
            else:
                print("Try again with the correct column name.\U0001F974")
        return

    def printdata(self):
        print(self.data)

    #Here starts the main function of the preprocessor
    def preprocessorMain(self):
        self.removeTargetColumn()
        
        while(1):
            print("\nTasks \U0001F447\n")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input("\nWhat do you want to do? (press -1 to exit): "))
                except ValueError:
                    print("Integer value required. Try Again.....\U0001F974")
                    continue
                break

            if choice == '-1':
                exit()

            #Here we will move the control to the DataDescription class.
            elif choice == '1':
                DataDescription(self.data).describe()
            
            #Here we will move the control to the Imputation class
            elif choice == '2':
                self.data = Imputation(self.data).imputer()

            #Here we will move the control to the Categorical class
            elif choice == '3':
                self.data = Categorical(self.data).categoricalMain()

            #Here we will move the control to the FeatureScaling class
            elif choice == '4':
                self.data = FeatureScaling(self.data).scaling()
            
            #Here we will move the control to the Download class
            elif choice == '5':
                Download(self.data).download()

            else:
                print("\nWrong integer value. Try Again....\U0001F974")

obj = Preprocessor()

obj.preprocessorMain()
