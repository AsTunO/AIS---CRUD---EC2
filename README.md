# AIS---CRUD---EC2

EC2 é o serviço de computação da AWS.
AMI é a imagem usada para criar instâncias, contendo o sistema operacional e aplicações.
Tipos de Instâncias como t2 e t3 são categorias de máquinas virtuais com diferentes capacidades de CPU e memória, otimizadas para vários tipos de cargas de trabalho.

aws ec2 describe-images --owners amazon --region sa-east-1 --query 'Images[*].[ImageId, Name]' --output table

ami-0fe7a5c8ab7439490

pip install boto3
pip install awscli
aws configure
