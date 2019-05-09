#!/bin/bash
set -e
# Check version in https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/
# Search "Running kubeadm without an internet connection"
# For running kubeadm without an internet connection you have to pre-pull the required master images for the version of choice:
KUBE_VERSION=v1.14.1
KUBE_PAUSE_VERSION=3.1
ETCD_VERSION=3.3.10
DNS_VERSION=1.3.1
VOLUME_NFS=0.8
GCR_URL=k8s.gcr.io
MIRRORS_URL=ccr.ccs.tencentyun.com/dy_tencent_hub

images=(kube-apiserver:${KUBE_VERSION}
kube-controller-manager:${KUBE_VERSION}
kube-scheduler:${KUBE_VERSION}
kube-proxy:${KUBE_VERSION}
pause:${KUBE_PAUSE_VERSION}
etcd:${ETCD_VERSION}
coredns:${DNS_VERSION}
volume-nfs:${VOLUME_NFS})

for imageName in ${images[@]} ; do
  docker pull $MIRRORS_URL/$imageName
  docker tag  $MIRRORS_URL/$imageName $GCR_URL/$imageName
  docker rmi $MIRRORS_URL/$imageName
done

docker images