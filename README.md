[![Built with Cookiecutter Django][cookiecutter-django-image]][cookiecutter-django-url]
[![Contributors][contributor-shield]][contributor-url]
[![Issues][issues-shield]][issues-url]
[![Apache License][license-shield]][license-url]
[![Coveralls][coverage-shield]][coverage-url]
[![Codacy][codacy-shield]][codacy-url]
[![Black][black-shield]][black-url]
[![Isort][isort-shield]][isort-url]
[![Checked with mypy][mypy-shield]][mypy-url]
[![pre-commit.ci status][pre-commit-shield]][pre-commit-url]
[![Deep Source][deepsource-shield]][deepsource-url]
[![Deep Source][deepsource-resolved-shield]][deepsource-resolved-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
   <a href="#">
    <img src="docs/images/oneBarangay_Brand.png" alt="Logo">
  </a>

<h3 align="center">oneBarangay</h3>

  <p align="center">
    An e-Government System for Online Transaction Processing
    <br />
    through Web and Mobile Application with Implementation of OCR Technologies.
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="https://github.com/PrynsTag/oneBarangay-REST-API/issues">Report Bug</a>
    ·
    <a href="https://github.com/PrynsTag/oneBarangay-REST-API/issues">Request Feature</a>
  </p>
</p>

> ***Note:*** For old implementation of the project with OCR and Image Processing capabilities,
> please refer to the [old repo](https://github.com/PrynsTag/oneBarangay).

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Screenshots](#screenshots)
- [Built With](#built-with-)
- [Pre-Requisites](#pre-requisites)
- [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Deployment](#deployment)
- [Settings](#settings)
- [Basic Commands](#basic-commands)
    - [Setting Up Your Users](#setting-up-your-users)
    - [Type Checks](#type-checks)
    - [Pre-Commit Checks](#pre-commit-checks)
    - [Test Coverage](#test-coverage)
        - [Running Tests with Pytest](#running-tests-with-pytest)
    - [Live reloading and Sass CSS compilation](#live-reloading-and-sass-css-compilation)
    - [Email Server](#email-server)
    - [Sentry](#sentry)
    - [Heroku](#heroku)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [About the Author](#about-the-author)
- [Disclaimer](#disclaimer)
- [Contact](#contact)
- [Donations](#donations)

## About the Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The manual way of processing transactions in the barangay (**village**) is still prevalent
today. Filling out necessary records by using pen and paper that are stored in
log books and folders in the barangay (**village**). There are records which have been
distorted, some records are incomplete and there has been a loss of data.

Web application systems and mobile applications have helped in the tasks that we
perform on a daily basis. These applications assisted us to make our lives
easier in making transactions. With the emergence of technology in the
Philippines, the proposed system, which is the oneBarangay system, will handle
the main office of the barangay (**village**) to provide a systematic, efficient, and
technological way of handling online document issuing and more secure data.

## Features

- Generate [Record of Barangay Inhabitants](https://dilg.gov.ph/PDF_File/issuances/memo_circulars/MC2008-144.pdf) (RBI)
- User Management
- Appointment
- Announcement
- Push Notification
- Analytics
- Browsable API
- [jsonapi.org](https://jsonapi.org) compliant API

## Screenshots

|||
|:-------------------------:|:-------------------------:|
| ![oneBarngay Admin Screenshot 1](docs/images/oneBarangay_Admin_1.png) | ![oneBarngay Admin Screenshot 2](docs/images/oneBarangay_Admin_2.png)|
| ![oneBarngay Admin Screenshot 3](docs/images/oneBarangay_Admin_3.png) | ![oneBarngay Admin Screenshot 4](docs/images/oneBarangay_Admin_4.png)|
| ![oneBarngay API Screenshot 1](docs/images/oneBarangay_API_1.png)   | ![oneBarngay Admin Screenshot 6](docs/images/oneBarangay_API_2.png)|

## Built With 🛠

- [Python](https://www.python.org/) - Programming Language
- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines
- [Django REST Framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web
  APIs
- [Postgres SQL](https://www.postgresql.org) - A relational database management system emphasizing extensibility and SQL
- [Redis](https://redis.io/) - An in-memory data structure store, used as a database, cache and message broker
- [Google Cloud Platform](https://cloud.google.com/) - GCP Storage for storing images and OCR capabilities

## Pre-requisites

- [Python 3.10](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Redis](https://redis.io/download)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Installation

1. Clone the repository

```bash
git clone https://
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the virtual environment

```bash
source venv/bin/activate
```

4. Install the requirements

```bash
pip install -r requirements.txt
```

5. Create a `.env` file and add the following environment variables

```bash
DATABASE_URL=postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/<NAME>
REDIS_URL=redis://<HOST>:<PORT>/0
```

6. Run the migrations

```bash
python manage.py migrate
```

7. Create a superuser

```bash
python manage.py createsuperuser
```

8. Run the server

```bash
python manage.py runserver
```

### Running the tests

#### With Django
```bash
python manage.py test
```

#### With Pytest
```bash
pytest
```

### Deployment

1. Create a `.env` file and add the following environment variables

```bash
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
REDIS_URL=redis://HOST:PORT/0
DJANGO_SECRET_KEY=<your_secret_key>
DJANGO_ALLOWED_HOSTS=<your_host>
DJANGO_GCP_STORAGE_BUCKET_NAME=<your_bucket_name>
DEFAULT_FROM_EMAIL=<your_email>
DJANGO_ADMIN_URL=<your_admin_url>
SENDGRID_API_KEY=<your_sendgrid_api_key>
SENDGRID_GENERATE_MESSAGE_ID=<your_sendgrid_generate_message_id>
SENDGRID_MERGE_FIELD_FORMAT=<your_sendgrid_merge_field_format>
SENTRY_DSN=<your_sentry_dsn>
```

2. Run the migrations

```bash
python manage.py migrate
```

3. Create a superuser

```bash
python manage.py createsuperuser
```

4. Run the server

```bash
python manage.py runserver
```

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "
  Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into
  your browser. Now the user's email should be verified and ready to go.

- To create an **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar),
so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy onebarangay_psql

### Pre-commit checks

Running pre-commit checks:

    $ pre-commit run --all-files

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved
to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to
use [MailHog](https://github.com/mailhog/MailHog) when generating the project a local SMTP server with a web interface
will be available.

1. [Download the latest MailHog release](https://github.com/mailhog/MailHog/releases) for your OS.

2. Rename the build to `MailHog`.

3. Copy the file to the project root.

4. Make it executable:

       $ chmod +x MailHog

5. Spin up another terminal window and start it there:

       ./MailHog

6. Check out <http://127.0.0.1:8025/> to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account
at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

### Heroku

See
detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

## Roadmap

See the [open issues](https://github.com/PrynsTag/oneBarangay-REST-API/issues) for a list
of proposed features (and known issues) .

## Contributing

Contributions are what make the open source community such an amazing place to
learn, inspire, and create. Any contributions you make are **greatly
appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Code of Conduct

Everyone interacting in the OneBarangay project's codebases, issue trackers, chat rooms, and mailing lists is expected
to
follow the [PyLadies Code of Conduct](https://www.pyladies.com/CodeOfConduct/).

## License

This project is licensed under the terms of the [Apache License](/LICENSE).

## Acknowledgements

- [Cookiecutter Django](https://) - A Cookiecutter template for Django projects
- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines
- [Django REST Framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web
  APIs
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Integrated set of Django applications addressing
  authentication, registration, account management as well as 3rd party (social) account authentication.
- [Django Filter](https://django-filter.readthedocs.io/en/master/) - Django Filter is a generic, reusable application to
  filter querysets based on user selections.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) - Custom storage backends for Django.
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) - A configurable set of panels that
  display various debug information about the current request/response.
- [Django Extensions](https://django-extensions.readthedocs.io/en/latest/) - This is a collection of custom extensions
  for
  the Django Framework.
- [Img Shields](https://shields.io) - Quality metadata badges for open source projects
- [Choose an Open Source License](https://choosealicense.com) - A guide to choosing an open source license
- [Font Awesome](https://fontawesome.com) - The web's most popular icon set and toolkit
- [CircleCI](https://circleci.com/) - Continuous Integration and Delivery
- [Codacy](https://www.codacy.com/) - Automated Code Review
- [DeepSource](https://deepsource.io/) - Automated Code Review
- [Sentry.io](https://sentry.io/) - Error Tracking
- [Browserstack](https://www.browserstack.com/) - Cross Browser Testing
- [Black Code Style](https://github.com/psf/black) - The uncompromising code formatter
- [Pre-commit](https://pre-commit.com/) - A framework for managing and maintaining multi-language pre-commit hooks
- [Coveralls](http://coveralls.io/) - Test Coverage History
- [isort](https://pycqa.github.io/isort/) - A Python utility / library to sort imports.
- [djhtml](https://github.com/rtts/djhtml) - A Django template language linter

## About the Author

Hello! I am Prince Velasco. I am a Information Technology student with specialization in Web and Mobile Applications.
I have passion Full-Stack Development and Data Science.

## Disclaimer

This is a work in progress. Any feedback is welcome.

## Contact

For any questions, please contact me at this [email](mailto:github@princevelasco.com)
or in [LinkedIn](https://www.linkedin.com/in/princevelasco/).

## Donations

If you found this project useful, please consider donating to help me maintain and improve this project.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: docs/images/oneBarangay_Product_Screenshot.png

[cookiecutter-django-image]: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?style=for-the-badge&logo=cookiecutter

[cookiecutter-django-url]: https://github.com/cookiecutter/cookiecutter-django/

[contributor-shield]:
https://img.shields.io/github/contributors/PrynsTag/oneBarangay-REST-API?style=for-the-badge

[contributor-url]: https://github.com/PrynsTag/oneBarangay-REST-API/graphs/contributors

[issues-shield]:
https://img.shields.io/github/issues/PrynsTag/oneBarangay-REST-API.svg?style=for-the-badge

[issues-url]: https://github.com/PrynsTag/oneBarangay-REST-API/issues

[license-shield]:
https://img.shields.io/github/license/prynstag/oneBarangay-REST-API?style=for-the-badge

[license-url]: https://github.com/PrynsTag/oneBarangay-REST-API/blob/develop/LICENSE

[coverage-shield]:
https://img.shields.io/coveralls/github/PrynsTag/oneBarangay-REST-API?label=Coveralls&style=for-the-badge

[coverage-url]: https://coveralls.io/github/PrynsTag/oneBarangay-REST-API?branch=develop

[codacy-shield]:
https://img.shields.io/codacy/grade/7a9e9a1402a14005ae4a14b5cffdb1ee?label=Codacy&style=for-the-badge

[codacy-url]:
https://www.codacy.com/gh/PrynsTag/oneBarangay/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PrynsTag/oneBarangay-REST-API&utm_campaign=Badge_Grade

[deepsource-shield]:
https://deepsource.io/gh/PrynsTag/oneBarangay-REST-API.svg/?label=active+issues&token=QI2m-XNk586t3GYXw6YhzOn6

[deepsource-url]:
https://deepsource.io/gh/PrynsTag/oneBarangay-REST-API/?ref=repository-badge

[deepsource-resolved-shield]:
https://deepsource.io/gh/PrynsTag/oneBarangay-REST-API.svg/?label=resolved+issues&token=QI2m-XNk586t3GYXw6YhzOn6

[deepsource-resolved-url]:
https://deepsource.io/gh/PrynsTag/oneBarangay-REST-API/?ref=repository-badge

[black-shield]: https://img.shields.io/badge/code%20style-black-black?style=for-the-badge

[black-url]: https://github.com/psf/black

[isort-shield]:
https://img.shields.io/badge/%20imports-isort-%231674b1?style=for-the-badge&labelColor=ef8336

[isort-url]: https://pycqa.github.io/isort/

[mypy-shield]: https://img.shields.io/badge/mypy-checked-blue?style=for-the-badge

[mypy-url]: http://mypy-lang.org/

[pre-commit-shield]: https://results.pre-commit.ci/badge/github/PrynsTag/oneBarangay-REST-API/develop.svg?style=for-the-badge

[pre-commit-url]: https://results.pre-commit.ci/latest/github/PrynsTag/oneBarangay-REST-API/develop
