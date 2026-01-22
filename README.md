# Student Attendance System

The Student Attendance System is a web-based application designed to efficiently manage student attendance across multiple classes. Built using the Flask framework and SQLite for data storage, the system provides an organized interface for managing students, classes, and attendance records, with a focus on simplicity, accuracy, and reliability.

---

## Features

### **1. Class Management**

The system supports multiple classes, such as Year 1 through Year 4. Users can view a list of all available classes and select a class to view or manage students and attendance records. Each class operates independently, ensuring that attendance tracking is accurate and organized. This design allows for easy expansion if more classes are added in the future.

### **2. Student Management**

Students can be added or removed from the system under their respective classes. Each student record includes a unique ID, a name, and the assigned class. Duplicate entries are prevented to maintain data integrity. Removing students is controlled through a dropdown selection to avoid accidental deletions. All student information is securely stored in the SQLite database.

### **3. Attendance Marking**

Attendance can be marked for a selected date. Each student in the class is listed in a tabular format with options to select their status: Present, Absent, or Leave. The system automatically checks for existing records to prevent duplicates and ensures that all updates are accurately recorded. Attendance data is stored with the student ID and date, providing a comprehensive history for reporting and tracking purposes.

### **4. Attendance Viewing**

The system allows users to view attendance records by class and date. Users can filter records to check attendance for specific days or generate a history overview for the entire class. The interface presents data in a clear tabular format, showing student names and their corresponding attendance status. Missing or empty records are handled gracefully with user-friendly error messages.

### **5. Data Validation and Error Handling**

All input forms are validated to ensure accurate data entry. Duplicate student IDs are automatically rejected, and the system prevents the submission of incomplete forms. Database errors and missing records are managed with informative messages to the user. This ensures reliability and prevents data inconsistencies.

---

## Routes Description

### **`/` – Home Page**

The landing page provides an overview of the system and navigation links to all features, including classes, student management, and attendance tracking.

### **`/select_class/<action>` – Class Selection Gateway**

This route dynamically adapts based on the user's intended action, such as marking attendance, viewing records, or removing students, streamlining the workflow.

### **`/new_student` – Add Student**

A form for registering new students. The user inputs the student ID, name, and selects the class from a dropdown menu. The system prevents duplicate IDs and stores the information in the database.

### **`/attendance/<cls>` – Attendance Page**

This page lists all students for the selected class. Users select the date and mark each student as Present, Absent, or Leave. The system saves new records or updates existing ones to prevent duplicates.

### **`/records/<cls>` – Attendance Records**

Displays a table of attendance records for the chosen class. Users can filter by date to see daily attendance or view the full history. Empty results display a user-friendly message.

### **`/remove/<cls>` – Remove Student**

Allows safe removal of students. The user selects the class and student from dropdowns. A confirmation step ensures that records are deleted intentionally.

---

## Database Structure

### **Students Table**

Stores basic student information:

| Column     | Type    | Description       |
| ---------- | ------- | ---------------- |
| id         | INTEGER | Primary key       |
| student_id | TEXT    | Unique identifier |
| name       | TEXT    | Student name      |
| class      | TEXT    | Year group        |

### **Attendance Table**

Stores daily attendance records:

| Column     | Type    | Description          |
| ---------- | ------- | ------------------- |
| id         | INTEGER | Primary key          |
| student_id | TEXT    | Foreign key          |
| date       | TEXT    | Attendance date      |
| status     | TEXT    | Present/Absent/Leave |

---

## Technologies Used

* **Python (Flask)** for backend development  
* **SQLite** for relational database management  
* **HTML, CSS, Jinja2** for frontend templating and design  
* **Static Files:** `style.css` for styling and `bg.jpg` for background image  

---

## Future Enhancements

The system can be expanded with additional features:

* User authentication and roles for multiple staff members  
* Bulk import/export of student records  
* Advanced attendance reports and analytics  
* Email notifications for absent students  
* Mobile-optimized design for tablets and smartphones  
* Multi-school support for managing multiple institutions  

---

This Student Attendance System provides a reliable and organized solution for schools to digitize attendance tracking, replacing traditional paper-based methods. The application ensures accurate data, simple workflows, and efficient management of student attendance records.
