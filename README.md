# BasketBallTournamentManagementSystem - API

This project exposes REST API for Basket Ball Tournament

## Getting Started

```shell
git clone <repo_url>
```

### Prerequisites

Setting up local development environment.

* Install Python version 3.10.2

### Setup

* Install required packages mentioned in requirements.txt
    ```
    pip install <requirement>
    ```
* Create database models
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

* Generate dummy data
    ```
    python manage.py generate_data
    ```

### Test Project

* Run integrations tests using following command
    
    ```
    python manage.py test
    ```

