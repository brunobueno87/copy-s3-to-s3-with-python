import boto3

s3 = boto3.resource('s3')
copy_source = {
    'Bucket': 's3-de-origem',
    'Key': f'caminho/no/s3-de-origem/arquivo'
 }
s3.meta.client.copy(copy_source, 's3-de-destino', f'caminho/no/s3-de-destino/arquivo.csv')
