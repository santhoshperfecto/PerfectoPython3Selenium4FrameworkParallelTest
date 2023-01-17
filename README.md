# PerfectoPython3Selenium4FrameworkParallelTest
Perfecto Python3 Selenium project with parallel testing

**Prerequisites**
- Python3.x
- Selenium 4.x
- Appium Python Client 2.x


**Install** 

Install Perfecto Python3 Reportium package using below command.

pip install perfecto-py3 (Windows)

pip3 install perfecto-py3 (Mac)

Install pytest and pytest-xdist(for parallel testing)


**Integration with Perfecto**

1. Navigate to "webdriverfactory.py" under base package

2. Replace "cloud name" with your perfecto cloud name (e.g. trial is the cloudName of trial.app.perfectomobile.com).


3. Replace "security token" with your perfecto security token.


4. Update associated browser options as needed or leave as is.



**Executing the script**

Run the project/scripts from the IDE(Ex: PyCharm) after updating Pytest configuration file as below.
![image](https://user-images.githubusercontent.com/61005279/212878582-92dfd3a0-789e-4f28-a854-dab00b150fa4.png)


                OR
Run the script from command line/terminal using below steps.

- Open command line/terminal and navigate to Python project(tests) folder.

- Run the below command:

    pytest -n 4
    
 You can see the test is triggered parallely on Windows Chrome/FF/Edge and Mac Safari browsers.
