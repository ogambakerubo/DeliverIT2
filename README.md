# DeliverIT2
Zoom is a courier service that helps users deliver parcels to different destinations. Zoom provides courier quotes based on weight categories.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Git
* Python 3.6.4
* Virtualenv

### Quick Start

1. Clone the repository

```
$ git clone https://github.com/ogambakerubo/DeliverIT2.git
$ cd DeliverIT2
```

2. Initialize and activate a virtualenv

```
$ virtualenv venv
$ source venv/bin/activate
```

3. Install the dependencies

```
$ pip install -r requirements.txt
```

4. Run the development server

```
$ python run.py
```

5. Navigate to [http://localhost:5000](http://localhost:5000)

At the / endpoint you should see Welcome to library books API displayed in your browser.

## Endpoints

Here is a list of all endpoints in the DeliverIT2 API

Endpoint | Functionality
------------ | -------------
POST   /api/v1/users | Create a user
GET    /api/v1/users | Get all users
GET   /api/v1/users/id | Get a single user
PATCH  /api/v1/users/id | Update a single user
DELETE   /api/v1/users/id | Delete a single user
POST   /api/v1/parcels | Create new parcel
GET   /api/v1/users/id/parcels | Get a single user's parcels
GET   /api/v1/parcels | Get all parcels
GET   /api/v1/parcels/id | Get a single parcel
PATCH   /api/v1/parcels/id | Update a single parcel
PATCH   /api/v1/parcels/id/status-update | Update a single parcel status
PUT   /api/v1/parcels/id/cancel | Cancel a single parcel
GET   /api/v1/cancelled-parcels | Get all cancelled parcels

### And coding style tests

Coding styles tests are tests that ensure conformity to coding style guides. In our case, they test conformity to
PEP 8 style guides

```
pylint run.py
```

## Built With

* HTML5
* CSS3
* Python 3.6.4
* Flask - The web framework used

## GitHub pages

https://github.com/ogambakerubo

## Versioning

Most recent version is version 1

## Authors

Ogamba.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration and encouragement
* etc