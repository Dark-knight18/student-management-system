import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, major):
        if student_id in self.students:
            return "Student ID already exists."
        else:
            self.students[student_id] = Student(student_id, name, age, major)
            return "Student added successfully."

    def view_students(self):
        return "\n".join(str(student) for student in self.students.values()) or "No students available."

    def update_student(self, student_id, name=None, age=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
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

        self.sms = StudentManagementSystem()
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        # Title label
        title_label = tk.Label(frame, text="Student Management", font=("Arial", 16))
        title_label.pack(pady=10)

        # Buttons
        self.add_button = ttk.Button(frame, text="Add Student", command=self.add_student)
        self.add_button.pack(fill='x', padx=20, pady=5)

        self.view_button = ttk.Button(frame, text="View Students", command=self.view_students)
        self.view_button.pack(fill='x', padx=20, pady=5)

        self.update_button = ttk.Button(frame, text="Update Student", command=self.update_student)
        self.update_button.pack(fill='x', padx=20, pady=5)

        self.delete_button = ttk.Button(frame, text="Delete Student", command=self.delete_student)
        self.delete_button.pack(fill='x', padx=20, pady=5)

        self.search_button = ttk.Button(frame, text="Search Student", command=self.search_student)
        self.search_button.pack(fill='x', padx=20, pady=5)

        # Exit button
        self.exit_button = ttk.Button(frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(fill='x', padx=20, pady=20)

        # Footer label with your name
        footer_label = tk.Label(self.root, text="Created by Sourabh", font=("Arial", 10))
        footer_label.pack(side='bottom', pady=10)

    def add_student(self):
        student_id = simpledialog.askstring("Input", "Enter Student ID:")
        name = simpledialog.askstring("Input", "Enter Name:")
        age = simpledialog.askstring("Input", "Enter Age:")
        major = simpledialog.askstring("Input", "Enter Major:")
        result = self.sms.add_student(student_id, name, age, major)
        messagebox.showinfo("Result", result)

    def view_students(self):
        result = self.sms.view_students()
        messagebox.showinfo("Students", result)

    def update_student(self):
        student_id = simpledialog.askstring("Input", "Enter Student ID to update:")
        name = simpledialog.askstring("Input", "Enter new Name (leave blank to keep unchanged):")
        age = simpledialog.askstring("Input", "Enter new Age (leave blank to keep unchanged):")
        major = simpledialog.askstring("Input", "Enter new Major (leave blank to keep unchanged):")
        
        result = self.sms.update_student(
            student_id,
            name if name else None,
            age if age else None,
            major if major else None
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
