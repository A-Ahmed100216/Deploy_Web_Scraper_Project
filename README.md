# Web Scraper Project

## Introduction
This app scrapes data from ITJobsWatch and writes to a file on the local host. The aim of this project is to deploy the app on a virtual machine and build a CI/CD pipeline.

## Run app on local machine
1. Clone code and open with PyCharm.
2. Install any package and dependencies, these can be found in the requirements.txt file.
3. Run main.py file and confirm the app runs on the local host.

## Running local tests
1. Set test_env to `live` in the config.ini file
2. Run the following command `pip3 install -U pluggy`
3. Run
```bash
python -m pytest tests/
```
4. The following output should be displayed
![local tests](images/local_tests.png)


## CI Pipeline
1. Navigate to Jenkins
2. Configure the job.
3. Add the following commands to the build step
```bash
sudo apt-get update
# Install python pip module
sudo apt-get install python3-pip -y
# Install pytest
pip3 install -U pytest
# Install BeautifulSoup4
sudo pip3 install BeautifulSoup4
```

Testing 1    
Testing 2    
Testing 3 - checking failures are not pushed to main
