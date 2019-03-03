# JT Mundi
# CS 351
# 03-02-2019

import csv
from itertools import groupby

# Generate bitmap for input file and write to ouput to specified
# output file name
def createBitMap(inputFileName, outputFileName):

    # Age bin for 0-100 age domain for animals
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

            # Turncate with new line and write to file
            bitMapString += "\n"
            outputFile.write(bitMapString)

    # close output file
    outputFile.close()

# Sort the text file


def sortFile(filename):

    # Split the data tuples on new lines
    sortedData = sorted(open(filename).read().split('\n'))

    # Open a new file for sorted output
    f = open("./output/animals_sorted.txt", "w")

    # Sort the data write to file
    for row in sortedData:
        if row != "":
            data = row + "\n"
            f.write(data)

    # Close the ouput file
    f.close()


# Compression on provided input file and name of the output file and bit size 32 or 64
def compression(inputFile, outputFile, bitSize):

    fillCount = 0
    litCount = 0

    # Open file for writing
    compressedFile = open(outputFile, "w")

    # Create a bit array of the input file removing new lines
    cleanTuples = [line.rstrip('\n') for line in open(inputFile)]

    # For the 16 column bits run a loop compressing each column
    for a in range(0, 16):
        WAHCompress(cleanTuples, compressedFile, a,
                    bitSize, fillCount, litCount)

    # Close the compressed file
    compressedFile.close()


# Using wah compressing compress the file
def WAHCompress(cleanTuples, compressedFile, a, sizeBit, fillCount, litCount):

    # Mark a run with 1
    runFlag = "1"

    # Mark a literal with 0
    litFlag = "0"

    # Count the bits for runs
    bitCount = 0

    # String to write to file
    bitString = ""

    # Iterate the columsn by converting into a list
    for x in cleanTuples:
        chunk = list(x[a])

        # Create a chunck and count bits iterated
        for y in chunk:
            bitString += y
            bitCount += 1

            # Break with comma if the bit size is reached
            # and reset bit count to zero
            if bitCount == sizeBit - 1:
                bitString += ","
                bitCount = 0

    # Strip the comma and create a list
    bitList = [x.strip() for x in bitString.split(',')]

    # Group the bitlist into segment
    segment = [(k, sum(1 for i in g)) for k, g in groupby(bitList)]

    # Iterate the segment
    for x in segment:
        newSeg = x[0]
        runCount = "{0:b}".format(x[1])

        # max length for runs based on specifed size
        maxLen = (sizeBit - 2) - len(runCount)

        # Runs
        if newSeg.count(newSeg[0]) == len(newSeg) and len(newSeg) == (sizeBit - 1):
            compressedFile.write(runFlag)
            compressedFile.write(newSeg[0])

            for i in range(0, maxLen):
                compressedFile.write(litFlag)
            compressedFile.write(runCount)

        # Literals
        else:
            compressedFile.write(litFlag)
            compressedFile.write(newSeg)

    # Turncate with newline
    compressedFile.write("\n")


def main():

    # File names for ouput and input
    sortedBitMap = "./output/animals_bitmap_sorted.txt"
    sortedAnimals = "./output/animals_sorted.txt"

    unsortedAnimals = "./data/animals.txt"
    unsortedBitMap = "./output/animals_bitmap.txt"

    sortedWAH32 = "./output/animals_compressed_sorted_32.txt"
    unsortedWAH32 = "./output/animals_compressed_32.txt"

    sortedWAH64 = "./output/animals_compressed_sorted_64.txt"
    unsortedWAH64 = "./output/animals_compressed_64.txt"

    # Create bit map on unsorted file
    createBitMap(unsortedAnimals, unsortedBitMap)

    # Sort the file
    sortFile(unsortedAnimals)

    # Create bit map on sorted file
    createBitMap(sortedAnimals, sortedBitMap)

    # Compress sorted and unsorted using 32 WAH
    compression(sortedBitMap, sortedWAH32, 32)
    compression(unsortedBitMap, unsortedWAH32, 32)

    # Compress sorted and unsorted using 64 WAH
    compression(sortedBitMap, sortedWAH64, 64)
    compression(unsortedBitMap, unsortedWAH64, 64)


if __name__ == "__main__":
    main()
