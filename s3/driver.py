import pandas as pd


class Driver:
    def read_file_csv(self, conn, bucket, path, dtype=None):
        """Lê um arquivo .csv localizado no S3.
        Arguments:
            conn {}: boto3 client s3.
            bucket {str} -- Nome do bucket que encontra-se o arquivo.
            path {str} -- Caminho que encontra-se o arquivo.

        Keyword Arguments:
            dtype {dict} -- Tipo de cada coluna. (default: {None})
        Returns:
            dataframe -- Retorna um dataframe com as informações do arquivo,
        """
        obj = conn.get_object(Bucket=bucket, Key=path)
        data = pd.read_csv(obj["Body"], sep=",", low_memory=False, dtype=dtype)
        return data
