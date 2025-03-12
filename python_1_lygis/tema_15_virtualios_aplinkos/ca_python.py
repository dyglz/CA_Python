# pip

# to check pip version
# $ python3 -m pip --version

# to install pip packet
# $ python3 -m pip install <paketo-pavadinimas>


# venv

# to create virtual environment (default name venv or .venv)
# $ python3 -m venv <jūsų_pasirinktas_pavadinimas>
# $ python3 -m venv <.venv>

# activate virtual environment
# $ source .venv/bin/activate


# to install pip packet in .venv
# (venv) $ pip install numpy


# to exit .venv
# (venv) $ deactivate


# so save list of packages in requirements.txt file
# (venv) $ pip freeze > requirements.txt

# to use install requirements from list in .txt file
# (venv) $ pip install -r requirements.txt



# pipenv

# $ python3 -m pip install pipenv

# inicialize pipenv in wanted directory / Pipfile and Pipfile.lock files will be created
# $ pipenv install

# to activate virtual encironment
# $ pipenv shell

# install packages
# (project) $ pipenv install <paketo-pavadinimas>

# packages graph
# (project) $ pipenv graph

# uninstall a package
# (project) $ pipenv uninstall <package-name>

# exit virtual environment
# (project) $ deactivate



