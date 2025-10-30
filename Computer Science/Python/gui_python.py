import tkinter as tk
from tkinter import messagebox, filedialog
import random
import threading
##This program is a Student Selection GUI Program
##Requires a file containing the student names and
##the program will randomly select a student based 
##on on-screen parameters/controls

class StudentSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Selector")
        
        # Variables
        self.students = []
        self.remaining_students = []
        self.auto_reset_enabled = tk.BooleanVar()
        self.reset_time = tk.IntVar(value=30)
        self.timer_thread = None
        
        # GUI Components
        self.setup_gui()
    
    def setup_gui(self):
        # Buttons
        tk.Button(self.root, text="Load Students", command=self.load_students).pack(pady=5)
        tk.Button(self.root, text="Select Student", command=self.select_student).pack(pady=5)
        tk.Button(self.root, text="Manual Reset", command=self.manual_reset).pack(pady=5)
        
        # Labels
        self.selected_label = tk.Label(self.root, text="Selected Student: None", font=("Arial", 14))
        self.selected_label.pack(pady=5)
        
        self.remaining_label = tk.Label(self.root, text="Remaining Students:")
        self.remaining_label.pack(pady=5)
        
        # Remaining students display
        self.student_listbox = tk.Listbox(self.root, height=10, width=30)
        self.student_listbox.pack(pady=5)
        
        # Auto reset controls
        auto_reset_frame = tk.Frame(self.root)
        auto_reset_frame.pack(pady=5)
        
        tk.Checkbutton(auto_reset_frame, text="Enable Auto Reset", variable=self.auto_reset_enabled).pack(side=tk.LEFT)
        tk.Label(auto_reset_frame, text="Reset Time (seconds):").pack(side=tk.LEFT)
        tk.Entry(auto_reset_frame, textvariable=self.reset_time, width=5).pack(side=tk.LEFT)
        
    def load_students(self):
        # Load students from file
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return
        
        try:
            with open(file_path, "r") as file:
                self.students = [line.strip() for line in file if line.strip()]
            self.remaining_students = self.students.copy()
            self.update_student_list()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load students: {e}")
    
    def select_student(self):
        if not self.remaining_students:
            messagebox.showwarning("Warning", "No students remaining! Please reset.")
            return
        
        selected_student = random.choice(self.remaining_students)
        self.remaining_students.remove(selected_student)
        self.selected_label.config(text=f"Selected Student: {selected_student}")
        self.update_student_list()
    
    def manual_reset(self):
        self.remaining_students = self.students.copy()
        self.update_student_list()
        self.selected_label.config(text="Selected Student: None")
    
    def update_student_list(self):
        self.student_listbox.delete(0, tk.END)
        for student in self.remaining_students:
            self.student_listbox.insert(tk.END, student)
        
        if self.auto_reset_enabled.get() and not self.timer_thread:
            self.start_auto_reset_timer()
    
    def start_auto_reset_timer(self):
        reset_time = self.reset_time.get()
        if reset_time <= 0:
            messagebox.showwarning("Warning", "Reset time must be greater than 0!")
            return
        
        self.timer_thread = threading.Timer(reset_time, self.auto_reset)
        self.timer_thread.start()
    
    def auto_reset(self):
        self.manual_reset()
        self.timer_thread = None

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentSelectorApp(root)
    root.mainloop()
