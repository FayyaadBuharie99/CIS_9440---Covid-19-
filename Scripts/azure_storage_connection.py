pip install azure-storage-blob

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

def upload_to_azure_storage(account_name, account_key, container_name, blob_name, file_path):
    try:
        # Create a BlobServiceClient using the storage account's name and key
        blob_service_client = BlobServiceClient(
            account_url=f"https://{account_name}.blob.core.windows.net",
            credential=account_key
        )

        # Get a reference to the container where the blob will be uploaded
        container_client = blob_service_client.get_container_client(container_name)

        # Upload the file to Azure Blob Storage
        with open(file_path, "rb") as data:
            blob_client = container_client.upload_blob(name=blob_name, data=data)

        print(f"Uploaded {blob_name} to Azure Blob Storage in container {container_name}.")
    except Exception as e:
        print(f"An error occurred while uploading to Azure Blob Storage: {e}")

# Azure Storage Configuration
account_name = "your_storage_account_name"
account_key = "your_storage_account_key"
container_name = "your_container_name"
blob_name = "your_blob_name.json"
file_path = r"path_to_your_json_file.json"  # Update with your JSON file path

# Upload the JSON file to Azure Blob Storage
upload_to_azure_storage(account_name, account_key, container_name, blob_name, file_path)
