import csv


def createBitMap(inputFileName, outputFileName):

    ageBin = ["1000000000", "0100000000", "0010000000", "0001000000", "0000100000",
              "0000010000", "0000001000", "0000000100", "0000000010", "0000000001"]

    # Open output file for writing
    outputFile = open(outputFileName, "w")

    # Open the file using csv
    with open(inputFileName) as csvFile:
        unsortedFile = csv.reader(csvFile, delimiter=',')

        for row in unsortedFile:

            # Variables to store row data
            bitMapString = ""
            animal = row[0]
            age = int(row[1])
            adopted = row[2]

            #print(animal, age, adopted)

            # Check for Anmimals and convert to binary
            if(animal == "cat"):
                bitMapString = bitMapString + "1000"
            elif(animal == "dog"):
                bitMapString = bitMapString + "0100"
            elif(animal == "bird"):
                bitMapString = bitMapString + "0001"
            elif(animal == "turtle"):
                bitMapString = bitMapString + "0010"

            # Convert the age based on the age bin binary
            if(0 <= age <= 10):
                bitMapString += ageBin[0]
            elif(11 <= age <= 20):
                bitMapString += ageBin[1]
            elif(21 <= age <= 30):
                bitMapString += ageBin[2]
            elif(31 <= age <= 40):
                bitMapString += ageBin[3]
            elif(41 <= age <= 50):
                bitMapString += ageBin[4]
            elif(51 <= age <= 60):
                bitMapString += ageBin[5]
            elif(61 <= age <= 70):
                bitMapString += ageBin[6]
            elif(71 <= age <= 80):
                bitMapString += ageBin[7]
            elif(81 <= age <= 90):
                bitMapString += ageBin[8]
            elif(91 <= age <= 100):
                bitMapString += ageBin[9]

            # Convert True and False into binary
            if(adopted == "True"):
                bitMapString += "10"
            elif(adopted == "False"):
                bitMapString += "01"

            bitMapString += "\n"

            outputFile.write(bitMapString)

    outputFile.close()


def sortFile(filename):
    sortedData = sorted(open(filename).read().split('\n'))
    f = open("animals_sorted.txt", "w")
    for row in sortedData:
        if row != "":
            data = row + "\n"
            f.write(data)

    f.close()

def wah32Compress(inputFile, ):



def main():

    sortedInput = "animals_sorted.txt"
    sortedBitMap = "animalsBit_sorted.txt"
    unsortedInput = "data/animals_test.txt"
    unsortedBitMap = "animalsBit_unsorted.txt"

    createBitMap(unsortedInput, unsortedBitMap)
    sortFile(unsortedInput)
    createBitMap(sortedInput, sortedBitMap)


if __name__ == "__main__":
    main()
