<p align="center">

  <h1 align="center">
    ❮/❯
    <br />
    CUST X
  </h1>
  
  <a href="https://github.com/custproject/custx/blob/release/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
  <a href="https://github.com/custproject/custx/releases"><img src="https://img.shields.io/badge/size-20.83kb-green" height="20"/></a>

</p>

## Features

* Full **Docker** integration (Docker based).
* **Docker Compose** integration and optimization for local development.
* **Production ready** Python web server using Uvicorn and Gunicorn.
* **Secure password** hashing by default.
* **JWT token** authentication.
* **SQLAlchemy** models (independent of Flask extensions, so they can be used with Celery workers directly).
* Basic starting models for users (modify and remove as you need).
* **Alembic** migrations.).
* **Vue** frontend:
    * Generated with Vue CLI.
    * **JWT Authentication** handling.
    * Login view.

## How to use it

Go to the directory where you want to create your project and run:

```bash
pip install cookiecutter
cookiecutter https://github.com/custproject/custx
```

### Generate passwords

You will be asked to provide passwords and secret keys for several components. Open another terminal and run:

```bash
openssl rand -hex 32
# Outputs something like: 99d3b1f01aa639e4a76f4fc281fc834747a543720ba4c8a8648ba755aef9be7f
```

Copy the contents and use that as password / secret key. And run that again to generate another secure key.


### Input variables

The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto generated) are:

* `project_name`: The name of the project
* `project_slug`: The development friendly name of the project. By default, based on the project name

<br/>
<p align="center"><a https://github.com/custproject/custx#"><img src="https://github.com/custproject/.github/blob/main/images/buttons/backToTopButtonTransparentBackground.png" alt="Back to top" height="29"/></a></p>
