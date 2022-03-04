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
  
### Assumptions

* Average_score of each player is considered as past personal statistic of that player (not specific to current tournament)
* Average_score of each team is considered as past team statistic of that team (not specific to current tournament)
* Unit of height of players is considered as in centimeters(cm) 
* Unit of weight of players is considered as in kilograms(kg) 

### Test Project

* Run integrations tests using following command
    
    ```
    python manage.py test
    ```

