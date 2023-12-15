## Create rg
az group create --name rg-store-oai --location northeurope


az aks create --resource-group rg-store-oai --name aksstore --os-sku AzureLinux --generate-ssh-keys

az aks get-credentials --resource-group rg-store-oai --name aksstore

kubectl get nodes

kubectl apply -f ./aks-store-all-in-one.yaml

### Edit ai-service info

kubectl apply -f ai-service.yaml


kubectl get pods

kubectl get service store-admin

kubectl get service store-front

## secure access
[walkthrough](https://moaw.dev/workshop/?src=gh%3Apauldotyu%2Fmoaw%2Fsecure-aoai-aks%2Fworkshops%2Fsecure-aoai-aks%2F&step=0)
show why (openai key is in plain text)
```shell
kubectl describe pod --selector app=ai-service
```

# Get the Azure OpenAI resource group name
RG_NAME=rg-store-oai

# Get the Azure OpenAI resource id
AOAI_RESOURCE_ID=$(az resource list \
  --resource-group $RG_NAME \
  --resource-type Microsoft.CognitiveServices/accounts \
  --query "[0].id" -o tsv)

# Add yourself as a Cognitive Services OpenAI User
az role assignment create \
  --role "Cognitive Services OpenAI User" \
  --assignee $(az account show --query user.name -o tsv) \
  --scope $AOAI_RESOURCE_ID


## add product
Indestructable chew toy
puppy dog chew toy teething training


curl -X POST "http://localhost:5001/generate/description" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":\"Seafarer's Tug Rope\",\"tags\":[\"toy\",\"dog\"]}"


* Install
```shell
.\kubeshark.exe tap 
```

* Open dashboard
```shell
.\kubeshark.exe proxy
```

* Clean up
```shell
.\kubeshark.exe clean
```