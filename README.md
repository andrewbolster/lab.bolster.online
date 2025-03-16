# lab.bolster.online

[![Infrastructure](https://github.com/andrewbolster/lab.bolster.online/actions/workflows/infrastructure.deploy.yaml/badge.svg)](https://github.com/andrewbolster/lab.bolster.online/actions/workflows/infrastructure.deploy.yaml)

[![Example CI/CD Pipeline for Hello World App](https://github.com/andrewbolster/lab.bolster.online/actions/workflows/hello_world.deploy.yaml/badge.svg)](https://github.com/andrewbolster/lab.bolster.online/actions/workflows/hello_world.deploy.yaml)

This is an infrastructure project for creating a 'self service' k8s / gcp deployment and management environment.

## Features

### Persistent Volumes

Add the following to your values.yaml to create a persistent volume claim:

```yaml
persistentVolume:
  enabled: true
  mountPath: /mnt/data
  capacity: 1Gi
```

Default storage class is standard-rwo (i.e. spinning platters, not ssd), and capacity is limited at the service level

### Environment Passthrough from Github Secrets

To pass 'sensitive' environment variables to the cluster, we use the [`yaml-update-action`](https://github.com/marketplace/actions/yaml-update-action) to inject secrets (or any envvars) at deploy time into the `values.yaml` at deploy time. 

THIS DOES NOT USE KUBERNETES SECRETS SO YMMV

## TODO

- [X] Persistent Volumes
- [X] lab.bolster.online
- [ ] Postgres DB (Per Service)
- [ ] Postgres DB (Shared)
- [ ] Redis DB (Per Service)
- [ ] Redis DB (Shared)
- [ ] Backstage.io
- [ ] [Tailscale Operator](https://tailscale.com/kb/1236/kubernetes-operator)
- [ ] Multi-Kubernetes Cluster (i.e. run on that bunch of pi's in the house via tailscale)