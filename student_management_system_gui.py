import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


class Student:
    def __init__(self, student_id, name, age, major, email, contact_no, dob):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.email = email
        self.contact_no = contact_no
        self.dob = dob

    def __str__(self):
        return (f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, "
                f"Major: {self.major}, Email: {self.email}, "
                f"Contact No: {self.contact_no}, DOB: {self.dob}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, major, email, contact_no, dob):
        if student_id in self.students:
            return "Student ID already exists."
        else:
            self.students[student_id] = Student(student_id, name, age, major, email, contact_no, dob)
            return "Student added successfully."

    def view_students(self):
        return "\n".join(str(student) for student in self.students.values()) or "No students available."

    def update_student(self, student_id, name=None, age=None, major=None, email=None, contact_no=None, dob=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
            if email:
                student.email = email
            if contact_no:
                student.contact_no = contact_no
            if dob:
                student.dob = dob
            return "Student updated successfully."
        else:
            return "Student not found."

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return "Student deleted successfully."
        else:
            return "Student not found."

    def search_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            return str(student)
        else:
            return "Student not found."


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("400x450")
        self.root.configure(bg='black')  # Set background color

        self.sms = StudentManagementSystem()
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg='black')  # Frame background color
        frame.pack(pady=20)

        # Title label
        title_label = tk.Label(frame, text="Student Management System", font=("Arial", 20), fg='grey', bg='black')
        title_label.pack(pady=15)

        # Buttons
        self.add_button = ttk.Button(frame, text="Add Student", command=self.add_student)
        self.add_button.pack(fill='x', padx=20, pady=5)
        self.add_button.configure(style='TButton')

        self.view_button = ttk.Button(frame, text="View Students", command=self.view_students)
        self.view_button.pack(fill='x', padx=20, pady=5)
        self.view_button.configure(style='TButton')

        self.update_button = ttk.Button(frame, text="Update Student", command=self.update_student)
        self.update_button.pack(fill='x', padx=20, pady=5)
        self.update_button.configure(style='TButton')

        self.delete_button = ttk.Button(frame, text="Delete Student", command=self.delete_student)
        self.delete_button.pack(fill='x', padx=20, pady=5)
        self.delete_button.configure(style='TButton')

        self.search_button = ttk.Button(frame, text="Search Student", command=self.search_student)
        self.search_button.pack(fill='x', padx=20, pady=5)
        self.search_button.configure(style='TButton')

        # Exit button
        self.exit_button = ttk.Button(frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(fill='x', padx=20, pady=20)
        self.exit_button.configure(style='TButton')

        # Footer label with your name
        footer_label = tk.Label(self.root, text="Created by Sourabh", font=("Arial", 10), fg='grey', bg='black')
        footer_label.pack(side='bottom', pady=10)

        # Custom style for buttons
        style = ttk.Style()
        style.configure('TButton', background='blue', foreground='grey', padding=10)
        style.map('TButton', background=[('active', 'darkblue')])  # Change button color on hover

    def add_student(self):
        student_id = simpledialog.askstring("Input", "Enter Student ID:")
        if not student_id:
            messagebox.showerror("Error", "Student ID is required.")
            return

        name = simpledialog.askstring("Input", "Enter Name:")
        if not name:
            messagebox.showerror("Error", "Name is required.")
            return

        age = simpledialog.askstring("Input", "Enter Age:")
        if not age or not age.isdigit():
            messagebox.showerror("Error", "Valid age is required.")
            return

        major = simpledialog.askstring("Input", "Enter Major:")
        if not major:
            messagebox.showerror("Error", "Major is required.")
            return

        email = simpledialog.askstring("Input", "Enter Email:")
        if not email:
            messagebox.showerror("Error", "Email is required.")
            return

        contact_no = simpledialog.askstring("Input", "Enter Contact No (10 digits):")
        if not contact_no or not (contact_no.isdigit() and len(contact_no) == 10):
            messagebox.showerror("Error", "Contact No must be exactly 10 digits.")
            return

        dob = simpledialog.askstring("Input", "Enter Date of Birth (YYYY-MM-DD):")
        if not dob:
            messagebox.showerror("Error", "Date of Birth is required.")
            return

        result = self.sms.add_student(student_id, name, int(age), major, email, contact_no, dob)
        messagebox.showinfo("Result", result)

    def view_students(self):
        result = self.sms.view_students()
        messagebox.showinfo("Students", result)

    def update_student(self):
        student_id = simpledialog.askstring("Input", "Enter Student ID to update:")
        if not student_id:
            messagebox.showerror("Error", "Student ID is required.")
            return

        name = simpledialog.askstring("Input", "Enter new Name (leave blank to keep unchanged):")
        age = simpledialog.askstring("Input", "Enter new Age (leave blank to keep unchanged):")
        major = simpledialog.askstring("Input", "Enter new Major (leave blank to keep unchanged):")
        email = simpledialog.askstring("Input", "Enter new Email (leave blank to keep unchanged):")
        contact_no = simpledialog.askstring("Input", "Enter new Contact No (leave blank to keep unchanged):")
        dob = simpledialog.askstring("Input", "Enter new DOB (leave blank to keep unchanged):")

        result = self.sms.update_student(
            student_id,
            name if name else None,
            int(age) if age and age.isdigit() else None,
            major if major else None,
            email if email else None,
            contact_no if contact_no and (contact_no.isdigit() and len(contact_no) == 10) else None,
            dob if dob else None
        )
        messagebox.showinfo("Result", result)

    def delete_student(self):
        student_id = simpledialog.askstring("Input", "Enter Student ID to delete:")
        result = self.sms.delete_student(student_id)
        messagebox.showinfo("Result", result)

    def search_student(self):
        student_id = simpledialog.askstring("Input", "Enter Student ID to search:")
        result = self.sms.search_student(student_id)
        messagebox.showinfo("Search Result", result)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
