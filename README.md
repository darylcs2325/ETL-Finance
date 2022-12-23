# ETL FINANCE
Primero se obtendrá datos registrados de la **bolsa de valores**, estos datos son obtenidos mediante un sencillo **Web Scrapping** a la página de [**Yahoo Finance**](https://finance.yahoo.com), luego se realiza un ETL a dichos datos para ser enviado a la base de datos (**PostgreSQL**), además se crea un **API REST** para poder acceder a la base de datos de forma directa y sencilla. Finalmente, se "*dockeriza*" el programa. 

## Herramientas utilizadas
Detallaré las herramientas más importantes que se utilizó para la realización del proyecto.

### Poetry
En esta ocación utilicé `poetry` como herramienta de gestión y empaquetado de dependencias en Python.

Puede aprender más en este enlace, [Poetry](https://python-poetry.org).

### BeatifulSoap
[BeatifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) es una librería muy utilizado para **Web Scrapping**, en nuestro caso se utiliza para la obtención de datos de **Yahoo Finance**

`poetry add beatifulsoup4`

### FastAPI
[FastAPI](https://fastapi.tiangolo.com) es un framework moderno para la creación de APIs, lo utilizaremos para la creación de un API REST y así acceder a la base de datos de forma directa.

`poetry add fastapi`

### Docker
[Docker](https://www.docker.com) nos permite realizar despliegue de aplicaciones dentro de contenedores. Además, nos permite correr en una distribución de Linux desde cualquier Sistema Operativo, en este proyecto es utilizado para conectarlo a PostgreSQL y PgAdmin.

`poetry add sqlalchemit`

### SQLAlchemit - psycopg2-binary
[SQLAlchemit](https://www.sqlalchemy.org) es una librería que nos permite trabajar con SQL a través de ORM, facilitándonos su programación.

`poetry add sqlalchemit`

[psycopg2](https://pypi.org/project/psycopg2-binary/) nos permite trabajar con PostgreSQL con python.

`poetry add psycopg2-binary`

## Proceso de ejecución
