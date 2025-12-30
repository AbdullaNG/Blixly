# 📝 Blixly – Blog Application

Blixly is a full-featured blog web application built with Django. It allows users to create and manage blog posts, interact through comments and likes, and includes an admin panel for content management.

## 📸 Screenshots

### Home Page
<img width="1900" height="708" alt="image" src="https://github.com/user-attachments/assets/b1c851aa-1227-4099-8e90-49f45bbb24aa" />


### Post Detail Page
<img width="1898" height="690" alt="image" src="https://github.com/user-attachments/assets/edb62236-5731-467f-a021-bacd496e66c4" />
<img width="1894" height="861" alt="image" src="https://github.com/user-attachments/assets/226ad941-2fba-497e-8dd7-1b2e6d6de007" />


### Profile Page
<img width="1898" height="781" alt="image" src="https://github.com/user-attachments/assets/6b1ad239-45b0-412b-9031-d1867b328c78" />


## 🚀 Features

- User Authentication (Sign up, Login, Logout)
- User profiles
- Blog Posts (Create, Read, Update, Delete)
- Pagination
- Comments system
- Like and Unlike posts
- Django Admin Panel
- Responsive UI using Bootstrap

## 🧰 Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite


## ⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/AbdullaNG/Blixly.git  
cd Blixly
```

2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows  
```bash
venv\Scripts\activate
```

Linux / macOS  
```bash
source venv/bin/activate
```

3. Install dependencies

```bash
pip install django pillow django-crispy-forms crispy-bootstrap5 django-ckeditor
```

4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

Open your browser and go to:  
http://127.0.0.1:8000/



## 🔑 Admin Panel

Access the admin panel at:  
http://127.0.0.1:8000/admin/

The admin panel allows management of:
- Users
- Blog posts
- Comments
- Likes
