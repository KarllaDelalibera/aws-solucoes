import boto3

from moto import mock_athena

from athena import driver


@mock_athena
def test_athena_get_query_execution_id():
    athena_driver = driver.Driver()

    client = boto3.client("athena", region_name="us-east-1")

    query = "SELECT stuff"
    bucket = "mybucket"

    result = athena_driver.athena_get_query_execution_id(client, query, bucket)

    assert isinstance(result, str)
