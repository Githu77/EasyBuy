# EasyBuy

EasyBuy is an e-commerce platform developed using Django. It allows users to browse various products, add them to a cart, and purchase them using different payment methods, including PayPal. The platform is designed to provide a seamless shopping experience with features like product search, categories, and user authentication.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (signup, login)
- Product listing with categories
- Product search functionality
- Add to cart and checkout with PayPal
- Responsive design for mobile and desktop

## Requirements

- Python 3.10+
- Django 3.x
- pip (Python package installer)
- A web browser

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/easybuy.git
cd easybuy
```

### Create virtual environment

```bash
python -m venv myenv
source myenv/bin/activate # On Windows use `myenv\Scripts\activate`
```  
### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```
### Create a Superuser

```bash
python manage.py createsuperuser
```
## Configuration

### Environment Variables

Create a .env file in the root directory and add the following environment variables:


SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # Update this if using a different database
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_SECRET=your_paypal_secret


### Static Files

Collect static files:

```bash
python manage.py collectstatic
```

## Usage

### Running the Development Server

Start the server by running:

```bash
python manage.py runserver
```

Open your browser and navigate to http://127.0.0.1:8000/ to see the application.

## Usage

### Running the Development Server

Start the server by running:

```bash
python manage.py runserver
```

Open your browser and navigate to http://127.0.0.1:8000/ to see the application.

### Admin Panel

Access the Django admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials created earlier.

### Deployment
Deploying to PythonAnywhere
Sign up for a PythonAnywhere account if you haven't already.

Create a new web app using the Manual Configuration option.

Clone your repository on PythonAnywhere.

Create a virtual environment and install dependencies.

Set up your WSGI configuration file.

Add your environment variables in the PythonAnywhere web app settings.

Reload your web app to apply the changes.

For detailed deployment instructions, refer to the PythonAnywhere Deployment Guide.

### Contributing
We welcome contributions to EasyBuy! If you would like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

### License
EasyBuy is licensed under the MIT License. See the LICENSE file for more information.


### Explanation:
- **Features:** Lists the key features of your application.
- **Requirements:** Specifies the software required to run the project.
- **Installation:** Detailed steps on how to clone the repository, create a virtual environment, and install dependencies.
- **Configuration:** Instructions on setting up environment variables and static files.
- **Usage:** How to run the development server and access the admin panel.
- **Deployment:** Basic instructions for deploying the project on PythonAnywhere.
- **Contributing and License:** Information on contributing to the project and its licensing.

Feel free to customize any part of this README to better suit your project! Let me know if there's anything else you need. 😊