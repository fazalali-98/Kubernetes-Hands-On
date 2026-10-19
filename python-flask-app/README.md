# Exercise 9: Jenkins Multi-Stage Pipeline

## Objective
Build and execute a Jenkins CI/CD pipeline for a Python Flask application using multiple stages.

## Tools Used
- Jenkins Pipeline
- Docker Desktop
- Python 3
- Flask
- Git and GitHub
- PowerShell

## Application
The Flask application returns the following message at the home route (`/`):

`Hello, Jenkins Multi-Stage Pipeline!`

## Pipeline Stages
1. **Build:** Create a Python virtual environment and install dependencies from `requirements.txt`.
2. **Test:** Run unit tests using Python's `unittest` framework.
3. **Deploy:** Copy the application files to the `python-app-deploy` directory.
4. **Run Application:** Start the Flask application in the background.
5. **Test Application:** Run the unit tests again to verify the application.

## Dependency Management
A Python virtual environment is used to install dependencies. Flask and Werkzeug versions are pinned in `requirements.txt` to maintain compatibility.

## Jenkins Configuration
- Job name: `Python-MultiStage-Pipeline`
- Pipeline definition: Pipeline script from SCM
- SCM: Git
- Branch: `main`
- Script path: `python-flask-app/Jenkinsfile`

## Expected Outcome
The pipeline stages complete successfully, the unit tests pass, and Jenkins reports:

`Finished: SUCCESS`

## Conclusion
This exercise demonstrates how Jenkins can automate dependency installation, testing, deployment to a mock directory, and application verification through a multi-stage pipeline.
