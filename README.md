

# Financial Dashboard for Viwe Teko (Pty) Ltd

## Overview
This project is an interactive financial dashboard built for Viwe Teko (Pty) Ltd, an investment company that manages its own funds. The dashboard allows users to track financial investments over various time periods, including `daily`, `weekly`, `monthly`, `quarterly`, and `annually`. It provides features to:

- Filter data by asset classes
- Visualize trends with interactive charts (line and pie charts)
- View detailed financial data in tables

The backend is developed using **Django** and **Django REST Framework**, while the frontend is built with **HTML**, **CSS**, and **JavaScript**, utilizing **Chart.js** for dynamic visualizations.

## Technologies Used
- **Backend**: Django, Django REST Framework, Pandas
- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Database**: SQLite (default), configurable to other databases supported by Django

## Installation
Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/financial-dashboard.git
   cd financial-dashboard
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

## Running the Application
1. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

2. **Access the dashboard**:
   Open a web browser and navigate to `http://127.0.0.1:8000/`.

## Populating the Database
To add data to the dashboard, you have two options:

- **Using the Django admin interface**:
  1. Create a superuser:
     ```bash
     python manage.py createsuperuser
     ```
  2. Log in to the admin panel at `http://127.0.0.1:8000/admin/` with your superuser credentials.
  3. Add entries for `AssetClass` and `FinancialData`.

- **Using a custom script**:
  Write a script to seed the database with sample data and run it using:
  ```bash
  python manage.py shell
  ```

## API Endpoints
The backend provides the following API endpoints for the frontend to fetch data:

- **Asset Classes**: `/api/asset-classes/`  
  - Lists all available asset classes.

- **Financial Data**: `/api/financial-data/`  
  - Fetches filtered and aggregated financial data.  
  - **Query Parameters**:
    - `start_date`: Start date for the data range (e.g., `2020-01-01`)
    - `end_date`: End date for the data range (e.g., `2023-12-31`)
    - `granularity`: Time period aggregation (`D` for daily, `W` for weekly, `M` for monthly, `Q` for quarterly, `A` for annually)
    - `asset_classes`: Comma-separated list of asset class names (e.g., `Stocks,Bonds`)

  **Example Request**:
  ```
  /api/financial-data/?start_date=2020-01-01&end_date=2023-12-31&granularity=M&asset_classes=Stocks,Bonds
  ```

## File Hierarchy
The project is organized as follows:
```
financial-dashboard/
├── financial_dashboard/          # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dashboard/                    # Django app for the dashboard
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/               # Database migration files
│   │   └── ...
│   ├── models.py                 # Database models
│   ├── serializers.py            # API serializers
│   ├── static/                   # Static files (CSS, JS)
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── scripts.js
│   ├── templates/                # HTML templates
│   │   └── dashboard/
│   │       └── index.html
│   ├── tests.py                  # Unit tests
│   ├── urls.py                   # App-specific URL routing
│   └── views.py                  # Views and API endpoints
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

### Notes
- Replace `yourusername` in the `git clone` command with your actual GitHub username or repository URL.
- Ensure that all dependencies are listed in `requirements.txt` for the `pip install` command to work correctly.
- This README assumes the project is hosted on GitHub. If using another platform, adjust the clone URL accordingly.
- For production deployment, consider using a more robust database like PostgreSQL and configure Django settings accordingly.

---

To use this, save the above content as `README.md` in the root directory of your project. It provides a comprehensive guide for anyone looking to understand, set up, or contribute to the "Financial Dashboard for Viwe Teko (Pty) Ltd" project.