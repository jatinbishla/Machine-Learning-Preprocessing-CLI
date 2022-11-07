from os import path
import sys
import pandas as pd

class DataInput():

    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    #extensions supported are to be entered here
    supported_file_extensions = [
        '.csv',
    ]

    #Function to covert column names into lowercase
    def change_to_lower_case(self,data):
        for column in self.data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)
        return data

    #stating all the possible errors and reading the csv file
    def inputFunction(self):
        try:
            filename, file_extension = path.splitext(sys.arg[1])
            if file_extension == "":
                raise SystemExit(f"Provide the " + self.bold_start + "DATASET" + self.bold_end + "name (with extension) \U0001F643")

            if file_extension not in self.supported_file_extensions:
                raise SystemExit(f"This file extension is not " + self.bold_start + "supported. \U0001F643" + self.bold_end)
            
        except IndexError:
            raise SystemExit(f"Provide the " + self.bold_start + "DATASET" + self.bold_end + "name (with extension). \U0001F643")
        

        try:
            data = pd.read_csv(filename+file_extension)
        
        except pd.errors.EmptyDataError:
            raise SystemExit(f"The file is" + self.bold_start + "EMPTY" + self.bold_end + "\U0001F635")

        except FileNotFoundError:
            raise SystemExit(f"The file " + self.bold_start + "DOESN'T" + self.bold_end + "exists. \U0001F635")
        
        data = self.change_to_lower_case(data)

        return data