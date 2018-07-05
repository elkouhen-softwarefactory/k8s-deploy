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

###  Installation de Helm

```bash
ansible-playbook -vv softwarefactory.yml -i inventories/prod/02-helm
```

Attendre la fin de l'installation de Helm

=> L'exécution de 'helm list' ne termine pas en erreur

```bash
[root@vps242131 ~]#helm list
```

###  Installation de Ingress

```bash
ansible-playbook -vv softwarefactory.yml -i inventories/prod/03-ingress
```

### Installation du manager de certificats 

```bash
ansible-playbook -vv softwarefactory.yml -i inventories/prod/04-cert
```

### Installation des services de l'usine

```bash
ansible-playbook -vv softwarefactory.yml -i inventories/prod/05-softwarefactory
```

## Liste des Machines

* vps242131 20 Go (master kubernetes)
* vps242565 10 Go 
* vps267690 10 Go
* vps242130 40 Go
* vps257315 40 Go
* vps242564 10 Go
* vps267694 10 Go
