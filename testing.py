#!/usr/bin/env python
import boto3
import psycopg2

session = boto3.session.Session()
client = session.client('rds', region_name='us-east-2')
token = client.generate_db_auth_token('database-django-apprenti-testing-fifthtry.cebxmljii3h7.us-east-2.rds.amazonaws.com',5432,'djangoapp')
ssl = {'ca': 'rds-combined-ca-bundle.pem'} 
print(token)
conexao = psycopg2.connect(host='database-django-apprenti-testing-fifthtry.cebxmljii3h7.us-east-2.rds.amazonaws.com',port=5432,user='djangoapp',password=token, database="django")