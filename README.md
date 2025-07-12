# News API

A RESTful API for fetching, filtering, and searching news articles, built with Django and Django REST Framework. This project serves as a robust backend foundation for any news-aggregator application.

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/541c2d88-75c5-4f3e-940e-e480fbcd7723" />

## Key Features

- **RESTful Endpoints**: Provides a clean and predictable API for interacting with news article data.
- **Advanced Filtering**: Supports filtering articles by any model field through `django-filter`.
- **Full-Text Search**: Integrated search functionality to find articles by keywords in their title or summary.
- **Ordering**: Allows clients to sort the article list based on creation date or other fields.
- **Browsable API**: Includes the powerful, self-documenting browsable API from Django REST Framework for easy testing and development.
- **Persistent Storage**: Utilizes an SQLite database to store and manage article data efficiently.

---

## Tech Stack

- **Backend Framework**: Django
- **API Framework**: Django REST Framework
- **Filtering**: `django-filter`
- **Database**: SQLite3
- **Language**: Python

---

## How to Run the Project Locally

To run this project on your local machine, please follow these steps.

### Prerequisites

- Python 3.10 or higher
- Git

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Andrii-Kon/news-api.git
    cd news-api
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables (recommended for security):**
    - Find the `SECRET_KEY` in the `news_api/settings.py` file.
    - Create a new file named `.env` in the project root.
    - Move your secret key into the `.env` file like this:
      ```
      SECRET_KEY="your-django-secret-key-goes-here"
      ```
    - Install `python-dotenv`:
      ```bash
      pip install python-dotenv
      ```
    - Update your `requirements.txt` file:
      ```bash
      pip freeze > requirements.txt
      ```
    - Modify `settings.py` to read the key from the `.env` file. Add these lines at the top:
      ```python
      from dotenv import load_dotenv
      import os
      load_dotenv()
      ```
    - Replace the original `SECRET_KEY` line with this:
      ```python
      SECRET_KEY = os.getenv('SECRET_KEY')
      ```

### Running the Application

1.  **Apply database migrations:**
    This command will create the `db.sqlite3` file and set up the necessary tables.
    ```bash
    python manage.py migrate
    ```

2.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The API will now be live and accessible.

---

## API Endpoints

The primary endpoint for this API is:

- **`GET /api/articles/`**: Retrieve a list of all articles.

### Query Parameters

You can use the following query parameters to control the results:

- **Search**: `?search=<keyword>`
  - _Example_: `/api/articles/?search=Bieber`

- **Ordering**: `?ordering=<field>` (use `-` for descending order)
  - _Example_: `/api/articles/?ordering=-created_at`

- **Filtering**: `?<field>=<value>`
  - _Example (assuming you have a 'source' field):_ `/api/articles/?source=BBC`

---

This project was built as a portfolio piece to demonstrate proficiency in backend development, API design, and professional Python/Django practices.
