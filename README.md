
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
