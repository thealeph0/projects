import random

def write_grades_to_file(filename):
    random.seed(42)
    with open(filename, 'w') as file:
        grades = [
            str(random.randint(0,100)) for i in range(30)] #creates a list as a string
        file.write(" ".join(grades))
    print("Grades written to file successfully. \n")
    
def read_grades_from_file(filename):
    #Read grades from file and return them as a list of integers"
    try:
        with open(filename, 'r') as f:
            grades = f.read().split()
            return [int(grade) for grade in grades] #returns grades as integers
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    
def display_grades_grid(grades):
    print("Student Grades:")
    for i in range(0,30,6):
        row = grades[i:i+6]
        print(" ".join(f"{grade:3d}" for grade in row))
    print()
    
def generate_summary_report(grades):
    if not grades:
        print("No grades available to report.\n")
        return
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    print("Summary Report: ")
    print(f"Class Average: {average:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest} \n")
    
def main():
    infile = 'student_grades.txt'
    write_grades_to_file(infile)
    
    grades = read_grades_from_file(infile)
    
    display_grades_grid(grades)
    
    generate_summary_report(grades)


main()
    
