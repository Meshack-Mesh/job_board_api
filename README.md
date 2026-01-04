**JOB_BOARD_API**
**OVERVIEW**
job_board_api is an open-source Django-based backend framework tailored for building scalable and manitainable job board applications. Its designed to manage companies, job listings, and applications with secure authentication and an admin dashboard.

**Whyjob_board_api?**
The project streamlines the development, deployment, and management of a comprehensive job
the core features include:
1. Management Commands: Simplifies database migrations, server management, and maintenance tasks.
2. Deployment Ready: Supports both WSGI and ASGI interfaces for flexible deployment options including real-time features.
3. Clear Routing & Configuration: Provides structured URL routing and environment settings for seamless integration.
4. Build-in testing: Ensures code quality with dedicated tests modules for key components.
5. Modular Design: Facilitates organized developments across user, job, company, and application modules.

Features
Authentication & Authorization

1. JWT-based authentication (login & refresh tokens)
2. Django superuser for admin-level access
3. Secure access control for job and company management

Company Management

1. Create, update, delete companies
2. Store company details (name, location, website, description)
3. Admin-managed via Django Admin panel

Job Management

1. Create and manage job postings
2. Job types (Full-time, Part-time, Contract, Internship)
3. Link jobs to companies
4. Timestamped job creation

Applications Management

1. Users can apply to jobs
2. Upload resumes
3. Application status tracking (Pending, Reviewed, Accepted, Rejected)

Admin Dashboard

1. Fully customized Django Admin interface
2. Search, filter, and sort jobs, companies, and applications
3. Production-ready admin experience

Project Structure 

job_board/
│
├── job_board/          # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── users/              # Authentication & users
│
├── companies/          # Company management
│
├── jobs/               # Job postings
│
├── applications/       # Job applications
│
├── templates/          # Django templates
│
├── static/             # CSS & JS files
│
├── media/              # Uploaded resumes
│
├── manage.py
└── README.md


Tech Stack
Backend            - Django
API                - Django REST Framework
Authentication     - Simple JWT
Database           - SQLite
Version Control    - Git & Github


**Getting Started**
Prerequisites

This project requires the following dependencies:

Programming Language: Python
Editor : Vs Code

**Installation**
Build job_board_api from the source and install dependencies:

1. Clone the repository:

> git clone https://github.com/Meshack-Mesh/job_board_api

2. Navigate to the project directory:
> cd job_board_api

3. Install Dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Create Superuser (Admin)
python manage.py createsuperuser

6. Start the Server
python manage.py runserver

Authentication Endpoints

POST	/auth/login/	Get access & refresh token
POST	/auth/refresh/	Refresh access token
