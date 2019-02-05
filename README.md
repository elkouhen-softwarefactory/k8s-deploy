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

Vérifier la création des certificats 

```bash
[root@vps242131 ~]# kubectl describe certificate certificate
BLA BLA BLA
    Message:               Certificate issued successfully
BLA BLA BLA    

```

Vérifier la création du secret contenant le certificat créé

```bash
[root@vps242131 ~]# kubectl describe secret certificate
Name:         certificate
Namespace:    default
Labels:       <none>
Annotations:  certmanager.k8s.io/alt-names=jenkins.k8.wildwidewest.xyz,nexus.k8.wildwidewest.xyz
              certmanager.k8s.io/common-name=jenkins.k8.wildwidewest.xyz
              certmanager.k8s.io/issuer-kind=ClusterIssuer
              certmanager.k8s.io/issuer-name=letsencrypt-issuer

Type:  kubernetes.io/tls

Data
====
tls.crt:  3862 bytes
tls.key:  1679 bytes
```

### Installation des services de l'usine

```bash
ansible-playbook -vv softwarefactory.yml -i inventories/prod/06-softwarefactory
```

