# Command Log

## GCloud/Google Cloud SDK/Kubectl setup

`brew install --cask google-cloud-sdk`
`gcloud init`
`gcloud auth login` # This will prompt you to select or create a Google Cloud project, I created a new project called `bolsterlab`
`gcloud components install kubectl`
 
 Visit [GCP Compute Engine API](https://console.cloud.google.com/marketplace/product/google/compute.googleapis.com) and enable the API.

 `gcloud config set project bolsterlab`
`gcloud container clusters create bolsterlab-cluster --num-nodes=3 --zone=europe-west2-b`
`gcloud container clusters get-credentials bolsterlab-cluster --zone=europe-west2-b` # Probably unnecessary but just to be sure

# Helm setup
`brew install helm`
`helm repo add stable https://charts.helm.sh/stable`
`helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx`
`helm repo add jetstack https://charts.jetstack.io`
`helm repo update`
`helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
`kubectl get svc -w -n ingress-nginx` # Wait for the external IP to be assigned

# Cert Manager setup

Check [here](https://cert-manager.io/docs/installation/helm/#2-install-cert-manager) for the latest version of cert-manager

`
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.17.0 \
  --set crds.enabled=true
`

# CR setup
`gcloud services enable containerregistry.googleapis.com`

Create Service account from GCP IAM & Admin and assign Storage Admin role; download the JSON key and Add it to the GitHub secrets as `GCR_JSON_KEY`

Update your KUBECONFIG with the following command:
`gcloud container clusters get-credentials bolsterlab-cluster --zone europe-west2-b --project bolsterlab`

and add the contents to ~/.kube/config to Github secrets as `KUBECONFIG`


# Other Junk
* Creation of 'hello-world' app
* Creation of 'service-chart' helm chart
* Creation of k8s/manifests
* Creation of helm/values
  