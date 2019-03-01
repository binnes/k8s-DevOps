# Creating the DevOps env

## Creating the supporting components for the devops environment

1. Create a new namespace
   1. Run command ```kubectl create -f manifests/devops-setup/namespace-devops.yaml```
2. Create the storage claim - this is where all data will be stored for devops
    2. Run command ```kubectl create -f manifests/devops-setup/storage-devops.yaml```

TODO : service account and rbac config?

## Creating the source control capability with Gitea

1. Install the Gitea deployment
   - Run command ```kubectl create -f manifests/gitea/gitea-deployment.yaml```
2. Create the service for gitea
   - Run command ```kubectl create -f manifests/gitea/gitea-service.yaml```
3. Create an entry in /etc/hosts for gitea.  Get the IP address from command:
   - Run Command ```kubectl get services -n devops``` to get the external IP address
4. Launch a browser with the external IP address or name you created in /etc/hosts, we configured the http service to be exposed on port 8080, so add :8080 to the address, e.g. If you used a /etc/hosts entry with **gitea.k8s.home** as the host that maps to the external address, then the URL is : **http://gitea.k8s.home:8080/**
5. Hit the register button, where you will be asked to complete the initial setup.  Select sqlite3 as the database and set the base URL to match you /etc/hosts entry or enter the external IP address, e.g. : **http://gitea.bi-k8s.home:8080/**
6. Wait for the setup to complete, then you can access gitea with the base URL set in the previous set.  Create yourself a user account with the register link to start using gitea.

## Creating the Jenkins CI

