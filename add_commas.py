# import required module
import os

# Assign variables
directory = 'tweets'
tweets_proccessed = 0
 
# Iterate over files in tweets directory, checking each file
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # If the path is a file
    if os.path.isfile(f):

        # Open file and read the induvidual lines
        with open(f, 'r', encoding="utf8") as file:
            # read a list of lines into data
            data = file.readlines()

        # For each line, replace the 'newline' with ',newline', except if it's the last line
        for i, row in enumerate(data):
            if i != len(data)-1:
                data[i] = row.replace("\n", ",\n")


        # Add bracket to start of file and ending
        data.insert(0, '[')
        data.append(']')


        # Write everything back to orignal file
        with open(f, 'w', encoding="utf8") as file:
            file.writelines( data )