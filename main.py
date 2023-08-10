
import boto3

client = boto3.client('service-quotas')

def get_services_list():
    # Get list of service codes
    # ------------------------------
    paginator = client.get_paginator('list_services')
    page_iterator = paginator.paginate(
        PaginationConfig={
            'PageSize': 100,
        }
    )
    
    services = []
    for response in page_iterator:
        services.extend(response.get('Services', []))

    return services
    
services = get_services_list()
with open('aws_services.txt', 'w') as f:
    f.writelines([', '.join([v for k, v in s.items()])+'\n' for s in services])
    

def list_service_quotas(service_code):
    # Get a service's quotas
    # -------------------------------
    paginator = client.get_paginator('list_service_quotas')
    page_iterator = paginator.paginate(
        ServiceCode=service_code,
        PaginationConfig={
            'PageSize': 100,
        }    
    )
    
    quotas = []
    for response in page_iterator:
        quotas.extend(response.get('Quotas', []))
    
    return quotas
    
    
quotas = list_service_quotas('es')
print(quotas)