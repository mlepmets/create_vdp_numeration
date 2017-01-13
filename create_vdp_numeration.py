"""create_vdp_numeration.py - create .csv file to be used with
Adobe InDesign "Data Merge" feature."""

import sys

try:
    file_name = input('File name?: ')
    csvfile = open(file_name, 'w')

    csvfile.write('number')

    """For duplex print jobs create an additional column in the csv file called
    "dummy" which will later be assigned to a page without numeration."""
    two_sides = input('Duplex? (y/n) ')
    if two_sides.lower() == 'y':
        csvfile.write(',dummy')
    csvfile.write('\n')

    # get user input for the number start and end of the sequence of numbers
    start = int(input('Start of seq.: '))
    end = int(input('End of seq.: '))

    # loop from start to end number, write to file
    if start.isnumeric() and end.isnumeric():
        for i in range(start, end + 1):
            csvfile.write(str(i) + '\n')
    else:
        sys.exit('Must enter numbers for sequence')
    csvfile.close()

except IOError as e:
    sys.exit(str(e))
except OSError as e:
    sys.exit(str(e))
