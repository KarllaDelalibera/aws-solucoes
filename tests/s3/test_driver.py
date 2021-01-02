import boto3
import pandas as pd

from moto import mock_s3

from s3 import driver


@mock_s3
def test_read_file_csv():
    classe_read_file = driver.Driver()

    bucket = "mybucket"
    path = "test/file_1.txt"

    conn = boto3.client("s3", region_name="us-east-1")
    conn.create_bucket(Bucket=bucket)
    conn.put_object(Bucket=bucket, Body=b"ABCD", Key=path)

    data_frame = classe_read_file.read_file_csv(conn, bucket, path)

    assert isinstance(data_frame, pd.DataFrame)
