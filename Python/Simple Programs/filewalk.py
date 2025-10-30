# Count the lines a file that
# contains song lyrics encoded as text.
import os


def main():
    """Open the file. Print out all lines with a line number."""
    print(os.getcwd()) # os already imported above
    file_name = input('Enter file name: ')
    if not os.path.isfile(file_name):
        print(file_name, 'does not exist in the current directory.')
    else:
        file = open(file_name, 'r')
        line = file.readline()
        line_number = 0

        # Print out lines of file with line numbers.
        while line:
            line_number += 1
            print(format(line_number, '4d'), ': ',
                  line.strip(), sep='')
            line = file.readline()
        print('Found', line_number, 'lines.')
        file.close()


def line_count_with():
    """Demonstrate the use of the with statement.

    Ask user for file name and count lines.
    """
    file_name = input('Enter file name: ')
    with open(file_name, 'r') as infile:
        line = infile.readline()
        line_number = 0

        # Print out lines of file with line numbers.
        while line:
            line_number += 1
            print(format(line_number, '4d'), ': ',
                  line.strip(), sep='')
            line = infile.readline()
        print('Found', line_number, 'lines.')
    print('Is file closed?', infile.closed)

main()