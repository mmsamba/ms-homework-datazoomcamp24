import os
import pandas as pd
from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    filepath = '/home/src/data'

    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }

    # native date parsing 
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    

    data = pd.DataFrame()
    #data = pd.read_csv('/home/src/data/green_tripdata_2020-09.csv.gz')
    #df2 = pd.read_csv('/home/src/data/green_tripdata_2020-11.csv.gz')

    #data = pd.concat([df1,df2],axis=0)
    for filename in os.listdir(filepath):
        f = os.path.join(filepath, filename)
        if os.path.isfile(f) and filename.endswith('.csv.gz')  and "green_tripdata_2020-1" in filename:
            print(f)
            print(filename)
            pdTemp = pd.read_csv(f, sep=',', compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates)
            data = pd.concat([data,pdTemp])
            print(len(data))
            
  
    return data
    #return FileIO().load(filepath)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
