### Dependencies

#### Setting up Workspace:
1. install `virtualenv`

  ```bash
  sudo pip install virtualenv
  ```
2. create a new environment

  ```bash
  virtualenv env
  ```
3. install the dependencies:

  ```bash
  env/bin/pip install -r requirements.txt
  ```
4. add config.py

  ```bash
  cp config.sample config.py
  ```
  (change twitter credentials accordingly)
5. make sure to setup PYTHONPATH correctly, go the project directory

    ```bash
  export PYTHONPATH='.'
  ```
6. run server

    ```bash
  env/bin/python run.py
  ```
