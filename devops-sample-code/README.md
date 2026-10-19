# Exercise 8: Hello World Jenkins Job

## Objective
Create a Jenkins job that retrieves a shell script from GitHub and executes it.

## Tools Used
- Jenkins
- Docker Desktop
- Git and GitHub
- PowerShell

## Steps Completed
1. Created the public GitHub repository `devops-sample-code`.
2. Created and pushed `hello-world.sh` to GitHub.
3. Configured the existing Jenkins `hello-ci` job to use the GitHub repository.
4. Added an Execute shell build step.
5. Ran the Jenkins job and checked the console output.

## Shell Script
```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

## Jenkins Build Command
```bash
sh hello-world.sh
```

## Expected Output
```text
Hello, Jenkins!
Finished: SUCCESS
```

## Conclusion
Successfully configured Jenkins to retrieve and execute a shell script from GitHub.
