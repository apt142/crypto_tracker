# Crypto Tracker


## Project Decription

This service will query external crypto services and monitor some key metrics including:

 * Current Price
 * Pricing History
 * Volatility


## Tech Stack

This project was initialized off of [Docker Django Example](https://github.com/nickjj/docker-django-example). 

### Why this was chosen

First off, there's a lot of boiler plate to getting a django instance running locally on docker. I wanted to go straight to a dockerized instance so that my code has maximum portability. In addition, nearly every code base I've worked on eventually makes the leap to containerization. So, we might as well just do it straight off the bat.

There's a few docker django templates out there. I really like this one because it has a great set of defaults with not a lot of opinions. This means that I can get a lot of things working quickly without locking decisions down early on.

In addition, this boilerplate has EXCELLENT documentation to assist with environment configs. These will save a lot of time in set up.


The initial bare bones are the following:

### Django Version
 - Django 5.1 
 - Python 3.12.5**

### Back-end

- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Celery](https://github.com/celery/celery)

### Front-end

- [esbuild](https://esbuild.github.io/)
- [TailwindCSS](https://tailwindcss.com/)
- [Heroicons](https://heroicons.com/)


## Set up for local dev


### Requirements

You will need to install [Docker Desktop](https://www.docker.com/products/docker-desktop/)


### Install Steps

```
git clone git@github.com:apt142/crypto_tracker.git
cd crypto_tracker
```

#### Copy and update .env file

You're going to need a local environment file.

The `.env.example` file has some standard dev environment values set by default. For a local dev environment, it should work without alteration. Production will definitely want a more robust version of this file.

```
cp .env.example .env
```


#### Run Docker
```
docker compose up --build
```

Once docker has initalized and is running you can visit the project at: <http://localhost:8000>


### Tools for ongoing development

#### Install Pre-commit

A pre-commit is highly recommended. To install it just run the following commands:

```
brew install pre-commit
pre-commit install
```

This will ensure that each commit that you do is in line with our coding standards.


#### Useful Commands

This project is built off of [Docker Django Example](https://github.com/nickjj/docker-django-example). See their documentation for a full list of useful commands. 

Here is a short list of helpful ones:


Update dependencies:
Back-end: `./run pip3:install` 
Front-end: `./run yarn:install`


Run Django commands:
```
./run manage <command>

# Run migrations
./run manage migrate

# Run all tests
./run manage test
```


ssh into main host
ssh into celery

