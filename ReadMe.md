# <center><u>pyGameFlix project for IST 412</u></center>

## Structure

- APP_ROOT: 
    - contains application start up scripts (dev_main.py for local development, main.py for container)
    - application dependency records (Pipfile, Pipfile.lock, requirements.txt)
    - database and application structure files (GameFlix.{dbml, png, puml})
- APP_ROOT/pyGameFlix: 
    - containes the main module code (__init__.py, sets up application and calls the views from the submodules)
    - database models (for application reference and database migrations) (models.py)
    - initial database seed data (seed_data.py)
- APP_ROOT/pyGameFlix/static: static files used by html templates (css, js, and images)
- APP_ROOT/pyGameFlix/templates: application html templates
- APP_ROOT/pyGameFlix/{admin, catalog, users}: application sub-modules
    - views.py: creates views for module (called by __init__.py)
    - forms.py: creates controls used by views and html templates
    - \*.py: broken down views for more modular management

## Database

![GameFlix.png](GameFlix.png)