# Flask Metakam Application

This is a web-based admin panel built using Flask, designed to manage brands and manufacturers. It includes CRUD (Create, Read, Update, Delete) functionality, authentication, and more. The application is styled for a modern look and provides a user-friendly interface.

## Features

- User authentication and authorization using Flask-Login.
- CRUD operations for Brands and Manufacturers.
- Dynamic and responsive design.
- Flash messages for better user feedback.
- Separate login routes for client and admin users.
- Admin-only access to certain features.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Admin Panel](#admin-panel)
- [Screenshots](#screenshots)

## Installation

### Prerequisites

- Python 3.8+
- Poetry (for dependency management)
- Docker (optional, for containerization)

### Clone the Repository

```bash
git clone https://github.com/k4rimdev/Flask-Metakam.git
cd Flask-Metakam
```

### Install Dependencies

```bash
poetry install
```

### Setup Environment Variables
Create a `.env` file in the root directory and add the following configuration:

```bash
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///app.db  # or use PostgreSQL/MySQL URI
FLASK_ENV=development
```

### Configuration

Modify the `config.py` file if you need to customize the settings further:

* SECRET_KEY: Security key for encryption and sessions.
* SQLALCHEMY_DATABASE_URI: Database connection string.
* FLASK_ENV: Set to `development` or `production`.

### Usage

Running the Application

```bash
poetry run flask db upgrade  # Set up the database
poetry run flask run         # Start the server
```

Navigate to `http://127.0.0.1:5000` in your browser.

### Creating an Admin User
You need to create an admin user to access the admin panel:

```py
from app import create_app, db
from app.controllers.user_controller import UserController

app = create_app()
with app.app_context():
    UserController.add_user('admin', 'adminpassword')
```

### API Endpoints

##### Brands
* `GET /brands` - List all brands
* `POST /brands` - Add a new brand
* `GET /brands/edit/<id>` - Edit a specific brand
* `POST /brands/delete/<id>` - Delete a brand

##### Manufacturers
* `GET /manufacturers` - List all manufacturers
* `POST /manufacturers` - Add a new manufacturer
* `GET /manufacturers/edit/<id>` - Edit a specific manufacturer
* `POST /manufacturers/delete/<id>` - Delete a manufacturer

##### Admin Panel

The admin panel can be accessed at `http://127.0.0.1:5000/admin_client/brands` and `http://127.0.0.1:5000/admin_client/manufacturers`. This requires login authentication.

##### Admin Access
To access the admin panel, log in with the credentials created during the setup. If not logged in, the application will redirect you to the login page.

### Screenshots

![Manufacturers page](https://github.com/k4rimDev/Flask-Metakam/blob/main/screenshots/Screenshot%202024-10-20%20at%2002.09.47.png)
![Edit Manufacturers](Screenshots/Screenshot%202024-10-20%20at%2002.09.54.png)
![Add Manufacturers](Screenshots/Screenshot%202024-10-20%20at%2002.10.02.png)
![Brand page](Screenshots/Screenshot%202024-10-20%20at%2002.10.08.png)
![Add Brand](Screenshots/Screenshot%202024-10-20%20at%2002.10.13.png)
![Login page](Screenshots/Screenshot%202024-10-20%20at%2002.10.21.png)
![Login page](Screenshots/Screenshot%202024-10-20%20at%2002.10.27.png)
![Admin create](Screenshots/Screenshot%202024-10-20%20at%2002.10.32.png)
![Login page](Screenshots/Screenshot%202024-10-20%20at%2002.12.13.png)


## Contact

For any questions or feedback, please reach out at:

Email: karimmirzaguliyev@gmail.com
LinkedIn: [Karim Mirzaguliyev](https://linkedin.com/in/kerim-mirzequliyev)
    
