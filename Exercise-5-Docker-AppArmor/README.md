# Exercise 5: Docker Security with AppArmor and Python

## Objective
Learn Docker security using AppArmor and the Python Docker SDK.

## Files
- app.py: Flask application.
- Dockerfile: Builds the Docker image.
- apply_apparmor.py: Builds the image and checks Docker security options.
- test_restricted_actions.py: Checks AppArmor availability.

## Build Docker Image
docker build -t flask-apparmor .

## AppArmor
AppArmor is a Linux security module that restricts application access using security profiles.

## Results
The Flask Docker image was built successfully. Docker reported seccomp and cgroupns security options, but AppArmor was not enabled in the tested Docker Desktop environment. Therefore, custom AppArmor enforcement could not be verified.

## Conclusion
The Docker image and Python SDK scripts were prepared. Actual AppArmor enforcement requires a Linux environment with AppArmor enabled.
