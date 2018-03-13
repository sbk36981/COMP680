# COMP680: Big Data and Analytics
## Housing Data Prediction
This repo is intended to be an example of a data pipeline, with a customer-facing portal to give them the ability to submit jobs and data. Specifically, it is intended to make predictions on housing prices.

### Sprint 1
Our first sprint is intended to cover the following:
* Business goal: Identify and define features relevant to the price prediction
  * User Story 1: Create a scalable and reliable data pipeline using open source tools
    * Technical Tasks:
      * Examine jupyter notebook
      * Basemap, seaborn
      * AWS
      * Version control (github)
  * User Story 2: Have a clean and complete dataset
    * Technical Tasks:
      * Decide what to do with missing/incorrect values
  * User Story 3: Understand impact of each column on price prediction
    * Technical Tasks:
      * Create an excel workbook with definitions for each feature in the dataset
      * Identify relevant features
      * Remove unnecessary features


## Installation instructions: Customer Portal
### Linux
First, clone the repo in a location of your choice.
`$ git clone https://github.com/sbk36981/COMP680.git`
Enter the directory.
`$ cd COMP680`

If you don't have virtualenv installed, install it with:
`$ pip install virtualenv`
Then, create yourself a virtual environment and activate it.
`$ virtualenv env`
`$ source env/bin/activate`
Install the dependencies via pip.
`(env) $ pip install -r requirements.txt`

Before running the server, you'll need to generate a *secrets.py* file that has value for [SECRET_KEY][https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-SECRET_KEY "SECRET KEY"]. File should be in the same directory as manage.py. Contents will be something like this, see the Django documentation for how to generate a secret key.
`SECRET_KEY = 'random-50-character-string'`
**BE AWARE THAT YOU SHOULD NEVER COMMIT YOUR SECRET KEY TO VERSION CONTROL OR OTHERWISE EXPOSE IT. READ THE OFFICIAL DOCUMENTATION.**

After that's filled out, you can run the development server like so, which will open it on localhost:8000.
`(env) $ python manage.py runserver`

You can open the customer portal by visiting localhost:8000/customerportal.

Close the server by pressing CTRL-C.

The offical amazon docs are a good guide to getting a django server set up on amazon ELB: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html.

Detailed installation instructions pending for the rest of the pipeline.
