# Producer Project README

## Project Overview

This Django project serves as the producer in a producer-consumer architecture. It includes components for generating and sending messages to a consumer project. Authentication and permissions are enforced for secure communication.

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd producer_project


2. **Create and activate a virtual environment:**
```
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies

`pip install -r requirements.txt`

Create a .env file using the .env.example template

4. Run migrations:

`python manage.py migrate
`
Creating and Managing API Keys
https://florimondmanca.github.io/djangorestframework-api-key/guide/#creating-and-managing-api-keys

5. Running the Server
`python manage.py runserver`

6. Testing
`python manage.py test`
