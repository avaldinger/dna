import csv
import sys
import pandas as pd

def main():

    # Get the STRs from the CSV header
    list = []

    # Dynamically store the STRs
    matches = {}

    args = len(sys.argv) -1

    # Checking if two files were given
    if args < 2:
        print("Please enter the file names!")
        return 1

    # Storing the file names
    databases =  sys.argv[1]
    sequence = sys.argv[2]
    # print(databases)
    # print(sequence)

    with open(databases, "r") as f:
        reader = csv.reader(f)
        row1 = next(reader)
        # print(row1)
        for row in row1[1:]:
            list.append(row)
        # print(list)
        for elements in list:
            matches[elements] = 0
        # print(matches)



    # Open sequence file
    with open(sequence, "r") as sequence:
        dna = sequence.read()
        print(dna)
        for reps in list:
            countSTR(dna, reps, matches)


    for key in matches:
        print(f"{key}: {matches[key]}")

    # Read file into Dictionary
    with open(databases, "r") as database:
        reader = csv.DictReader(database)
        identified = False
        for row in reader:
            count = 0
            for key in matches:
                if int(row[key]) == int(matches[key]):
                    count += 1
                    if count == len(matches):
                        print(f"Suspect found: {row['name']}")
                        identified = True
        if identified == False:
            print("No Match")


# Count STRs in the sequence
def countSTR(sequence, repeats, matches):
    i = 0
    j = len(repeats)
    # print(f"{repeats}: {j}")
    tandem = 0
    # print(f"STR: {repeats}")
    numberOfSTRs = 0
    while (i+len(repeats)) <= len(sequence):
        temp = sequence[i:j]
        # print(i, end="")
        # print(temp)
        if temp == repeats:
            tandem = 0
            match = True
            x = i + len(repeats)
            y = j + len(repeats)
            # print(x, y)
            tandem += 1
            # print(f"Found: {temp}")
            # Checking the following DNA code
            while(match):
                window = sequence[x:y]
                # print(f"Window: {window}")
                if window == repeats:
                    tandem += 1
                    # print(f"if true: {tandem}")
                    x = x + len(repeats)
                    y = y + len(repeats)
                else:
                    match = False

            if tandem > numberOfSTRs:
                numberOfSTRs = tandem
                # print(tandem)
            # increment the value for the matched STR
            matches[repeats] = numberOfSTRs
        i += 1
        j += 1


if __name__ == "__main__":
    main()