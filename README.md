# FastAPI RBAC Project with JWT Authentication

This project is a RESTful API built using FastAPI that supports:

- User registration and login with JWT authentication
- Role-based access control (admin/user)
- CRUD operations for projects (admin only)

# Features

- Secure authentication using JWT
- User roles (admin, user)
- Admin-only access to create/update/delete projects
- Project listing for all authenticated users

# Installation

1. Clone the repository

   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Create a virtual environment

    python -m venv venv
    source venv/bin/activate

3. Install dependencies

    pip install -r requirements.txt

4. Configure environment variables

    DATABASE_URL=sqlite:///./db.sqlite3
    SECRET_KEY=your_secret_key_here

5. Run the FastAPI app

    uvicorn main:app --reload

6. Access the interactive API docs

    http://localhost:8000/docs

    http://localhost:8000/redoc

7. Endpoints Summary

    Auth Routes:

    POST /register – Register a new user

    POST /login – Login and receive JWT access token

    Project Routes:

    GET /projects – View all projects (authenticated users)

    POST /projects – Create a project (admin only)

    PUT /projects/{id} – Update a project (admin only)

    DELETE /projects/{id} – Delete a project (admin only)

8. Demo Video

    Watch the setup and usage demo here:

    Demo Video Link
    ((https://drive.google.com/file/d/1eO8nlDodRgbyKR9DlxfOQ31GKCoAeKlN/view?usp=sharing))

9. Dependencies
    Install with:

    pip install -r requirements.txt