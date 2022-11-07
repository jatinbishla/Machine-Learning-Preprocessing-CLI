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
    def 