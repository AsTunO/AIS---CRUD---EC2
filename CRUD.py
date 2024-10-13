import boto3  # Importa a biblioteca boto3 para interagir com a AWS
from botocore.exceptions import ClientError  # Importa a exceção ClientError para tratamento de erros

# Cria um cliente EC2 usando boto3
ec2 = boto3.client('ec2')

def criar_instancia(ami_id, instance_type):
    """
    Cria uma nova instância EC2.
    
    :param ami_id: ID da Amazon Machine Image (AMI) a ser usada
    :param instance_type: Tipo da instância a ser criada (ex: t2.micro)
    """
    try:
        # Inicia a instância com a AMI e tipo especificados
        response = ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            MinCount=1,  # Número mínimo de instâncias a serem criadas
            MaxCount=1   # Número máximo de instâncias a serem criadas
        )
        # Obtém o ID da instância criada
        instance_id = response['Instances'][0]['InstanceId']
        print(f'Instância iniciada com ID: {instance_id}')
    except ClientError as e:
        # Trata erros relacionados à criação da instância
        print(f'Erro ao iniciar a instância: {e}')

def listar_instancias():
    """
    Lista todas as instâncias EC2 e seus estados.
    """
    response = ec2.describe_instances()  # Obtém informações sobre as instâncias
    # Itera sobre as reservas e instâncias
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Exibe o ID e estado da instância
            print(f'ID: {instance["InstanceId"]}, Estado: {instance["State"]["Name"]}')

def atualizar_tipo_instancia(instance_id, new_instance_type):
    """
    Atualiza o tipo de uma instância EC2 existente.
    
    :param instance_id: ID da instância a ser modificada
    :param new_instance_type: Novo tipo da instância
    """
    try:
        # Modifica o tipo da instância especificada
        ec2.modify_instance_attribute(InstanceId=instance_id, Attribute='instanceType', Value=new_instance_type)
        print(f'Tipo de instância atualizado para {new_instance_type} para a instância {instance_id}')
    except ClientError as e:
        # Trata erros relacionados à atualização do tipo da instância
        print(f'Erro ao atualizar o tipo da instância: {e}')

def terminar_instancia(instance_id):
    """
    Termina uma instância EC2.
    
    :param instance_id: ID da instância a ser terminada
    """
    try:
        # Termina a instância especificada
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f'Instância {instance_id} terminada.')
    except ClientError as e:
        # Trata erros relacionados à terminação da instância
        print(f'Erro ao terminar a instância: {e}')

def alterar_estado_instancia(instance_id, estado):
    """
    Altera o estado de uma instância EC2 (iniciar, parar, reiniciar ou terminar).
    
    :param instance_id: ID da instância a ser alterada
    :param estado: Novo estado da instância (start, stop, reboot, terminate)
    """
    try:
        if estado == 'start':
            # Inicia a instância
            ec2.start_instances(InstanceIds=[instance_id])
            print(f'Instância {instance_id} iniciada.')
        elif estado == 'stop':
            # Para a instância
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f'Instância {instance_id} parada.')
        elif estado == 'reboot':
            # Reinicia a instância
            ec2.reboot_instances(InstancesIds=[instance_id])
            print(f'Instância {instance_id} reiniciada.')
        elif estado == 'terminate':
            # Termina a instância
            terminar_instancia(instance_id)
        else:
            # Mensagem de erro para estado inválido
            print('Estado inválido. Use: start, stop, reboot, terminate.')
    except ClientError as e:
        # Trata erros relacionados à alteração do estado da instância
        print(f'Erro ao alterar o estado da instância: {e}')

def menu():
    """
    Exibe um menu de operações EC2 e gerencia as interações do usuário.
    """
    while True:
        # Exibe opções de operações disponíveis
        print("\nMenu de Operações EC2")
        print("1. Criar uma nova instância")
        print("2. Listar instâncias")
        print("3. Atualizar tipo de instância")
        print("4. Terminar instância")
        print("5. Alterar estado da instância")
        print("6. Sair")
        
        # Solicita a escolha do usuário
        escolha = input("Escolha uma operação (1-6): ")

        if escolha == '1':
            # Criação de uma nova instância
            ami_id = input("Digite o ID da AMI: ")
            instance_type = input("Digite o tipo da instância (ex: t2.micro): ")
            criar_instancia(ami_id, instance_type)
        elif escolha == '2':
            # Listagem de instâncias existentes
            listar_instancias()
        elif escolha == '3':
            # Atualização do tipo de uma instância
            instance_id = input("Digite o ID da instância a ser modificada: ")
            new_instance_type = input("Digite o novo tipo da instância: ")
            atualizar_tipo_instancia(instance_id, new_instance_type)
        elif escolha == '4':
            # Terminação de uma instância
            instance_id = input("Digite o ID da instância a ser terminada: ")
            terminar_instancia(instance_id)
        elif escolha == '5':
            # Alteração do estado de uma instância
            instance_id = input("Digite o ID da instância: ")
            estado = input("Digite o novo estado da instância (start, stop, reboot, terminate): ")
            alterar_estado_instancia(instance_id, estado)
        elif escolha == '6':
            # Saída do programa
            print("Saindo...")
            break
        else:
            # Mensagem de erro para escolha inválida
            print("Opção inválida. Tente novamente.")

# Execução do menu quando o script é chamado diretamente
if __name__ == '__main__':
    menu()
