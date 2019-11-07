#!/usr/bin/env python
import boto3
import pymysql

session = boto3.session.Session(profile_name="mtgstore")
client = session.client('rds', region_name='us-east-2')
token = client.generate_db_auth_token('database-ecommerce-mtg-apprenti-thirdtry.cebxmljii3h7.us-east-2.rds.amazonaws.com',3306,'masteruser')
ssl = {'ca': 'rds-combined-ca-bundle.pem'} 
print(token)
conexao = pymysql.connect(host='database-ecommerce-mtg-apprenti-thirdtry.cebxmljii3h7.us-east-2.rds.amazonaws.com',port=3306,user='masteruser',password=token, ssl=ssl)