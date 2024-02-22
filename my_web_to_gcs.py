import io
import os
import requests
import pandas as pd
from google.cloud import storage


"""
Pre-reqs: 
1. `pip install pandas pyarrow google-cloud-storage`
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""

# services = ['fhv','green','yellow']
#init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'
#init_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'
#https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-01.parquet

#init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv/' # NE FONCTIONNE PAS POUR CE CODE

init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/' 

# switch out the bucketname
BUCKET = os.environ.get("GCP_GCS_BUCKET", "04-analytics-engineering")


#        'extra':float,   -> float possible

taxi_dtypes = {     'dispatching_base_num':str,
                    'PUlocationID':pd.Int64Dtype(),
                    'DOlocationID':pd.Int64Dtype(),
                    'SR_Flag': pd.Int64Dtype(),
                    'Affiliated_base_number': str
                }

# native date parsing 
parse_dates = ['pickup_datetime', 'dropOff_datetime']



def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    # storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    # storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)
    
    
def extract(year, service):
    #for i in [1]:
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # csv file_name
        file_name = f"{service}_tripdata_{year}-{month}.csv.gz"
        #file_name = f"{service}_tripdata_{year}-{month}.parquet"

        print(f"urlfilename extaract: {file_name}")

        # download it 
        os.system(f"wget {init_url}{file_name} -O {file_name}")
    
    print(f"END extract ")
        
    
def transform(year,service):
    #for i in [1]:
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # csv file_name
        file_name = f"{service}_tripdata_{year}-{month}.csv.gz"
        file_name_to = f"{service}_tripdata_{year}-{month}.parquet"

        print(f"urlfilename before read   : {file_name}")
        #df = pd.read_csv(file_name, sep=',', compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates)
        df = pd.read_csv(file_name, sep=',', compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates)
        print(f"urlfilename tansform  : {file_name}")
        print(df.head(10))
       
        df.to_parquet(file_name_to) 
        print(f"urlfilename tansform saveed  : {file_name_to}")
    
    print(f"END TRANSFORM ")
        
    

def web_to_gcs(year, service):
    
    #for i in [1]:
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # csv file_name
        #file_name = f"{service}_tripdata_{year}-{month}.csv.gz"
        file_name = f"{service}_tripdata_{year}-{month}.parquet"

        print(f"filename load: {file_name}")

        
        # upload it to gcs 
        upload_to_gcs(BUCKET, f"{service}/{year}/{file_name}", file_name)

        print(f"GCS load: {service}/{year}/{file_name}")
    
    print(f"END LOAD ")

#web_to_gcs('2019', 'green')
#web_to_gcs('2020', 'green')
# web_to_gcs('2019', 'yellow')
# web_to_gcs('2020', 'yellow')

#web_to_gcs('2022', 'green')

extract('2019', 'fhv')
transform('2019', 'fhv')
web_to_gcs('2019', 'fhv')

# wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz
# wget https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv/fhv_tripdata_2019-01.csv.gz



