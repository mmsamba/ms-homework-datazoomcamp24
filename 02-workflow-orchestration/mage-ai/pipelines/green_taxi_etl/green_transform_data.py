if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    print( "rows with zero passengers BEFORE : " , data['passenger_count'].isin([0]).sum())
    data =  data[data['passenger_count']>0]
    print( "rows with zero passengers AFTER : " , data['passenger_count'].isin([0]).sum())

    
    print( "rows with zero trip_distance BEFORE : " , data['trip_distance'].isin([0]).sum())
    data = data[data['trip_distance']>0]
    print( "rows with zero trip_distance AFTER : " , data['trip_distance'].isin([0]).sum())
    
    print(data.columns)

    data.columns = (data.columns
                    .str.replace('ID','_id')
                    .str.lower()
    )

    # transforme en date formant string la colonne que pyarrow peut utiliser lors de export load to gcs
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    #data[data['vendor_id']==2]
    print( "rows with vendor_id = 1 : " , data['vendor_id'].isin([1]).sum())
    print( "rows with vendor_id = 2 : " , data['vendor_id'].isin([2]).sum())
    print( "rows with vendor_id = 3 : " , data['vendor_id'].isin([3]).sum())
    print( "rows with vendor_id = 4 : " , data['vendor_id'].isin([4]).sum())
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert ('vendor_id' in output.columns) == True , 'There are rides with zero passengers'
    assert output['passenger_count'].isin([0]).sum() == 0 , 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0 , 'There are rides with zero trip_distance'
