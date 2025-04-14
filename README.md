# Car Sales Web Application

This is a web application for managing car sales using the Flask framework. It allows users to register, log in, and input data related to car sales, with a simple and responsive user interface. The app also includes functionality for user management and sales tracking.

## Features

- **User Registration and Login**: Users can create an account, log in, and manage their session.
- **Data Input**: Users can input data related to car sales and track important metrics such as average income, ad spend per car, and sales-to-income ratio.
- **Prediction**: Based on the input data, the app makes predictions on sales outcomes.
- **Responsive UI**: The application is designed to be responsive for use across various devices.
- **Database Integration**: Data is stored in a SQLite database.

## Installation

To get the project up and running on your local machine, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/snmahsa/car_sales.git
```

### 2. Navigate into the project directory

```bash
cd car_sales
```

### 3. Create a virtual environment

On Windows:
```bash
python -m venv venv
```

On macOS/Linux:
```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

### 5. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 6. Set up the database

The project uses SQLAlchemy for database management. The database will be created automatically when you first run the app.

### 7. Run the application

```bash
python app.py
```

Your application will be accessible at `http://127.0.0.1:5000/`.

## Project Structure

The project has the following structure:

- **`app.py`**: Main application file that defines the Flask routes and application logic.
- **`database.py`**: Defines the database models (User, TrackerInput) and initializes the database connection.
- **`forms.py`**: Contains the forms for user registration, login, and data input using Flask-WTF.
- **`requirements.txt`**: Lists the required Python packages and dependencies.
- **`static/`**: Contains static files such as CSS, JavaScript, and images.
- **`templates/`**: Contains HTML templates for rendering pages.
- **`model/`**: Contains business logic for predictions.
- **`tests/`**: Contains unit and integration tests to ensure the functionality of the app.
- **`instance/`**: Contains configuration files for different environments.
- **`.github/`**: GitHub-related configuration files.

## Routes

- `/`: Home page of the application.
- `/register`: Registration page where new users can sign up.
- `/login`: Login page for existing users.
- `/input`: Page where users can input data for sales tracking.
- `/predict`: Page to show prediction results based on input data.
- `/history`: View past input and prediction history.
- `/logout`: Logout from the session.

## Database Models

- **User**: Contains the user data such as username and password.
- **TrackerInput**: Stores the sales data including metrics such as average income, ad spend per car, and sales-to-income ratio.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
**Link:** https://car-sales-nkpq.onrender.com/

