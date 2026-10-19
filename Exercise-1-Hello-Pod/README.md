

\# Exercise 1: Hello Pod — Kubernetes



\## Overview



This exercise is my first hands-on experience with Kubernetes.

I used Nginx to simulate a simple web application, similar to a

storefront that customers could access through their browser.



The goal was to run the application inside a Kubernetes Pod and

make it accessible using a Service.



\## Tools Used



\- Docker Desktop

\- Minikube

\- Kubernetes

\- kubectl

\- Nginx



\## What I Did



1\. Started a local Kubernetes cluster using Minikube.

2\. Created a Pod named `hello-k8s` using the Nginx image.

3\. Checked the Pod status to confirm that it was running.

4\. Exposed the Pod through a NodePort Service.

5\. Opened the application in a browser and checked the Nginx page.



\## Commands Used



```powershell

minikube start --driver=docker



kubectl run hello-k8s --image=nginx --port=80



kubectl get pods



kubectl expose pod hello-k8s --type=NodePort --port=80



kubectl get services



minikube service hello-k8s

```



\## Files in This Exercise



\- `pod.yaml` — Defines the Nginx Pod.

\- `service.yaml` — Exposes the Pod through a NodePort Service.



\## What I Learned



\- A Pod is the basic unit used to run workloads in Kubernetes.

\- A container image provides the application environment.

\- A Service provides a stable way to access a Pod.

\- Minikube lets me practise Kubernetes on my local machine.



\## Result



The Nginx application ran successfully in my local Kubernetes

cluster, and I was able to access the Nginx welcome page through

my browser.



