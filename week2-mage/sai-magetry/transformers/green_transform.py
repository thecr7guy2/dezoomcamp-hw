import pandas as pd
import re 

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def is_camel_case(s):
    """
    Check if a string is in camel case.
    """
    return s != s.lower() and s != s.upper() and "_" not in s

def camel_to_snake(name):
    """
    Convert a string from camelCase to snake_case.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()



@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    null_values = data.isnull().sum()
    print(null_values)
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
  
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    newcolumns = []
    count =0
    for column in list(data):
        if is_camel_case(column):
            newcolumns.append(camel_to_snake(column))
            count = count + 1
        else:
            newcolumns.append(column)
    data.columns = newcolumns

    print(data["vendor_id"].value_counts())
    print(count)
    

    data= data.drop('ehail_fee', axis=1)

    return data


@test
def test_vendor_id_exists(output, *args) -> None:
    assert 'vendor_id' in output.columns, "The column 'vendor_id' does not exist in the Data."
    
@test
def passenger_count_test(output, *args) -> None:
    assert (output['passenger_count'] > 0).all(), "Some entries in 'passenger_count' are not greater than 0."

@test
def trip_distance_test(output, *args) -> None:
    assert (output['trip_distance'] > 0).all(), "Some entries in 'trip_distance' are not greater than 0."