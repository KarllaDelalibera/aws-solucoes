import time


class Driver:
    def athena_get_query_execution_id(self, conn, query, bucket):
        """Executa uma consulta no athena
        Arguments:
            conn {}: boto3 client athena.
            query {str} -- Consulta SQL na qual deseja executar.
            path_output {str} -- Caminho completo na qual deseja
                                 armazenar o resultado.

        Returns:
            {str} -- ID da query
        """
        path_output = "s3://{}".format(bucket)
        response_query = conn.start_query_execution(
            QueryString=query, ResultConfiguration={"OutputLocation": path_output}
        )

        return response_query["QueryExecutionId"]

    def athena_check_query_status(self, conn, id_query, counter=900):
        """Verifica o status de consulta no athena.
        Arguments:
            conn {}: boto3 client athena.
            QueryExecutionId {str} -- id da query.

        Keyword Arguments:
            counter {int} -- Número máximo de vezes que
                             será verificado o status
                             da consulta. (default: {900})

        Returns:
            str -- Retorna o status da consulta.
        """
        for _ in range(0, counter):
            query_status = conn.get_query_execution(QueryExecutionId=id_query)

            if query_status["QueryExecution"]["Status"]["State"] == "SUCCEEDED":
                result = "SUCCEEDED"
                break
            elif query_status["QueryExecution"]["Status"]["State"] == "FAILED":
                result = "FAILED"
                break
            elif query_status["QueryExecution"]["Status"]["State"] == "CANCELLED":
                result = "CANCELLED"
                break
            time.sleep(1)
        return result
