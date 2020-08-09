import boto3


class Driver:

    def assumed_role_session(self, role_arn, name_session_role):
        """Função responsavel por assumir uma role com base no ARN,
           e retornará uma sessao pre-autenticada.
        Args:
            role_arn (string): ARN da role na qual deseja assumir.
            name_session_role (string): Nome da sessão assumida.

        Returns:
            Uma sessao pre-autenticada.
        """        
        sts_client = boto3.client('sts', region_name='us-east-1')
        role = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=name_session_role)
        credentials_role = role['Credentials']
        
        aws_access_key_id = credentials_role['AccessKeyId']
        aws_secret_access_key = credentials_role['SecretAccessKey']
        aws_session_token = credentials_role['SessionToken']
        
        session = boto3.session.Session(aws_access_key_id=aws_access_key_id,
                                        aws_secret_access_key=aws_secret_access_key,
                                        aws_session_token=aws_session_token)
        return session
