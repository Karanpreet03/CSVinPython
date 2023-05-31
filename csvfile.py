import csv
# opening and reading a csv file
csv_file = open("student_table.csv" , 'r')
# create an array type variable for reading the csv file
for line in csv_file:
    print(line)
    # printing the file as the desired output
csv_file.close()
csv_file = open("student_table.csv", 'a')
writer = csv.writer(csv_file ,delimiter = ',')
writer.writerow(['Jaspreet','singh','444'])
csv_file.close()
# Exercise
# Write a function that takes two files as the parameter that are the names of the files
# The function needs to copy the content of one file to another

def functionCopy(source, destination):
        srcFile = open(source, 'r')
        destFile = open(destination, 'w')
        for lines in srcFile:
            destFile.write(lines)
            print(lines)
functionCopy("student_table.csv","destination.csv")
# Dictionary file
csv_file = open("student_table.csv","w")
writer = csv.DictWriter(csv_file, ["first_name","last_name","ID"])
writer.writeheader()
writer.writerow({"first_name":"Karanpreet","last_name":"Sachdeva","ID":"111"})
csv_file.close()