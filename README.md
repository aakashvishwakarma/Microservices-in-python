# Microservices-in-python

-Install python 3.x.
-Create Python Virtual Env.
-Install python VS code extension.
-Sample Flask App.
-Jinja templating for Dynamic web pages.
-Using PIP to freeze dependencies.
-Building Docker images using Dockerfile.
-Writing Docker Compose file.
-Writing Kubernetes manifest files for the app.
-Create Helm chart.

# To Build using Docker Compose
- run command docker-compose build (make sure dockercompose file is available in that dir where you are running the cmnd) then run docker-compose up -d and you can see the runnning container by running docker ps
- to bring complete thing down run docker-compose down  
    

# Kubernetes can be used via docker desktop 
- Start it in setting on Docker desktop

- cmnds: change into kubernetes dir and run-> kubectl apply -f deployment.yml and then kubectl apply -f deployment.yml
- to check the pods and service and ports of pods run: kubectl get po,svc


- TO delete the pod and service use command : kubectl delete -f .

# Using Helm 
- First if you don't have helm then install it from this git repo by downloading the respecting binary file as per your OS. Then extract it to any folder and set the PATH in enviroment variable.
- Git for Helm binary-> https://github.com/helm/helm/releases
- Helm is installed now create a template first using command-> helm create webapp , webapp is name of template. 
This command will create a folder with name "webapp" in your working dir with lot of dir and files so use only that is required.
- After making the required changes on helm chart now time to render it to check any errors or typos in helm chart
use command: helm template webapp (webapp name of help template created above). 
- Once everything is okay now time to install/release the helm chart using command: helm install web webapp ( web is name of release and webapp the template).
- Now to see the relaese type command -> helm list

- Now you can check using above kubectl coomand the pods.

- Now if you wanted to deleted the helm release use the command-> helm unistall web( web is name of relase we given in install time)

# Commands used...
1. git clone
2. pip install -r requirement.txt and then run python app.py locally. OR 
3. Build docker image using above docker commands. OR
4. Use Docker compose or Kuberentes or Helm to run.