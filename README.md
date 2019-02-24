# Software Factory

Ce projet contient les sources ansible de déploiement de notre usine.

## Installation

## Opérations de maintenances

### Pré requis

Créer un fichier contenant le mot de passe du vault (à demander à Mehdi et ne pas divulguer bien sûr !!!)

Créer une variable d'environnement qui pointe sur ce fichier.

```bash
export ANSIBLE_VAULT_PASSWORD_FILE=.vault.txt
```

###  Installation du cluster Kubernetes

```bash
ansible-playbook -vv softwarefactory.yml -i inventories/prod/01-cluster
```

Attendre que tous les noeuds soient Ready

```bash
[root@vps242131 ~]# kubectl get nodes 
NAME                STATUS    ROLES     AGE       VERSION
vps242130.ovh.net   Ready     <none>    13h       v1.11.0
vps242131.ovh.net   Ready     master    13h       v1.11.0
vps242564.ovh.net   Ready     <none>    13h       v1.11.0
vps242565.ovh.net   Ready     <none>    13h       v1.11.0
vps257315.ovh.net   Ready     <none>    13h       v1.11.0
vps267690.ovh.net   Ready     <none>    13h       v1.11.0
vps267694.ovh.net   Ready     <none>    13h       v1.11.0
```

### Dashboard 

Exécution d'un proxy vers l'API Kubernetes API
```bash
kubectl proxy
```

URL du dashboard
```bash
http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/
```

Token de connexion
```bash
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep admin-user | awk '{print $1}')
```bash
