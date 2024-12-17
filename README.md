<h2>Quick Start Guide (MacOS)</h2>

<h3>In order to view this project you will need to install Python & Django and initialize a virtual environment.</h5>

Install python with command prompt: ```brew install python```

Install django: ```pip install django```

Initialize venv: ```python -m venv ./.venv```

activate venv: ```source ./.venv/bin/activate```

run the server: ```python manage.py runserver```

use Chrome to navigate to http://localhost:8000/


to end the session, press CONTROL + C in the command prompt window to close the server then type ```deactivate``` and press enter to exit the venv.


<h3>Please note that the site does not currently have the ability to add/update ingredients and steps to recipes.</h3>
In order to add ingredients/steps to recipes, you must create an admin/superuser in Django.

With the venv/server running, run ```python manage.py createsuperuser``` in the command window and follow the prompts to create a username, email(optional), and password. Once this is completed navigate to http://localhost:8000/admin/ and login. To add ingredients or steps, click the "+" button next to either option on the left. You will have to add each ingredient/step one at a time and apply it to a specific recipe by selecting it in the dropdown menu before submitting.

Once you have submitted ingredients/steps for a recipe, you should be able to refresh the recipe page on the front end and see the updates!
