# Bulk Ipo Apply - Django

## Clone the Project
Clone the project and  do the following steps:

### 1.1 Setup Vertual Environment:

It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python.

#### Windows cmd : 
` py -m venv envname `

#### Unix/MacOS Terminal : 
` python -m venv envname `

### 1.2 Activate the environment, by typing this command:

#### Windows cmd :
` envname\Scripts\activate.bat `

#### Unix/MacOS Terminal : 
` source envname/bin/activate `

Once the environment is activated, you will see this result in the command prompt:

#### Windows cmd :

` (envname) C:\Users\Prashant> `

#### Unix/MacOS Terminal : 
` (envname) ... $ `



Change Directory to Project:

`cd bulkipo-django/bulkipoapplier`


You can install all the required dependencies by running below command:

` pip install -r requirements.txt `

#### Migrate:

`python manage.py makemigrations`
`python manage.py migrate`

#### Create Super User:

`py manage.py createsuperuser`

#### Run the project:
` py manage.py runserver `

this is not neccessary to do . it is just for freeze dependencies
### Freeze Requirements file:


` pip freeze>requirements.txt`
