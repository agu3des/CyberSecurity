import os

#receber os dois valores
numi = int(input())
numf = int(input())

#criar o processo filho, através de um fork
pid = os.fork()

#para o filho
if pid == 0:
  #crie uma lista
    pares = []
    for i in range(numi, numf +1): 
      #se par, adicione os números na lista
      if i % 2 == 0:
        pares.append(i)   
    print()
    #abrindo o arquivo temporário, escreva os números
    with open("/tmp/pares.txt", "w") as arqPares:
      for numero in pares:
        arqPares.write(str(numero) + "\n")
#para o pai
elif pid > 0:
  #fique em espera até o término do filho
  os.wait()
  #abra o arquivo e o leia
  with open('/tmp/pares.txt','r') as arqPares:
    #mostre o conteúdo do arquivo
    print(f'Os números pares entre {numi} e {numf} são:\n{arqPares.read()}')
#caso não entre nessas condições cancele
else:
  exit()