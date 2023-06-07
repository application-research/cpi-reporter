# cpi-reporter
This reporting script is intended to be deployed using either Docker or Kubernetes.

To use it, you must have a working FDI installation (formerly known as Estuary Hosted Infrastructure).

## Prerequisites
* Working Gitea server, and customer lists tracked using it
* Working FDI installation
* Working Kubernetes cluster

## Getting started
* Deploy the manifests, modifying them as appropriate
* Set up a Kubernetes secret in the appropriate namespace
`kubectl create secret generic gitea-api-key --from-literal=GITEA_API_KEY=<your-api-key> -n <your-namespace>`