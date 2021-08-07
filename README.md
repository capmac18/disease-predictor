# disease-predictor
A simple Django web application using a Naive Bayes Classifier in the backend to predict a disease form the symptoms entered by the user

If you don't have Django installed on your system, you can install it in a virtual environment using pipenv:

In Windows:

* Open cmd
* Type and Enter:
  pip install pipenv

* Make a folder on your Desktop (say 'Project')
* Type and run these commands:
  cd Desktop/Project
  pipenv install django
  
* Django will be installed in a virtual environment.
* You will see two files : Pipfile and Pipfile.lock in the above directory
* Make sure you are in the above directory (i.e Desktop/Project) to activate the virtual environment.Run the command:
    pipenv shell
    pip install scikit-learn


* After cloning the disease-predictor repository in the local system, navigate to the directory where manage.py is present and run:
  python manage.py runserver
* The development server will be started and link of the web application will be found at the bottom of the terminal viz: http://127.0.0.1:8000/  
 

