## Create rg
az group create --name rg-store-oai --location swedencentral


az aks create --resource-group rg-store-oai --name aksstore --generate-ssh-keys

az aks get-credentials --resource-group rg-store-oai --name aksstore

kubectl get nodes

kubectl apply -f ./aks-store-all-in-one.yaml

### Edit ai-service info

kubectl apply -f ai-service.yaml


kubectl get pods

kubectl get service store-admin

kubectl get service store-front

## add product
Indestructable chew toy
puppy dog chew toy teething training