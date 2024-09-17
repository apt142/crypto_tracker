# Crypto Tracker


## Project Decription

This service will query external crypto services and monitor some key metrics including:

 * Current Price
 * Pricing History
 * Volatility


### How to use it

Keeping in mind this is all a prototype project that was done in a relatively short period of time, here is some functionality on how to use it.

After getting the project up and running there are a number of urls that will be beneficial to you.


The admin interface has access to browse the data. This could use more refinement but it works out of the box.
http://localhost:8000/admin/


The API to view individual bits of processed data is here. It has a full REST retrieve, list, update and delete crud
http://localhost:8000/api/currency/


To pull the analysis of the data you can go here. This will have the ranking and standard deviation values
http://localhost:8000/api/currency/analysis/


To initiate a pull of the data manually you can go here:
http://localhost:8000/api/currency/pull/


There is all the plumbing and code to run the data pull as a celery beat task. However, that doesn't work due to celery detail that I didn't have time to track down.




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


### Initialize your environment

The first thing you'll want to do is run your migrations

```
./run manage migrate
```

Next, you'll need to new super user.
```
./run manage createsuperuser
```


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


## Next Steps

### Scalability

For maintainability, I'd want to add typing to the project.

> What would you change if you needed to track many other metrics or support every exchange and pair available?

I made the `CurrencySpecificDatem` object really small with concise values so that it could be queried really easily. This should add utility for aggregate functions. If performance was at a high premium, I'd change `currency` and `crypto_id` to integer fields so that DB indexing is much faster with those and searching by string.


> What if you needed to sample them more frequently?

Database volume could become an issue. In addition, I'm doing some post processing after retrieving and storing. If retrieval volume went up, I'd move that post processing to a celery task.


> What if you had many users accessing your dashboard to view metrics?

Calculating the aggregates post retrieval and then caching them would help with a lot of users looking at the same data. The initial assumption here is that we'd just hit the db for this data. But, if we can decide on specific cookie cutter sized data that we think our users want, we could pre-package it.



### Production Readiness

Because the environmental variable are abstracted out and the code is already ready for a container, going to production shouldn't be too difficult. We'd need to have a system to maintain the secrets and to build out the environment files on deploy.


### Testing

> How would you extend testing for an application of this kind (beyond what you implemented)?

This definitely needs unit tests. I feel like those would be easy to write. For testing the API calls, I'd want to use something like PyVCR where we can mock the actual call itself. This would give us a tool to run through all the api code while not actually reaching out their servers.

