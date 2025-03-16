# Command Log

## GCloud/Google Cloud SDK/Kubectl setup

`brew install --cask google-cloud-sdk`
`gcloud init`
`gcloud auth login` # This will prompt you to select or create a Google Cloud project, I created a new project called `bolsterlab`
`gcloud components install kubectl`
 
 Visit [GCP Compute Engine API](https://console.cloud.google.com/marketplace/product/google/compute.googleapis.com) and enable the API.

 `gcloud config set project bolsterlab`

 ## GKE Cluster initialisation
`gcloud container clusters create bolsterlab-cluster --num-nodes=3 --zone=europe-west2-b`
`gcloud container clusters get-credentials bolsterlab-cluster --zone=europe-west2-b` # Probably unnecessary but just to be sure

## Helm setup
`brew install helm`
`helm repo add stable https://charts.helm.sh/stable`
`helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx`
`helm repo add jetstack https://charts.jetstack.io`
`helm repo update`
`helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
`kubectl get svc -w -n ingress-nginx` # Wait for the external IP to be assigned

## Cert Manager setup

Check [here](https://cert-manager.io/docs/installation/helm/#2-install-cert-manager) for the latest version of cert-manager

`
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.17.0 \
  --set crds.enabled=true
`

## CR setup
`gcloud services enable containerregistry.googleapis.com`

Create Service account from GCP IAM & Admin and assign Storage Admin, Artifact Registry Create-on-Push Writer, and Kubernetes Engine Service Agent roles; download the JSON key and Add it to the GitHub secrets as `GCR_JSON_KEY`

**NOTE** If you're doing this in a multi user environment you might not want to use the 'Create on Push' role as it will allow anyone to create a repository in the registry, which might let people skip over livecycle/security monitoring

Update your KUBECONFIG with the following command:
`gcloud container clusters get-credentials bolsterlab-cluster --zone europe-west2-b --project bolsterlab`

and add the contents to ~/.kube/config to Github secrets as `KUBECONFIG` (Don't do anything funny with quotes, leave it 'bare')

~Manually create a 'labs' repository in GCR (I did it in London region so the PKG_REPO is europe-west2-docker.pkg.dev)~ might be unnecessary with the 'Create on Push' role

## DNS Setup

Domain controller of choice (I use Digital Ocean)

Get your ingress-nginx-controller `$EXTERNAL-IP` with `kubectl get svc -n ingress-nginx`

Set the following A records:
- `lab.bolster.online` -> `$EXTERNAL-IP` : Required if you want to host your own top-level lab, e.g. helm charts, docs, etc (possibly even Backstage later)
  - Note: I already have a github root domain so I needed to set a `CNAME` record pointing to that domain to host `lab.bolster.online` using GithubPages but YMMV
- `*.lab.bolster.online` -> `$EXTERNAL-IP` : Required for the wildcard subdomain routing to the services (cert-manager and ingress-nginx will handle the SSL)

# Other Junk
* Creation of 'hello-world' app
* Creation of 'service-chart' helm chart
* Creation of k8s/manifests
* Creation of helm/values
* Update default machine type from e2 medium to e2 micro  `gcloud container node-pools update default-pool --cluster bolsterlab-cluster --machine-type e2-micro`