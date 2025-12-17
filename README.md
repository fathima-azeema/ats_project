# Applicant Tracking System (ATS)

## 1️⃣ Project Overview
**Project Name:** Applicant Tracking System (ATS)  
**Purpose:** Helps HR teams manage job applicants efficiently — track applications, filter candidates, and visualize data.

---

## 2️⃣ Key Features
- Dashboard with total applicants, status counts (New, Shortlisted, Rejected, Hired), and charts.  
- Add/Edit/Delete applicants with form validations.  
- Upload resumes (PDF) or provide resume links.  
- Search applicants by name or position.  
- Filter applicants by status.  
- Responsive design for mobile and desktop.  
- Interactive charts: pie chart for applicant status, bar chart for applicants by position.  
- Optional: pagination for large applicant lists.

---

## 3️⃣ Frontend
- **HTML5, CSS3:** Structure and styling of pages.  
- **Bootstrap 5:** Responsive layout, cards, tables, buttons.  
- **Bootstrap Icons:** Edit/Delete icons, status icons.  
- **Chart.js:** Interactive charts for dashboard visualization.  
- **JavaScript:** Minor interactivity (charts rendering, tooltips).

---

## 4️⃣ Backend
- **Python 3.14**  
- **Django 5.x:**  
  - Handles routing, views, forms, and models.  
  - Manages database ORM for applicants and positions.  
  - Templates for dynamic HTML rendering.

---

## 5️⃣ Database
- **SQLite** (default for Django projects) for local development.  
- **Applicant model fields:** `name`, `email`, `phone`, `position`, `status`, `resume_file`, `resume_url`, `created_at`.

---

## 6️⃣ Deployment-Ready Configurations
- **PythonAnywhere Deployment:** The project is ready to run on PythonAnywhere using WSGI configuration.  
- **requirements.txt:** Lists Python dependencies like Django, gunicorn, etc.  
- Static & Media files are handled via Django’s `staticfiles` and `media` folders.

