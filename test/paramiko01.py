import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.56.1',port=10022,username='root',password='geostar')

stdin,stdout,stderr = ssh.exec_command('ifconfig')

res = stdout.read().decode('utf-8')

print(res.split())
ssh.close()
