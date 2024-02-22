import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter



os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/.gc/mage-zoomcamp-ms-xx-xxxx-xx-29.json'
bucket_name = 'mage-zoomcamp-ms'
#object_key = 'nyc_yellow_taxi_data.parquet'
project_id = 'mszoomcamxxxx'
table_name = 'green_taxi_data' # pyarrom utilise cette table pour partitionner

root_path = f'{bucket_name}/{table_name}'


@data_exporter
def export_data(data, *args, **kwargs):

    # lecture de notre dataframe dans un pyarrow table
    table = pa.Table.from_pandas(data) # table utilisée par pyarrow

    gcs = pa.fs.GcsFileSystem() # we need the file system object. autozise l'utilisation des variables envionnement automtiquement

    pq.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols = ['lpep_pickup_date'] ,
        filesystem = gcs

    )


