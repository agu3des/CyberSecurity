# Protocolos de Interconexão de Redes de Computadores

→ 3 avaliações:

- 1º Prova

- 2º Prova

- 3º Projeto (equipe/apresentação/ protocolo de transporte e de aplicação e o que a aplicação faz)

REVISÃO DE PROTOCOLO IP:

→ Cada interface de rede tem seu próprio endereço IP

→ Para ser roteador tem que participar de pelo menos 2 interfaces de rede, todo ele é um multihome, ex. celular (apenas quando você ativa a função de roteamento). Repassam pacotes entre redes das quais participa.

→ Multihomes podem ser ou não roteador

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeuHdRWmAQecX9kCWkzUbnbCedReH6ltAGMNnxAbndtjKplciNLXdZgAJm-nlIFC31dsepUEWK3R6aM1ebPNifOXb8mR7Z1rT5PYo3u8-pOZed5Z6KFbWOV6TEHgrPZzXaizcZUEcxvh6z1FCBK9NuG7Vba?key=4SgRub88vuVdpJD_jcqH_A)

**161.12 e 161.1 = 161.5 / 1º rede**

**160.8 = 160.1 / 2º rede**

**168.1.1 e  168.1.2 / 3º rede**

**166.5 e 166.15 = 166.10 / 4º rede**

→ Endereço da Rede: bota 0 nos bits de host, ex. 200.15.161.0

→ Endereço da Máquina: bota o endereço que indica o host nos bits 200.15.161.12

→ Antes: classes A (128 - 10000000), B (10 - 00001010) e C (200 - 11001000), são definidas pelos bits iniciais do número em binário.

→ Após a máscara de rede, a máscara que define o que é parte da rede e parte do host

→ Se a parte da rede do endereço de destino e de origem forem iguais não precisa de roteador, é direto.

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfQysOpb82D3Bdgm-DLkoEN72IE1q5I1TEzt5uqIV_G13bnG9q40RoHuKWGYzlM3JTTcs8FoQQ5ergOUOw1WF2aorseWdwYza4ABb6atWVqP0xuJD8yW6D0n3d0tTLw_5axj5A44VpW1B3rHxPaqyYlYuDV?key=4SgRub88vuVdpJD_jcqH_A)

→ Todo roteador tem que ser uma máquina dentro da minha rede, de modo que possua acesso direto a ela.

Pacote → Máquina

Quadro → Roteador

→ Máquinas diferentes: envia  dados para o roteador, utiliza o ARP, para procurar a máquina que possui esse endereço, após encontrá-la, o endereço é salvo na tabela ARP

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdCAVAM5TALwY_0QK_480CSNEmVIFKtDT6RWi6DdW9PTIVL8dpd_F-ym_F4Jjcs6oiXbjCZbuWOd4eLDbWBw1yq-OVEn9uEbuZTd32o6PBRVf48UrOlTtU5sXz6kAeBfiY6rYWqwDjbpPd2wEIy_bqI3Gd0?key=4SgRub88vuVdpJD_jcqH_A)

👆🏻reinframe: reinquadrar

SUBREDES:

- São necessárias pois as formas como as redes ip foram criadas apresentam problemas em relação ao tamanho dessas e o próprio desempenho que elas possuem.
- Problemas com grandes redes = solução → dividir essas redes em tamanhos menores, de modo a ser trabalhado com pequenas redes ligadas a roteadores.
- Pode trabalhar com máscaras de redes de valores diferentes.
- Máscara de Rede: padrão de bits no ipv4 é de 32 bits.

Os bits em 1 correspondem no endereço ip a partes de endereço da rede, os que forem 0 correspondem a endereçamento do host. Para que se possa diferenciar as partes do net-id e do host-id.

- EX: classe B com máscara de 24 bits

1111 1111  1111 1111  1111 1111  0000 0000 = um total de 256 endereços e 254 hosts / 255.255.255.0

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdhJwUjopDaAcyn2f5ubAUSYfzsabijk55ditvQH4pyX97oHg7nnhpXJjidBqiuEtT7_T8vVevhRFcvLBr_JdAwVbvNUmbAOdzE-8M9DWp_UBfdRdMUDl_BmKS0iOlmhprtQ7stmCUrSgoxOs_6qSyzu_2V?key=4SgRub88vuVdpJD_jcqH_A)

- Subnet-id : Pode ser de tamanho fixo nas flsn ou de tamanho variado nas vlsn.
- O último byte / terceiro grupo / 8 bits,pegar emprestado do host original de 16 bits é possível formar um net-id de 0 a 255, com 256 sub-redes distintas.
- Original: 255.255.0.0 com a máscara 255.255.255.0

Ex: 150.108.0.X até 150.108.255.X - 256 subnets.

- Um and lógico entre o endereço IP e a máscara gera um endereço de rede

Ex: 150.108.2.71 and 255.255.255.0 = 150.108.2.0

Ex²: 150.108.100.98 and 255.255.255.0 = 150.108.100.0

- A máscara contínua, vai acrescentando, estabelecer padrões binários para as máscaras

128 64 32 16 8 4 2 1

1  0 0 0 0 0 0 0 = 128

1 1 1 0 0 0 0 0 = 224

1 1 1 1 1 1 1 1 = 255

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeQzZgyB8f-b9VelojQ5osiD3NYhnDAPoURZ3pEFcn_UmAZ1kh_zWlf0-VdVfu-8JGx_CtqDMtGezxtlHJ4gwc8iEiRUNVtA54a92uWl0nrXd1_9KrK_3hjGOiungOyUJ0bnk-8d9-CXZXcgDREHFlDm30?key=4SgRub88vuVdpJD_jcqH_A)

máscaras de tamanho fixo - flsn

- Quantidade de endereços é sempre 2^16. Sempre subtrai 2 do total de endereços: um quando todos forem zero, pois é endereçado a própria rede, e outro quando todos forem 1 para usar como endereço de broadcast.
- Pega a quantidade de 1’s e eleva a 2 para ter a quantidade de subnets, o resto eu elevo a 2 e subtraio 2, para encontrar a quantidade de hosts.

Classe B - 4 bytes

Classe C - 2 bytes

- Encaminhamento com Sub-redes:

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcTY1PtkObLRxF8vRaOxb8UOybrwjB2AJ_HAEFyhb3GjtL5yKjnyI0DDLrruSlxFD47ZrLDDzlxrWCZBI0RxaegggdkDxkRCDqa50my3R0NO07aXrU3WA7wy-33fH8F6qBGIpYIVu7TCiVv2OFHoNgDqNM?key=4SgRub88vuVdpJD_jcqH_A)

FLSM

→ Na FLSM é projetado para aquela rede que tem a maior demanda.

Rede original: 192.168.0.0

Mascára: 255.255.255.0

→ Criar quatro sub redes, para endereçar os setores de informática, produção industrial e .

- Para isso, nesta máscara, só pode usar o que tiver 0.

255.255.255.0

- precisamos adicionar dois bits para suprir estas quatro sub redes

255.255.255.192

192 = 1100000

Ele precisa de 6 bits em 0, pois o total será 64 hots (64-2 = 62). E 62 é maior que 60, que é a necessidade do setor de informática.

Como analisar o endereço das sub redes?

End. Original: 192.168.0.0

Subredes possíveis:  o 4º grupo corresponde

00000000 - 0

01000000 - 64

10000000 - 128

11000000 - 192

Subrede de Informática:

End Rede 192.168.0.0 / 255.255.255.192

Host: 192.168.1 a 192.168.62  (pois 0 = rede e 63 = broadcast)

| destino | máscara | gateway | interface | R2 para: |
| --- | --- | --- | --- | --- |
| 192.168.0.0 | 255.255.255.128 | 192.168.0.125 | 192.168.0.125 |  |
| 192.168.0.128 | 255.255.255.192 | 192.168.0.190 | 192.168.0.190 |  |
| 0.0.0.0 | 0.0.0.0 | 192.168.0.126 | 192.168.0
.125 |  |
| 192.168.0.192 | 255.255.255.224 | 192.168.0.189 | 192.168.0.190 | comercial |
| 192.168.0.224 | 255.255.255.224 | 192.168.0.189 | 192.168.0.190 | financeiro |

para essas duas (comercial e financeiro) é o mesmo, então pode “juntar”

192.168.0.192  255.255.255.224  192.168.0.189  192.168.0.190  comercial

192.168.0.224  255.255.255.224  192.168.0.189  192.168.0.190    financeiro

192.168.0.192

192.168.0.224

224 - 111(0)00000

192 - 11000000

224 - 11100000

Logo a super rede vai ser  192 - com 26 subredes e não 27

VLSM

EXEMPLO:

- **Informática (120 Hosts)**

255.255.255.0 (00000000)

para atender 120 hosts -> 2^7

255.255.255.128

só 1 bit pra rede

(10000000) -> 2^1 = 2

não daria para atender os 4 setores

só tem 1 bit em um no último byte da máscara

- end rede: 192.168.0.00000000 (0)

ou 10000000 (128)

optando pelo 0

o endereço de subrede seria 192.168.0.0/255.255.255.128

- hosts: 192.168.0.1 a 192.168.0.126
- broadcast: 192.168.0.127

VLSM -> um projeto de máscara para cada setor

- **Produção (50 Hosts)**

255.255.255.0 -> 2^6 = 64 - 2 = 62

1100 0000

=> 255.255.255.192

subredes 2^2 = 4

00 000000 (0)

01 000000 (64)

10 000000 (128)

11 000000 (192)

o 0 e o 64 já foram usados na informática, sobraram os outros dois

do 0 ao 127 já tinha sido usado na informática

- end subrede: 192.168.0.128/255.255.255.192
- hosts: 192.168.0.129 a 192.168.0.190 (129 + 62 = 190)
- broadcast: 192.168.0.191
- **Comercial (25 Hosts)**

2^5 = 32 - 2 = 30 hosts

máscara 255.255.255.224 (11100000)

2^3 = 8 subredes (3 bits em 1)

000 00000 (0)

001 00000 (32)

010 00000 (64)

011 00000 (96)

100 00000 (128)

101 00000 (160)

110 00000 (192)

111 00000 (224)

já foram usados até o 191

sobraram os dois últimos

(192 em diante)

optando pela 192

- end subrede: 192.168.0.192/255.255.255.224
- hosts: 192.168.0.193 a 192.168.0.222
- broadcast: 192.168.0.223
- **Financeiro (15 Hosts)**

2^5 = 32 - 2 = 30

máscara 255.255.255.224

opções de rede iguais ao do comercial, mas sobrou só o 111 00000 (224)

- end subrede: 192.168.0.224/255.255.255.224
- hosts: 192.168.0.225 a 192.168.0.254
- broadcast: 192.168.0.255

VSLM → desperdiça menos endereços

se há sobra de endereços pode usar FLSM

→ **Gateway** - rota de entrega direta

- A própria máquina entrega

rota default → destino 0, máscara 0

route add 158.108.20.0 158.108.33.1

(destino e depois o gateway)

→ Quantos mais bits 1 na rota, mais específica, será a escolhida

→ A rota default é a menos específica

**ICMP redirect:** o roteador vai “aprendendo” as melhores rotas e atualizando a tabela

**CIDR**

→ Bits sempre da esquerda para a direita na máscara

255.255.255.224 -> seria escrito como /27

224 = 1110 0000 (24 bits + 3)

**SUPER REDES**

→ Reduzir tamanho das tabelas de rede

→ Deixar o protocolo ip mais rápida, pois vai consultar menos rotas

EXEMPLO:

200.129.68.0/24

200.129.69.0/24

200.129.70.0/24

200.129.71.0/24

68-> 0100 0100

69-> 0100 0101

70-> 0100 0110

71-> 0100 0111

→ Olhar onde está tendo variação:

- Nos dois bits da direita
- Nesse terceiro byte (destacado), a máscara está toda em 1 (255)
- Colocar zero onde teve variação (24 → 22)

1111 1100

69 passa a ficar igual ao 68

0100 0101 -> 0100 0100

- Os outros também -> 0100 0100

→ as variações não são mais da rede, passam a ser do host

- Endereço da super rede 220.129.68.0/22

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe4op7ty_Hfy_LOCcBPp_FdhQ2B3Rw7QvKWSIGQr7AZOwDSEostIJ7qA2r_EctQ-LxQFz-IFdPOXIU0A3NjKxrBU25kcKL1WCquNb0UFPzqGo-6av7jMj33LEbqIcqjFYBrDZLWet96B5x-O2lT5nWqx1UX?key=4SgRub88vuVdpJD_jcqH_A)

tabela de rotas de R1

destino | máscara | gateway | interface

192.168.0.0 255.255.255.128 192.168.0.126 192.168.0.126

10.0.4.0 255.255.255.0 10.0.4.245 10.0.4.245

- rotas de entrega direta

0.0.0.0  0.0.0.0  10.0.4.254  10.0.4.245

192.168.0.128 255.255.255.192 192.168.0.125 192.168.0.126

192.168.0.192 255.255.255.224 192.168.0.125 192.168.0.126

192.168.0.224 255.255.255.224 192.168.0.125 192.168.0.126

gateway sempre na mesma rede

interface é o ip de R1

**OBS: Se gateway e interface forem iguais → rota de entrega direta**

usando os endereços, formar super rede:

192.168.0.128/26

192.168.0.192/27

192.168.0.224/27

diferença a partir do último grupo

escrevendo em binário:

máscara - 1110 0000 (224)

128 - 1000 0000

192 - 1100 0000

224 - 1110 0000

nesses valores, houve mudanças nos bits sublinhados

vai zerar eles

192.168.0.128/25

tabela de rotas de R1

destino | máscara | gateway | interface

192.168.0.0 255.255.255.128 192.168.0.126 192.168.0.126

10.0.4.0 255.255.255.0 10.0.4.245 10.0.4.245

rotas de entrega direta

0.0.0.0  0.0.0.0  10.0.4.254  10.0.4.245

192.168.0.128 255.255.255.128 192.168.0.125 192.168.0.126

eliminou as duas últimas rotas

ex: destino 192.168.0.253

o ip de r1 vai consultar sua tabela de rotas

máscara 255.255.255.128

253 -> 1111 1101

128 -> 1000 0000

AND resulta em 1000 0000 -> 128

192.168.0.128

comparando com o destino das tabelas, procura um destino igual

segunda linha da tabela, and com 255.255.255.0

terceira linha, and com tudo 0

(vai testando com as máscaras)

a rota default atende o destino, mas o ip continua pesquisando

and com a próxima máscara (255.255.255.128)

resulta 192.168.0.128 (atendeu)

vai escolher a rota com mais bits 1 na máscara

montar tabela de redes de R2 (sem super redes)

rota de entrega direta nas duas primeiras

uma default pra r1;

depois ver linhas que ficam adequadas para formar uma super rede

e tentar mudar a tabela de rotas usando a super rede

CAMADA DE TRANSPORTE

→ Executa nos sistemas finais

→ Transporte fim a fim

→ É responsável pela segmentação de dados, criando pacotes

→ Controle de fluxo e congestionamento das redes

→ Multiplexação dos serviços de redes

→ Só até a camada IP

→ UDP: protocolo simples, não confiável, mexe com a multiplexação sem a mistura dos dados dessas aplicações → TCP no IP, mais seguro e lento

→ **Controle de erros:** tem um campo no cabeçalho do protocolo chamada de soma de verificação → zera todos, pega os outros campos, soma todos que dá um resultado de 16 bits, pega o resultado negativo onde ele coloca no campo de checksum → no destino ele pega esse valor e soma de novo e a resposta tem  que dar zero, significando que chegou tudo certo

→ Quando chegar errado ao destino ele não faz nada, se chegar certo ele manda uma notificação para a origem informando que está correto por um ACK, só trabalha com retorno positivo

→ 4 timers: retransmissão, keep alive time (verificar se ainda está conectado/enviado pelo tcp), persist time (indica que a porta é zero/ o novo tamanho de janela é descartado em transmissão/ele espera por mim e eu espero por ele - deadlock), acumulativo (junta e manda tudo/pode mandar o ack de carona junto com os dados)

→ RTO: se estourar o tempo e não chegar o arp, o tcp envia de novo

→ Multiplexação de Aplicações: permitir o acesso a diversas redes, como abas de um navegador → todos os dados saem e chegam pela mesma placa de rede (podem haver mais), os dados não se misturam pois existem identificações que são os endereços de transporte, as portas são utilizadas e elas separam para onde cada aplicação vai

→ Demultiplexação: quando chega eu desconecto e separo

→ **Controle de fluxos:** controlar a quantidade de informações entre os hosts / a máquina de origem controla, o de origem só manda a quantidade que o destino pode receber sem pifar / a máxima taxa que pode receber / estação final / feito pela camada de transporte

→ **Controle de congestionamento:** fazer com que a rede não fique congestionada / a máquina de origem controla a quantidade de informações de modo que a rede não pare / fazer com que as estações intermediárias não fique sobrecarregadas e estourem seus pacotes de memória / se sobrecarregar simplesmente não pega mais os dados enviados / feito pela camada de rede no OSI e no TCP/IP na camada de transporte

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfjzwJxhGU9yzvz6xNqqhteaWhTpMvtnUbYTpdZygfBrKG1E2iuDk0Ico2QW1ljgThMuSe3Tuv8NK0b_xXIzidG0PSeyCBEJzMvsBg3ed_7FgsZCxr37o_G4nXCl6cKtUwLSoESY2P2fxw43uDCvQslpfXI?key=4SgRub88vuVdpJD_jcqH_A)

mistura na multiplexação e encaminha os dados de aplicações diferentes por uma mesma interface de rede / separo de acordo com o protocolo / separo de acordo com a porta

PROJETO: definir qual protocolo vamos usar

ASSOCIAÇÃO DE PORTAS:

→ Iana: define o número de portas

→ Reservam faixas de portas conhecidas

→ Porta zero → significa use um porta de cliente que esteja livre

| Portas | Utilização |
| --- | --- |
| 0 | Não usado |
| 1-1023 | Serviços bem conhecidos |
| 1024-49151 | Serviços registrados |
| 49152-65535 | Portas dinâmicas para clientes |

TCP

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdZWu8eJZ3btuhplKMvN_wl7lPvKD_YP-o9YPhsQ4rcBEt2N_Qux5MOHTQR-IeFJJOoulKTmtV8Hyqh3qag849fSm45soDH4zqibVMyHh3EJjsmYWuwmgcODCHTUt2m758lbhySjJNa7RXw7vNIL8TJQ_L5?key=4SgRub88vuVdpJD_jcqH_A)

→ Socket: um par IP/porta, um do lado do servidor outro do cliente e nesse meio um protocolo (tcp/udp);

- Se algum desses 5 variar tem uma comunicação diferente, uma situação diferente de modo que não há a mistura de dados

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfDfF8o1iKkIorw_boYM7P_NfwHU6Tg0rGGV4KkUmjEfae6NvtUdFztPuyIjMokP4wA_3RT0WMRTAXyFI_QO2v6W2zj0RZ_ALBHrK2S6mnH7wkzCE4rPJeNDFuycg3PeLIl0xqmuxJjh5dFbaNUqH1-9-9P?key=4SgRub88vuVdpJD_jcqH_A)

→ Stream: lados da conexão, ex: servidor

- Pode se fechar, de modo a controlar o fluxo de dados
- Pode ser full-duplex ou half-duplex

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXey80XtVC6FzKqTewBro0ucBNDYrdJ8T7opiESRNKnWR0xlxq25_QQSdzvZYvGCoXNoQ5sLwSlVnXgCLqvi_8rfdzGR2Qkl8Shhof3tkQ1QoLWeVmoVgBsNmH035zm8vsodM7wkTAFlWtfNot46lhsH-eXt?key=4SgRub88vuVdpJD_jcqH_A)

→ Múltiplas Conexões:

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfrBhoDXaPIPK4cgwmnp10UYIMTYwg5doZIYMLv0lpyfTzyvAXjMSCM-nN-yCo6SFX5WcFTRP8NNPo3J97DdzhVwGpyGEHNy36IUeJPVxji3HK9HUMeuuTOHIrN4_Z4QRHv7EM7XyHckyOGHgG2CD3IH70?key=4SgRub88vuVdpJD_jcqH_A)

→ Transmissão do Protocolo de Controle:

TCP passa o bloco de dados para o IP: header

TCP + dados da aplicação: segmento

- Isso ocorre para cada conexão

Confiabilidade é conseguida por:

- Detecção e correção de erros (segmentos corrompidos)
- Controle de Fluxo (Evita que o transmissor “sufoque” o receptor através do esgotamento de seus recursos)
- Resequenciamento (IP pode entregar datagramas fora de ordem)
- Remoção de segmentos duplicados (fruto da estratégia de correção de erros do próprio TCP)
- Uso de números de seqüência para identificar

dados

- Reconhecimento Positivo de dados recebidos na seqüência correta
- Retransmissão de segmentos não reconhecidos dentro de um limite (variável) de tempo

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfXeRXsa7CDiLdNyUC2GRE5oboR2P-hRF2WOY6bsoBtOam_OllZL_CCd374rp16daS8Hdsz3HC57uPrqR3fY_SruFLSFmKEaHMYHMUlwgnfBWRCnB9RcSBnC0ZGLQCCsBJDXoQ4Po8OUsYFwUck6bOSBeUD?key=4SgRub88vuVdpJD_jcqH_A)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXepmU1OnyOhh_euI5Dv4pXzsMWFef5fUF7jC0H_he3ADAWJCyy5zeM7zpnqAUFq_R-CfFIF99XWfX2OupQmjHtu7InipDgXmXPCqJbppL8rz1VTQeO0LGbBp7AtgwyheC2lAOWkhjo-L5otrPTOG3Z2nVst?key=4SgRub88vuVdpJD_jcqH_A)

- source, destination port:16,16 – Identifica as portas dos nós envolvidos.
- sequence:32 – Indica o número do primeiro byte de dados nesse segmento.
- acknowledgment:32 – Informa próximo número de sequência que o parceiro espera receber. Só é válido quando o flag ACK está setado.
- data offset:4 – Posição na qual os dados iniciam (em palavras de 32 bits).
- reserved:6 - não usado.
- flag:6 - se tiver valor 1 no bit significa que ele está ligado, cad 1 corresponde a apenas 1 bit

° URG : validade do campo urgent pointer, a partir de tal ponto do pacote

° ACK : validade do campo de acknowledgment, jura de dedinho

° PSH : Passar segmento à aplicação imediatamente, segmento inteiro

° RST : Reset na conexão

° SYN : Estabelecimento da conexão

° FIN : Fechamento de um dos lados da conexão, cortar a conexão, pode ser respondido com o ack (deixa a conexão em aberto em uma das partes)

- Window size:16 – Informa o buffer disponível para recepção de dados (remetente preenche), quantidade de bytes que o meu parceiro pode receber sem interromper a transmissão
- checksum:16 – complemento de 1 da soma de 16 bits do pseudo header, TCP header e dados
- urgent pointer:16 – Posição final do byte do segmento que deve ser processado primeiro
- options – Algumas configurações

° MSS (max segment size) para evitar fragmentação

° WSF (Window Scale Factor) para fazer da Janela um

número de 32 bits.

- palavras = cada linha são 4 bytes
- os números são a quantidades de bits
- número de sequência o inicial é zero mas o valor real é gerado aleatoriamente / são 2, pois o número de sequência do que está enviando e o próximo que será enviado
- as 5 primeiras palavras vão existir em todos os pacotes, a 6º é utilizada para partes especiais do endereço tcp/ip

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfb7CfNpY5Zvm5L9sxllx9yxFJp8IkUSsLTwubZiTSrW-lFjylvlHOtIW8zgfUczJ5G6tebcPxPn460AnzsVmhVzx2rvL4CxQ1dsHNqo-O8CHkumQg26KOkdJx44984szt04kqLdsnl8hHTIIKhLTN0MtKn?key=4SgRub88vuVdpJD_jcqH_A)

TCP - Conexão

→ Servidores fazem passive open (listen - escutam)

→Clientes fazem active open (conectam)

→ Possui 3 fases: 1° Estabelecimento de Conexão, 2° Transferência de Dados, 3° Encerramento de Conexão

Estabelecimento de conexão TCP

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf_iPJlvWGEt89R8S2sb7Yk-yYL7mwEgaJYHmFiVIBi4F9R8u77J33pvKDvV1fJDriWk8SbKP0SlFu-SkXHlvAOsPRbgVlaedq-NDwYkfHQRtOK7bjh09kfJA-1DAiuunDwYL57xucZtI72kmXOb1bAFFA?key=4SgRub88vuVdpJD_jcqH_A)

3-way handshake

Troca do número de sequência / Assegura que ambos os nós estão cientes dos números de sequência.

Fase de transferência

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfhbZpBxBTVa8eQFiHo9WZrcklhl-jF6ILHuH2mPdZRUJzKAwNGec6Ggqu2T2um0qihJVWlJa0GWsVlWk-hzQxCFZEB30CLdactTUV0VtV2P9T-4sOOhFR3ZqKtw3iCgSmt9QMn00R34w7XHsuDkEgpGbna?key=4SgRub88vuVdpJD_jcqH_A)

Exemplo de conexão telnet (echo)

Fechamento de conexão

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdnDgCHHVBe6Vkh9-wJhcnB8pTYKw66CtIyZv3pfFoOLg28wNoJKtIJU3yZ_BSDLF7wgeIiKlcLLXtOtRWfzn2J3L_G04MVSqzWYtnof8gk9bMalTYD1hdM91-E5RqBrTHzmQXxwQmcFz2XpGOKLnKPx_U9?key=4SgRub88vuVdpJD_jcqH_A)

Usa o flag FIN para fechar a conexão

Estados do TCP

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcnRU6Xorr24vq7JUCiFWZIlMp3QtBOKizYynXUu3G_EDf21Iio2YcGEpTnMg0-KFZuoUqRXVJWHtiqCNfJ26vB824uoCUod0ie0L_sIUTe4JcFLUM80ytFXna1JV2GrAU3sieyimypxK8Sr55me_52S-4n?key=4SgRub88vuVdpJD_jcqH_A)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcgSbPo1Z3E_FGKxsrWH17QIrOj0EFTQbJPZN6S7j7HH6NjQzIEslNAGiYemutwaSOzev0EPBJqPJ_qs8MrGSD79HjGCGiJNJUCgVQqqT__FFepaqgUbOKAK2j_mo7ACq47f26SLpOprL_WKNQkfENTJ_As?key=4SgRub88vuVdpJD_jcqH_A)

**TIMERS TCP**

→ Persist timer: quando um dos lados informa um tamanho de janela igual a zero.

→ Windows size: permite que os parceiros informem ao outro qual a quantidade de bytes que ele é capaz de receber, sem receber nenhuma confirmação.

OBS: pacotes de ack puro não são retransmitidos

→ Quando a janela é zero, ele dispara o persist timer, passados os 500ms e não chegou novo tamanho de janela, ele pergunta de novo se continua zero, até o parceiro enviar o tamanho certo, assim, evita o deadlock.

→KEEPALIVE TIMER

- Tenta 10 vezes.
- O tempo entre tentativas é 2 horas por padrão

e o intervalo entre tentativas é 1min15s.

- Se um lado cair e voltar, vai ter que fazer um reset também

→RETARDO DE CONFIRMAÇÕES

- Reconhecimento atrasado.
- Ao invés de receber de imediato, aguarda um tempo, pois pode acontecer de chegar mais segmentos.
- Atraso típico: 200ms e vai no máximo até 500ms, pode mandar um ack cumulativo ou mandar de carona nos dados se a aplicação for enviar uma resposta.

**TIMER DE RETRANSMISSÃO**

- Mais importante do tcp.
- Calculado dinamicamente pelo tcp.
- Continuamente ajustado.
- Varia conforme o tempo de resposta com o parceiro que está comunicando.
- Não pode ser fixo, pois as conexões tcp ocorrem em diversas modalidades.
- Quando há perda de pacotes, o normal é transmitir rapidamente.

**RTT** - tempo de ir até a destino e voltar a confirmação

**RTO** - é calculado de acordo com o desvio

**CWND** - janela de congestionamento

Cálculo do RTO

→ Cada vez que manda pacote para o outro lado, faz uma medida de rtt

ex: amostraRTT1 = 1000

alfa = ⅛ (valor default) (0.125), peso que vai dar para amostra

1 - alfa vai ser o peso que vai dar para a média

calcula  a nova media baseada na que tem multiplicada por (1-alfa) + alfa*amostra

o valor de RTO inicial

RTO1 = 3000ms (valor default)

o primeiro segmento vai e volta e a amostra RTT1 é 1000 por exemplo

como é a primeira amostra, não tem a média anterior

mediaRTT1 = amostraRTT1 = 1000

**DESVIO**

→ É a variação da amostra em relação à média

→ Ao longo do tempo esse desvio vai variando

→ Vai ter uma média de todos os desvios calculados

→ DESVIO PADRÃO

desvioRTT1 = amostraRTT1 / 2 = 1000/2 = 500

→ O desvio vai ser a metade da amostra

→ Como é o primeiro não tem média anterior

beta é igual a ¼

está para a média do desvio assim como alfa está para a média das amostras

desvio até o momento vai ter um peso que é 1-beta, 75%

amostra do desvio = diferença em módulo entre a média e ???

a amostra do desvio vai ter um peso de 25%

beta é o amortizador do desvio

só muda o valor, a forma de calcular é a mesma

beta tem um valor maior, então a amostra do desvio tem um peso maior

RTO = mediaRTT + max(g , k*desvioRTT)

g é a granularidade

k é 4 por padrão

considerar o RTO1 anterior como RTOzero, inicial

RTO1 = 1000 + max(500, 4*500)

RTO1 = 1000 + 2000 = 3000

amostraRTT2 = 500

mediaRTT2 = mediaRTT1*(1-alfa) + amostraRTT2*alfa

mediaRTT2 = 1000(0.875) + 500*0.125 = 875 + 62.5 = 937.5

DesvioRTT2 = desvioRTT1*(1-beta) + |amostraRTT2 - mediaRTT1|*beta

desvioRTT2 = 500*0.75 + 0.25*|500 - 1000|

desvioRTT2 = 500

RTO2 = 937.5 + 2000 = 2937.5

**FAST RETRANSMIT**

**→ ACK Duplicado**

- Indica que pacote fora de sequência foi recebido
- Se a perda for fora da sequência é pior

**→ Fast Retransmit**

- Reenvia o segmento depois de 3 ACKs duplicados
- Não espera timeout

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf4LJJzKJSnLUMODQd2vUlBCaEnO0qgoOB8LP9QAlD4kO2QUl4twQcKvVemtoEboLcnMCNmhfkRiL3nL34lovDDvEWPn_22L3pArD2rhrk1X4KSQrV33gaIL4hAFkRtUy7DxATOQkMrzi3NjjEMI3g5ZpHv?key=4SgRub88vuVdpJD_jcqH_A)

Enquanto não chegar o que ele espera, ele continua pedindo.

O 3 não é obrigatório mas convencionou-se a utilização, porém, a partir de 1 já pode

**FAST RECOVERY**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdXXpAzhGLxhjWnCkASNJH7tIOHZK3xvKMFl0xM_Tlz4necrTqla36fR9E0rxruvhvcQng47VaCajLDDO3qeo5aqlj6mSzS0RAvwFnU9EO9W8D68461hbhWBEEjqilSdOZEJVG-zrIptRAc9VQsaEeiDtI?key=4SgRub88vuVdpJD_jcqH_A)

→ O melhor é o SACK, ele informa para origem exatamente quais pacotes foram perdidos, pode mandar até 4 faixas. Corrige na faixa de milissegundos.

CONTROLE DE FLUXO

→ TCP só manda reconhecimento positivo

→ Se chegar correto, ele manda ack

→ Se não chegar ou chegar com erro, ele não manda nada

→ Há protocolos que fazem reconhecimento negativo (no ack)

→ Campo Window size, 16 bits

→ Window scale factor -> amplia o tamanho da janela

**Janela unitária**

→ Window size = 1 (em bytes)   /   1 byte

→ Só recebe um byte por vez

→ Quando o destinatário receber 1, ele manda o ack 2

→ O remetente vai então mandar o 2, e o destinatário vai mandar o ack 3

**OBS: (sempre envia o ack do próximo que ele quer receber)**

→ half duplex - apenas 1 direção   /   ora um transmite, ora o outro

→ O tamanho da janela é informado pelo receptor, não pela origem (controle de fluxo)

→ A origem vai dizer a janela para controlar o congestionamento e não o fluxo

→ Window size = 3

→ 3 bytes, cada byte em 1 segmento

→ Pode mandar 3 antes de precisar mandar o ack

→ Ack cumulativo, o ack 4 vai validar o 1, 2 e 3

RETRANSMISSÃO DE SEGMENTOS PERDIDOS:

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf32zsAGaSwMdqLNCjxRgrQV0xAWUfnM0f92t06jRd28ggodcYTO1-pX6DyOLrwxTGAOWAyCbkLQXQF5tdJq6nf1gUD5We7N6jw70AvI4SwpcrrWouYnYiAWHu4FBMA6cxxYmpREPrI9WCObC6-l8afP2o7?key=4SgRub88vuVdpJD_jcqH_A)

→ Se não chegar do 600-699

→ Do 700-799 fica no buffer em nível de transporte

→ Ele só manda o ack 600

→ O receptor vai mandar do 600-699 de novo

–. Quando ele receber até o 699, aí sai do buffer o outro e ele manda o ack 800, indicando que recebeu tudo

SndUna - enviado e não reconhecido

SndNxt - próximo segmento a ser enviado

→ Entre SndUna e SndNxt - bytes que não foram acked, mas já foram enviados

SndWnd - definido pelo receptor

→ A janela vai deslizando

→ Pode ou não mudar de tamanho

→ O ack diz pra onde o SndUna deve avançar

→ Esse controle é **feito na origem**, respeitando a janela oferecida pelo receptor

**RTO** - tempo que espera antes de retransmitir

retransmission time out

**Algoritmo de Karn** - se ocorrer um time out, dobra o rto. Perde as estatísticas dos rtts

**Timestamp** - usado para tirar ambiguidade da retransmissão

- É a hora atual da máquina que vai fazer retransmissão
- Além do número de sequência, manda o número de segundo da máquina que vai transmitir
- Se rto for 2 s, vai retransmitir no segundo inicial+2s

**OBS: É desnecessário usar algoritmo de Karn se já estiver usando o timestamp**

→ A desvantagem é o número de bytes que vai gastar

→ 4 bytes da retransmissão e 4 do reconhecimento (timestamp que ele recebeu do parceiro), 2 de outra coisa (do tamanho). Como tem que ser múltiplo de 4, fica 12, 12 bytes no cabeçalho pra mandar o timestamp

CONTROLE DE CONGESTIONAMENTO

→ Quando a fila está cheia, os descartes começam a acontecer

IMPLEMENTAÇÕES TCP

→ Esses são implementados no kernel, a maioria usa o cubic ‘o melhor que tem em termos de estabilidade’.

→ TCP TAHOE:

- Implementado no projeto bbs unix 4.2
- Associação dos algoritmos slow-start
- Utiliza a associação dos algoritmos Slow-Start, Congestion Avoidance e Fast Retransmit
- A utilização do algoritmo Fast Retransmit pelo TCP Tahoe é feita baseada em dups ACK sem aguardar que o RTO expire.
- Emissor infere antecipadamente que um pacote foi perdido aumentando a utilização e o throughput da conexão
- Não implementa Fast Recovery

→ TCP RENO:

- Implementado no BSD Unix 4.3
- Modifica o algoritmo foi implementado
- Implementado no projeto BSD Unix 4.3
- Modifica o algoritmo Fast Retransmit e inclui o algoritmo Fast Recovery, prevenindo que o canal de transmissão fique vazio após a fase Fast Retransmit e não acionando o Slow Start quando um único pacote for perdido
- O Fast Recovery é acionado pelo TCP do emissor após receber um limiar inicial de normalmente 3 dup ACKs.
- Toda vez que recebe 3 dup acks, o emissor retransmite um pacote e reduz sua cwnd pela metade da janela permitida atual.
- Após entrar em Fast Recovery o emissor retransmite o pacote indicado pelos dup ACKS e aguarda um ACK do mesmo, enviando um novo pacote para cada dup ACK adicional que for recebido.
- Após receber um ACK de um novo dado ("Recovery ACK"), o emissor sai do Fast Recovery.
- Caso aconteça um RTO, entra no slow start

→ TCP NEWRENO:

- Pequenas alterações no reno para evitar problemas de desempenho, consegue se recuperar mais rapidamente
- Realiza pequenas alterações no Reno para evitar problemas de desempenho.
- Baseia-se em ACKs parciais, que referem-se a confirmação da chegada de apenas alguns pacotes enviados
- Quando ACKs parciais são recebidos durante o Fast Recovery, considera-se como indicação de que o pacote seguinte ao confirmado (ACK) foi perdido e deve ser retransmitido.

→ TCP SACK:

- Pode ser usado com o reno ou com o newreno, ele diz quais exatamente foram perdidos, são chamados de selective ACKs
- Extensão do TCP Reno, usando os mesmos algoritmos para o controle da janela de congestionamento.
- A diferença principal entre eles é o comportamento quando múltiplos pacotes são descartados.
- O SACK usa o campo "opções" do cabeçalho TCP para enviar um Selective ACK.
- Emissor pode evitar atrasos e retransmissões desnecessários, melhorando a vazão

→ TCP VEGAS:

- O TCP Reno é reativo e precisa da existência de perdas para encontrar a banda disponível, enquanto o TCP Vegas é proativo
- Percebe o congestionamento com base nas alterações da taxa de vazão
- Retransmissão é baseada no refinamento das medições do RTT
- Ajuste da cwnd é baseado nas medições e reduz a taxa de transmissão antes de haver perdas

→ TCP CUBIC:

- Modifica o crescimento linear de cwnd para ser uma função cúbica a fim de melhorar a escalabilidade do TCP em redes rápidas e de longa distância
- O crescimento da janela independe do RTT, possibilitando atingir alocações de largura de banda mais equitativas entre fluxos com diferentes RTTs. Usa o relógio interno da própria máquina.
- Cubic é o algoritmo TCP padrão para o Linux,

sendo disponibilizado desde o kernel 2.6.19

→ TCP BBR:

- Vê qual o máximo de taxa que ele pode usar, e de acordo com o tempo resposta ele faz um modelo de rede
- Em uma situação de erros ele e o cubic são iguais
- O Google criou o BBR (Bottleneck Bandwidth and Round-trip propagation time) em 2016
- Usa a largura de banda máxima e o RTT mais recentes para construir um modelo da rede
- Avaliações no YouTube mostraram uma vazão média da rede 4% maior
- Considerado injusto e pouco escalável ao ser usado junto com outras implementações TCP
- Está disponível no Linux desde a versão 4.9 do kernel, sendo também usado pelo QUIC
- É considerado injusto, porque se os hosts não estiverem usando o BBR podem ser afetados, pois ele concentra tudo o que tem disponível de capacidade de transmissão de rede
- **O BBR sabe lidar melhor com a perda de dados**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfBd-CxKKfe7TSNlMoS66kNcHOj3ikejdYKAX-tQ8v1_njmqW1eU4IB8Rx2tIwPTJMDXb6S5f8ZRwGyqHapyMzVNlnedt6eaexjhx9QXTIZbTGJr9dBsw-ts1LsxbvqM82hvKvcyxzg90QnoAERYbjjlvMS?key=4SgRub88vuVdpJD_jcqH_A)

**API DE SOCKETS**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeeOl5W6S8cKZQlmwizrP9Tsu7g4R3bXLHaaQVdss0Tje2RXY6yiGDQzzqn17eieQwc9GqV_fenBldte9OJV_YLl0nbmn6JDssSSUJqyQhmoMLvvJjd1WGVyiVnoOuvAiR5LV5Qtfk7H1k9wkASse4S6jc?key=4SgRub88vuVdpJD_jcqH_A)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfCw80slVi7HSZZZul5WH6KArBHa2t801I1IVFISsaZE9-O1tGrOPaYdweKWiCQLzl08wqo4bpd8RJ9LmiLMWTrlb4KnE58P7AImH_QuDDHoR6qPtlJNzPIgEGZUjaW66cIPFQrXAeicMYKLK_DBA14CVgR?key=4SgRub88vuVdpJD_jcqH_A)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcORYcmdBFH8zY_o8CzjKp3BtNzC2R4IGTVcWjMOH1xTqdCaWx_l1Q9G18d7jALU59ASRK9wUsjIyN_7-jLifVelwfJL0ATMxDXjFWGFwExpMLe-bjVJ5UoGqOfd8kYFEIpgEA003ten8FswxPc5P_H9WZU?key=4SgRub88vuVdpJD_jcqH_A)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcKUGTkAQpScI62TzShAqilJ8wfdCjIDqkgDAkVSpancA2o_x7OxOBE1M39_LLTIkpWLMprK2oxWpLkKqGLdvCE8CkqP49mrRp1ehjOx8JqRt8dc3cq2X3bMHhgJL0jPCEFVGZFU4nYvpAlYX5Q9iVHWXw1?key=4SgRub88vuVdpJD_jcqH_A)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcNzQiOEPTCHZfePuZq4Q6ltsz02djGj2mVNuzlS1n0rIcZ2e05Hfr4ziTo2-Cs_tsJBS2BxVAvzmhR3Xa3r5eb6Ou76EpwGhlA9XG1IadVgRWaJjlPqypQ_jdYzuLK5oRyNzlkxQeMx9u1nUNDHeXB9wE?key=4SgRub88vuVdpJD_jcqH_A)

**HTTP**

→ Cliente como navegador web, servidores web

→ Serve de base para troca

→ Em http pode-se trabalhar com tipos de mídias diferentes

→ utiliza o protocolo TCP, porta 80

1.0 conexões não persistentes

1.1 conexões persistentes / devolve em formato chunked que é em pedaços e mostra o tamanho em bytes de cada parte

2.0 compreensão de cabeçalhos, uma série de recursos para melhorar o http 1.0

→ Não tem estado, pois o servidor não mantém info dos clientes entre as requisições, pois assim seria mais simples de ser implementado

→ A performance varia, já que se trabalhou com o slow start do tcp

***Não persistente:***

1. cliente inicia conexão
2. cliente http envia requisição ao servidor buscando o objeto
3. Servidor recebe a solicitação, acessa o objeto solicitado, monta mensagem de resposta contendo o objeto
4. Servidor fecha imediatamente
5. cliente recebe resposta e fecha seu lado

obs: se precisar de mais objetos ele faz os mesmos passos anteriores, sempre estou abrindo novas conexões já que ela não é persistente, sempre em slow start, diminui a otimização

Pode se ter conexões em paralelo, todas começam com taxa de transferência baixa

Se pedir 4 arquivos, vão ser 5 conexões, uma para cada arquivo e uma para a página solicitante

***Persistente:***

1. Cliente http inicia conexão
2. cliente envia requisição
3. servidor recebe e acessa o objeto
4. servidor mantém sua conexão aberta
5. cliente recebe a resposta, trata o conteúdo do objeto, e observa que tem mais objetos
6. na mesma conexão ele envia os outros objetos
7. evita o slow start do tcp
8. podem ter paralelos, não necessariamente é otimizado

se botar só barra no GET, ele pega a página default

\r\n = terminadores de linha que indicam que terminou, é uma linha em branco

***Métodos:***

No head é só o cabeçalho, o objeto não é devolvido

options: o que você suporta? Helo (quais os métodos suportados)

o put é mais usado em apis, alteração no servidor adicionando um novo objeto

trace: depuração, se algo não tá funcionando direito eu posso usar para verificar

Em cada linha tem um rn

No http 1.1 é obrigatório o host, no 1.0 é opcional

no accept */* aceita qualquer tipo na resposta

Servidores virtuais na mesma máquina,  esse campo serve para fazer um distinção em quais sites estão sendo usados

O authorization é frágil e pode ser facilmente quebrado

Se modificado em tal data, traga o objeto se não o cliente usa o que está no cache

Pode ser solicitado uma versão específica

Solicita o login e a senha do usuário

Content-Length é o tamanho em bytes da resposta

Connection se tiver o keep alive mesmo que seja o 1.0 se for suportado pelo servidor ele vai trabalhar com persistente

Content-Encoding o objeto sendo enviado no corpo da entidade está nesse formato, é mais provável na resposta mas também pode ocorrer na requisição

echo -e “METODO /ananda.html HTTP/1.0\r\n\r\n” | nc 192.168.1.6 80

se colocar o host ele dá uma linha a mais com Host: blablabla

Action = ação a ser executada

O post os parâmetros passados através do corpo da entidade, é interessante quando quero passar algo como senhas, pois a informação passa protegida, na autenticação de um sistema por exemplo, ou muitos parâmetros. A query vem vazia. O post não armazena histórico.

O uso do get pode ser interessante para pegar direto da url, repetir requisições

***Autenticação***

cliente envia

Basic = login e senhas do usuário, isso significa que eles vão trafegar pela rede, o que não é seguro, é apenas codificação não criptografia

o response é sempre o mesmo

Digest = desafio, função de hash que faz a criptografia, envia-se uma uma informação da senha, o servidor possui essa info, se for certo o que o cliente enviou ele libera o acesso

1. Navegador pede login e senha

response muda a cada requisição se as informações variarem

cnonce para cada um, não é possível reaproveitar, vou incrementando o valor da contagem para que o servidor saiba quantas vezes foi feito

nonce = sequência gerada aleatoriamente pelo servidor

qop = operação devolvida pelo servidor explicitando o mecanismo utilizado

***Cookies:***

set-cookie é do servidor e cookie é do cliente

ambos no campo de cabeçalho

primeira vez que acesso não tenho cookie então o campo de cabeçalho devolve um set-cookie

Proxy: informações grandes e um acesso a internet de baixa qualidade

***Web Cache:***

→ Otimizar a performance do http, minimizando o número de requisições dos clientes, reduzindo a quantidade de respostas completas enviadas pelos servidores

Se eu tenho uma info já armazenada localmente ou um proxy web e ela não foi alterada pelo servidor eu envio ela pela rede

Expiração: se já acabou

Validação: se ele foi alterado

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcnPqTqmOI0IPon31sSOvdYzEVFmAWVUElNr8KEbSNPwMQwD5P2hZN59zbvs4MlfkPGdoy-XAwT9u92RHCQcRs5loHob1RrLqZXhs3qD84IFjET_lDBqmjr8t2MbH2YH6JLERuE2DXc_A3QA701o6Lv9jhB?key=4SgRub88vuVdpJD_jcqH_A)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXem_Veocg-5BOImiMPmN_5JnYTGOs7nJKXxkLzL7bOQ1g_w7_h_Dpb5D1XGxOiX3iK5-JIEHlzd9CqCvkK81zTz-taqO4WHLJ-rMQaEfUhf1EbrJ93DGuiipA7SXF6q3AYm8gESS_xXOyqzTRG2X4aXj20?key=4SgRub88vuVdpJD_jcqH_A)

**SMTP**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeByNIQT4y9aFKkqJW-hMzTnlTEOYI3QZW0aNANCCPf_ys6cb7P6eOMCHRwtafVETcQCit4V7jAR4yN53wRFWygzTxqChKNJ-DVcsbggb_uQyALYgHahwINNYXi4tZsZ-wtELzObYDa4p0qiVaBnTqMEIQ_?key=4SgRub88vuVdpJD_jcqH_A)

SMTP - envia emails

POP3 e IMAP4 - recebem emails

MTA envia

MAA recebe

pop3 - usado por conta da simplicidade

iMAP4 - cria pastas de emails, ex: emails lidos

**OBS: o smtp é menos rígido que o http em questão de case sensitive**

cada recept tool só recebe um endereço

ELEMENTOS COMPONENTES DO CENÁRIO

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdPNxXAsU-CLjSPp_48R59RXdOSl0MjKeKtJlH9uNmsZKYRlSN2o_RYzI0zpsV7kxf4KHVnbekOaoYfwOA0PV86ZlIV-PfcGVkuBi3GU4ptDuVrwAOeMRlQd_3CByYLjw-m6u41pNT2wO3BwhAEnWz5-8ER?key=4SgRub88vuVdpJD_jcqH_A)

EXEMPLO SIMPLES SMTP:

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdP5N04itbpmGcUBL6lr7iilZQr_8CkRRP3cQyLHWLWQq-I9Z0eXgJo8vUGlu7gs-Ar3Djxi_Dzy3znKVYR_6dscNw4dyD2qEvlreCLTnXqkQut6QnA4J1fTxlNCim1rcB6iknMhEAPwsHH2ywM2hMbnV0?key=4SgRub88vuVdpJD_jcqH_A)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcwxLqlRDfxKGmmYZ3yWslO1qJrWKeHko83ahDpU3jiaPTX_pLTFP4jqW1Ml9eEUF9SMxVpLsnU9UQl10R9uqOEZKFJO_Bgwdz0ufOCgnbwhHGJztI3XTksEKpFZBeqGb21j3xQgNNRXjFpA9WFhVwXDRaJ?key=4SgRub88vuVdpJD_jcqH_A)

→ Sempre utilizar a autenticação com a versão segura, pois se não o acesso a senhas e dados se torna fácil

EHLO ou HELO

– Usados para identificar o cliente SMTP junto ao servidor SMTP

– Servidores mais novos suportam EHLO e os antigos HELO

Ex: EHLO tabajara

MAIL FROM:

– Inicia uma transação de

email

Ex: MAIL FROM: [leoflj@ig.com.br](mailto:leoflj@ig.com.br)

RCPT TO

– Identifica o receptor do email  Cada receptor é indicado por um comando.

– Se houver múltiplos receptores usa-se um comando para cada

receptor

Ex: RCPT TO: [leoflj@ig.com.br](mailto:leoflj@ig.com.br)

DATA

– Estabelece os dados a serem enviados na

mensagem

– Informações de cabeçalhos como To:, From: e

Subject: são enviados no início dos dados, separados do corpo do email por uma linha em branco.

– O final dos dados é especificado por uma linha contendo .

Ex: DATA

QUIT

– Solicita ao servidor que encerre a

conexão

– O servidor não deve encerrar a conexão até que receba a mensagem QUIT e envie uma resposta para a mesma

– O cliente não deve encerrar a conexão antes de

mandar uma mensagem QUIT e obter a resposta

da mesma

Ex: QUIT

Suponha que você tenha um servidor de e-mail e deseja que os e-mails sejam transmitidos de forma mais segura. Você pode configurar o servidor de e-mail para usar o protocolo SMTP seguro (SMTPS) ou o STARTTLS para criptografar a comunicação.

**MIME**

Content-Disposition: outro tipo

→ O que significa MIME? Multipurpose Internet Mail Extensions (Extensão multiuso do correio da Internet)

→Permite o envio de arquivos anexos e o uso de emails com formatação

→ Definida nos RFCs 2045 e 2046

**Principais cabeçalhos**

Content-Type: Indica o tipo da mídia anexada

Content-Transfer-Enconding: Indica o mecanismo utilizado para converter dados binários em ASCII

**Exemplo de uso da MIME**

Conteúdo do corpo do email

From: =?iso-8859-1?Q?Le=F4nidas_Lima_J=FAnior?=

<leoflj@ig.com.br>

To: leoflj@ig.com.br

Subject: Teste de anexo

Date: Wed, 26 Mar 2014 21:20:31 -0300

Message-ID:

<NHBBJHCLKLJHEFLNJHAJCEIDCBAA.leoflj@ig.com.br>

MIME-Version: 1.0

Content-Type: multipart/mixed;

boundary="----=_NextPart_000_0000_01C41597.41A9AB60"

X-Priority: 3 (Normal)

X-Mailer: Microsoft Outlook IMO, Build 9.0.2416

(9.0.2910.0)

Importance: Normal

X-MimeOLE: Produced By Microsoft MimeOLE

V6.00.2800.1165

This is a multi-part message in MIME format.

- -----=_NextPart_000_0000_01C41597.41A9AB60

Content-Type: text/plain;charset="iso-8859-1"

Content-Transfer-Encoding: 7bit

Corpo do email

- -----=_NextPart_000_0000_01C41597.41A9AB60

Content-Type: image/jpeg;name="Inverno.jpg"

Content-Transfer-Encoding: base64

Content-Disposition:

attachment;filename="Inverno.jpg"

/9j/4AAQSkZJRgABAgEAYABgAAD/7RBKUGhvdG9zaG9wIDMuMAA

4QklNA+0KUmVzb2x1dGlvbgAA

AAAQAGAAAAABAAEAYAAAAAEAAThCSU0EDRhGWCBHbG9iYWwgTGl

naHRpbmcgQW5nbGUAAAAABAAA

AHg4QklNBBkSRlggR2xvYmFsIEFsdGl0dWRlAAAAAAQAAAAeOEJ

JTQPzC1ByaW50IEZsYWdzAAAA

... Demais dados binários codificados em base64

- -----=_NextPart_000_0000_01C41597.41A9AB60–

**POP3:**

+ok < descrição do servidor>

PASS espertinho - passa a senha certinho

STAT

+OK 0 0 - quantidade de mensagens e quantidade de bytes usados por ela

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeG74s47enOKTAbv3PtlLBJx0FYXAzrrO-uN8AhkGERqpJXQpytgvq8WidU-yZ8P6uSUDC3tgkROe-b9w8T9sqf5_RuyKjmXTGwSDXVdGSQDZD1bC87b9rpWMLTXhNB7p0klDDlv651PYwqj_m9Y-KUWSfj?key=4SgRub88vuVdpJD_jcqH_A)

MAIS DETALHADO

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXekJJp_KBefoW93H85lDx_S4pUhiKOwIMPDZhAr3pUZx65eunIzkzSoyGljcSVWlSbBcph-T1o1Ja82DHsYhfgSu7_Tfe-npq-QoNVbHnUjLrjm2DSO3QbnzEMZMxTCUxoye0uGL4VKswYKMp8hx8h_mrnn?key=4SgRub88vuVdpJD_jcqH_A)

USER

– Identifica o usuário junto ao servidor  Ex: USER leonidas

PASS

– Envia a senha do usuário, completando a autenticação

Ex: PASS espertinho

STAT

– Devolve uma informação de status da lista de mensagens. O formato da resposta é +OK msgs tamanho

Ex: STAT

+OK 2 10200

LIST

– Devolve lista das mensagens presentes no servidor. Se informado um argumento, este será tratado como o número da mensagem a ser lista

Exs: LIST LIST 1

+OK +OK 1 1804

1 1804

2 18364

DELE

– Marca uma mensagem para ser excluída do servidor

Ex: DELE 2

+OK

RSET

– Desmarca as mensagens marcadas anteriormente como deletadas

Exs: RSET

+OK

QUIT

– Solicita o encerramento da conexão com o servidor, habilitando o mesmo para eliminação das mensagens marcadas

Ex: QUIT

+OK

TOP

– Mostra as linhas iniciais do topo de uma mensagem. Os argumentos são a mensagem e o número de linhas do corpo da mensagem

Exs: TOP 1 3

UIDL

– Devolve lista dos emails não deletados presentes no servidor. É devolvido um ID único para cada mensagem, permitindo a identificação das mensagens em diferentes sessões. Se informado um argumento, este será tratado como o número da mensagem a ser listada

Ex: UIDL

+OK

1 M795717P2624V.mailserver-56,S=1804

2 M900456P24245V.mailserver-56,S=18364

3 M837883P27835V.mailserver-56,S=78598

RETR 1

ver o conteúdo, o número é de acordo com as mensagens

**DNS:**

→ Identificação de hosts

→ Endereços IP e nomes de host

→ utilizado para relacionar nomes a endereços

→ Base de dados distribuídas

→ Protocolo da camada de aplicação

→ Função interna da internet

→ Não é relacionado a uma aplicação em particular (todas fazem uso do mesmo tipo de serviço, get host by name e get host by addr)

Por que não centralizar? ponto único de falha, volume de tráfego, problemas de manutenção e base de dados distantes. Não cresce junto com a rede

nenhum servidor dns contém todos os mapeamentos de nomes, se tem os locais, os hosts da rede locais vão primeiro para o servidor de dns

servidor de nome local: verifica se tem armazenado

servidor de nome raiz: servidor de nome local, se não ele vai para o de nome autoritativo, se ele encontrar devolve para o local e deixa armazenado

servidor de nomes autoritativo: quando perguntar quem é fulano, ele responde, ele pode fazer um mapeamento de nome para aquele endereço

tem 13 tipos de a até m

1. host contacta o dns local, 200.129.77.52
2. o 200.129.77.52 contacta o servidor de nome raiz se necessário
3. e se necessário o servidor de nome raiz contacta o nome autoritativo

a cada passo a informação é adicionada ao cache para que caso seja feita a solicitação novamente o servidor já terá essa informação

1. servidores intermediários: aqueles que devem ser conectados para se encontrar os autoritativos

**consulta recursiva** = o servidor que tá fazendo assume a tarefa de resolução, pode ficar pesada

sempre entre o local e a máquina

**consulta encadeada** = o contactado responde com outro nome de servidor (esse que irá resolver), eu não sei, fala com fulano

as informações armazenadas num registro do tipo cache após um tempo se tornam obsoletas

mecanismos de notificação para que essas zonas fiquem atualizadas RFC 1996(notify) e RFC 2136(update)

dns é uma base de dados distribuída que armazena registros de recursos, uma tupla com 5 elementos(name, ttl, class, type, value)

*Tipos de registros DNS*

tipo **A** / 1 - name é nome do computador e value é endereço ip (Address IPv4), quando um cliente usa esse tipo de registro, o objetivo é descobrir o endereço IPv4 que responde por determinado nome de domínio;

tipo **NS** / 2 -  name é domínio e value é endereço ip do autoritativo para este domínio (Nameserver), especifica o nome do servidor DNS responsável por determinado domínio;

tipo **CNAME** / 5 - name é um apelido e value é nome canônico, (Canonical Name), faz o mapeamento de um alias (apelido) ou um DNS alternativo

tipo **MX**  / 15 - value é o nome do servidor de correio(mail) associado com name, (Mail Exchange), fornece o nome do servidor de e-mail de maior prioridade que responde por determinado domínio de e-mail.

AAAA – Address IPv6 - Quando um cliente usa esse tipo de registro, o objetivo é descobrir o endereço IPv6 que responde por determinado nome de domínio;

PTR – Pointer – Realiza o caminho inverso. A partir de um endereço IPv4, deseja-se obter o respectivo nome de domínio

SRV – Service – Permite definir serviços disponíveis em um domínio;

SOA (Start Authority) - registros dos servidores autoritativos, retorna o primeiro registro para determinado nome em uma zona DNS e seu responsável

Identificação: número de 16 bits para consulta, resposta usa mesmo número

Flags: consulta ou resposta, recursão desejada, recursão disponível, resposta autoritativa

**Porta 53**

UDP - até 512 bytes - longas ficam truncadas e chama-se o tcp

TCP - maior que 512 bytes - transmissão entre zonas

**snmp: monitorar e gerenciar dispositivos de rede.**

**DHCP:**

→ Dynamic Host Configuration Protocol

→ Definido nas RFCs 2131 e 2132

→ Criado com o objetivo de aprimorar o funcionamento dos protocolos RARP e BOOTP

→ Utiliza UDP como protocolo de transporte

Cliente → Servidor: porta 67

Servidor → Cliente: porta 68

→ Envia IP, Servidor DNS e Tempo

Em redes internas, é comum que a atribuição de endereços IP seja feita por meio do protocolo DHCP, utilizando um servidor configurado com esse serviço. Uma das características positivas de ter um servidor DHCP configurado na rede é evitar o acontecimento de IP duplicado na rede.

**Tipos de atribuição de endereços:**

*Automática:* servidor DHCP atribui um endereço IP permanente ao host

*Manual:* O endereço IP do host é estabelecido pelo administrador da rede, o servidor DHCP apenas transmite este para o cliente

*Dinâmica:* servidor atribui um endereço IP ao host por um intervalo de tempo limitado, chamado lease period

**Descrição da mensagem DHCP**

**op:** Tipo da mensagem

1 = BOOTREQUEST, 2 = BOOTREPLY

**htype:** Tipo do endereço do hardware

1 = Ethernet, 6 = Redes IEEE 802, ...

**hlen:** Tamanho do endereço de hardware, 6 bytes para Ethernet

**hops:** Usado por relay agents

**xid:** Identificação da transação, número aleatório gerado pelo cliente

**secs:** Tempo em segundos desde o momento que o cliente adquiriu ou renovou o endereço

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc-ToAu3qdpuWuhEOhNWobD2ubKCXtPN4UeTau8ZcY0hgLBnc_J_E93IWD6OUomlCgI3pEwoMSO-Csr84BZCZn1CB7-lrBkuYbqQo_N3zJTYYswz6DS42-Pzh9OytjhdXoBZVXoHvW80iZfqdxNln3u-eo?key=4SgRub88vuVdpJD_jcqH_A)

OBS: Se o B estiver ligado ele recebe em broadcast ou seja sempre em 1

**ciaddr:** Endereço IP informado pelo cliente

**yiaddr:** Endereço IP definido para ser usado pelo cliente

**siaddr:** Endereço IP do servidor DHCP

**giaddr:** Endereço IP do relay agent, caso esteja em uso

**chaddr:** Endereço de hardware do cliente

**sname:** Nome de host do servidor DHCP (opcional)

**file:** Nome e diretório do arquivo de boot remoto, caso seja usado, boot loader

**options:** Opções DHCP a serem negociadas entre cliente e servidor, conforme descrito nos slides seguintes

**Formato Da Mensagem**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdsWQCd4bu2u65aN9SpfiUdQv-QdrOZ1oRlwuZjDLxpGun9lJiig2aOUpUhtlV2-YknZ4ecKD_Amdc2dUayQa-kpc526nHdaIOXALTNvm1nMOlIYXXR5uFP3rx5-VNxGP2DbpjS8pfBio7G-RfKpi7FNdOK?key=4SgRub88vuVdpJD_jcqH_A)

**Número de roteadores + 2**

Nem sempre o servidor vai atender a requisição do cliente

**Opções DHCP:**

Subnet Mask: 1

A opção máscara de subrede específica é a máscara de subrede a ser usada pelo cliente.  O código para esta opção é 1, e seu tamanho é de 4 bytes. Code Len Subnet Mask

+-----+-----+-----+-----+-----+-----+

| 1 | 4 | m1 | m2 | m3 | m4 |

+-----+-----+-----+-----+-----+-----+

Se as opções de máscara de subrede e roteador são especificadas em um DHCP reply, a máscara de subrede deve vir primeiro.

Router: 3

A opção router especifica uma lista de endereços

IP de roteadores na subrede do cliente.  Roteadores devem ser listados em ordem de preferência.  O código para esta opção é 3, e seu tamanho possui um mínimo de 4 bytes e deve ser múltiplo de 4. Code Len Endereço 1 Endereço 2

+-----+-----+-----+-----+-----+-----+-----+-----+-- | 3 | n | a1 | a2 | a3 | a4 | a1 | a2 | ... +-----+-----+-----+-----+-----+-----+-----+-----+--

Domain Name Server: 6

A opção Name Server especifica uma lista de endereços IP de servidores DNS disponíveis para o cliente.  O código para esta opção é 6, e seu tamanho possui um mínimo de 4 bytes e deve ser múltiplo de 4. Code Len Endereço 1 Endereço 2

+-----+-----+-----+-----+-----+-----+-----+-----+-- | 6 | n | a1 | a2 | a3 | a4 | a1 | a2 | ... +-----+-----+-----+-----+-----+-----+-----+-----+--

Há um conjunto de opções específicas do DHCP, denominadas extensões DHCP

Request IP Address: 50

Usada em uma mensagem DHCPDISCOVER para o cliente indicar um endereço IP específico que deseja utilizar.  O código para esta opção é 50, e seu tamanho é 4. Code Len Endereço IP

+-----+-----+-----+-----+-----+-----+

| 50 | 4 | a1 | a2 | a3 | a4 |

+-----+-----+-----+-----+-----+-----+

DHCP Message Type: 53

Esta opção é usada para definir o tipo da mensagem DHCP.  O código para esta opção é 53, e seu tamanho é 1. Code Len Type

+-----+-----+-----+

| 53 | 1 | 1-9 |

+-----+-----+-----+

**OBS:** 53 é a mais importante, pois ele permite que especifique qual a operação do dhcp que será utilizada, qual a mensagem que está sendo enviada

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdO6WQovVeQ3Q_kFxzn0D4a3whI9YoBex301ZPYhN8_lxGOb4JiiD_9fXShpj8cMCgAdRd-hJiRAODLg1objwXrQkhk98FnALXvwV1eaF9lvNwqjM5Ts4QhEY8evqfgoSmjXTKI-tvrTlOTe-9D0eUsMjTM?key=4SgRub88vuVdpJD_jcqH_A)

1. Sempre Enviada Em Broadcast, quem responde é o hcp, e se houverem dois o default é ela responder o que chegar primeiro. Broadcast do cliente para localizar
2. O servidor que recebeu o “1”, responder, dá um ACK na rede para ver se a máquina está correta
3. Cliente para servidores com o objetivo de (a) requisitar formalmente parâmetros ofertados por um servidor e implicitamente descartar aqueles oferecidos por todos os outros servidores, (b) confirmar endereços previamente alocados, como no caso de um reboot do sistema, ou (c) estender o aluguel de um endereço IP.
4. A máquina rejeita, ex: pegou uma máquina com IP fixo, esse está na faixa de endereços do hcp, quando ocorrer o processos dois ambientes estaria com mesmo endereço IP
5. Indicando que funcionou
6. indicando que está errado e solicitando outro
7. Cliente para servidor liberando um endereço IP e cancelando qualquer aluguel associado a este.
8. Informar periodicamente ao servidor de que a máquina está ativa, notificando um ao outro

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdf4ItvEO8bObAlKz-5HzG2TuDAbTdgk5TuoFsD20bklN4kbWyVqpQJ9JG7thYPiuvWieS6JNlFcW38tFKiHy5Cgz1UyhstmypSpEYOH_OWhNQ07R1799CTV85IVSAi43eyuq5SfVxtG65r6yvFZzR1byc?key=4SgRub88vuVdpJD_jcqH_A)

CNAME: nome verdadeiro para o endereço

TTL: tempo de vida que essa informação fica no cache

**ORDEM:**

- ttl tipo - valor

Teve 1 é resposta, teve 0 é pergunta (query)

Primeiro vem a quantidade de caractere e depois o código ASCII correspondente

Para reduzir o espaço ocupado ele utiliza uma referência para indicar que ele está em outro local do pacote, como se fosse um apontador

"A mail exchanger record (MX record) specifies the mail server responsible for accepting email messages on behalf of a domain name." Ou seja, não é o domínio disposto a aceitar correio, mas sim o servidor responsável por receber as mensagens em nome do domínio.

**ESTUDOS E SURTOS - BIBLIOTECA**

→ Redes muito grandes dão trabalho, logo dividindo-las é mais fácil de se trabalhar. São pequenas redes, ligadas por roteadores.

→ As máscaras IPV4 são um padrão de 32 bits, no qual os bits de 1 vão corresponder no endereço IP, net-id, a partes do endereço da rede, os que forem 0 são de endereçamento do host, host-id.

→ Todos os bits em 0 correspondem ao endereço da rede, tudo em 1 o de broadcast

***FLSN***

→ O subnet-id pode ter tamanho variado ou não (FLSN), o terceiro byte é usado para identificar as subnets (0-255), e o quarto para os hosts address, estes podendo ir de 0 a 255, com um total de 256 subredes distintas

→ Um and lógico entre o IP e a máscara gera o endereço de rede

150.108.2.71 and 255.255.255.0 = 150.108.2.0

→ A máscara deve ser trabalhada com uma sequência de bits contínuos = padrão binário, são 8 bits - vai do mais significativo para o menos, de forma que os hosts variem de forma sequencial

→ Total de endereços host = 2^x(número de bits) - 2, pego o número e coloco em binário, dps pego a quantidade de bits = 1 e retiro, depois disso somo os bits = 0 e elevo 2 a esse valor da soma

→ Intranets podem ser: começadas com: ‘10’ / 192.168 / 172.16 - 172.31

***VLSN***

→ Trabalhar com uma máscara de tamanho variado

→ 192.168.0.0/255.255.255.0

→ Vamos ter tamanhos variados nos hosts pois depende da necessidade do projeto

→ Exemplo: eu uma rede posso precisar de 120 hosts em uma subrede e 50 em outra

Roteamento: processo de escolher um caminho para enviar o datagrama, quem faz isso é o IP, pode utilizar o host para não é ideal porque ele aumenta o tamanho das tabelas de rota

Componentes:

- Determinar que caminhos estão disponíveis
- Selecionar o melhor caminho disponível
- Usar o caminho para atingir o destino
- Decisões locais (ip)

Cada máquina tem uma tabela de rotas:

- Conexão a ser usada para alcançar certa rede
- Custo de usar a rota
- O comando netstat -nr informa a tabela de rotas
- Destino e máscara associada ao destino
- Quando a máscara puder enviar diretamente é 0.0.0.0
- Endereço de loopbacks faz com que os pacotes sejam enviados de volta para a máquina
- Por fim uma rota default, na qual todo endereço encaixa nela, o encaixe de um endereço de destino é operado bit a bit com a máscara e o resultado é comparado com a rota de destino, se for igual o ip marca, quando a máscara for parecida maior a possibilidade do ip escolher a rota, se há duas rotas com números de bits iguais aí a tabela de custo que escolhe
- O ip não cria as rotas por si próprio, existem 3 formas:
1. Rota estática: nós próprios adicionamos - route add 158.108.20.0 158.108.33.1
2. Rotas dinâmicas: via protocolo de roteamento, como lip, oste, eles conversam entre si e pela troca de informações elas são criadas
3. Via ICMP redirect: rotas melhores indicadas por outros roteadores

Padrão CIDR - eliminar as classes abc

- Obrigatório o uso de bits contínuos na máscara de subrede
- Convencional: 200.129.68.0/255.255.255.0 X CIDR: 200.129.68.0/24 (número de bits em 1)
- Pode utilizar tanto as pequenas como agregar elas e formar uma super-rede
- Considere como endereços de host e não de redes, utiliza o endereço da menor rede, encontrar o que “repete”
- E os intervalos de endereço IP públicos são estes:

1.0.0.0–9.255.255.255

11.0.0.0–126.255.255.255

129.0.0.0–169.253.255.255

169.255.0.0–172.15.255.255

172.32.0.0–191.0.1.255

192.0.3.0–192.88.98.255

192.88.100.0–192.167.255.255

192.169.0.0–198.17.255.255

198.20.0.0–223.255.255.255

broadcast - todos os bits em 1

unicast - misturado

loopback - 127

privado - ‘10’ / 192.168 / 172.16 - 172.31

experimental - 200 / multicast

Demultiplexação é a entrega dos dados de um segmento da camada de transporte à porta correta. Acontece na entrega

Multiplexação é reunir no hospedeiro de origem porções de dados provenientes de diferentes portas, de criar segmentos e de passar à camada de rede

Socket API - Sockets

- Suportam os protocolos de camada 3: TCP e UDP. em uma porta, mas a conexão, para troca de dados, pode ser estabelecida em uma outra porta.

**A camada de transporte - TCP**

- serviços fim a fim
- núcleo da hierarquia de protocolos
- serviço básico de transmissão (pode ocorrer perda de pacotes e a desorganização da ordem)
- corrige as limitações da camada de redes
- busca oferecer serviço confiável fim a fim
- **Funções:**
    - Controle de erro - checksum, faltou um pacote, através de retransmissões isso é corrigido → segmentos corrompidos
    - Multiplexação de aplicações - permite que diversas aplicações diferentes enviem seus dados usando uma mesma interface de rede e eles não vão se misturar
    - Controle de fluxo - máquina de origem não sobrecarregue a de destino final → evita que sufoque através do esgotamento de recursos
    - no tcp/ip tem o Controle de congestionamento - evita que as estações intermediárias fiquem congestionadas
    - Nem todos os protocolos oferecem os mesmos serviços, ex: o udp não controla erros e multiplexação de aplicações, a utilização depende da necessidade da aplicação
    - Ressequenciamento - IP pode gerar datagramas fora de ordem
    - Remoção de segmentos duplicados - fruto da estratégia de correção de erros
- **Detalhes tcp/ip:**

- Portas; funcionam como endereços de níveis de transporte

- Chegam multiplexadas e baseada na aplicação são demultiplexadas - separadas - e são enviadas para o número da porta

- 0: não usado / porta dinâmica para cliente

- 1 - 1023: serviços bem conhecidos

- 1024 - 49151: serviços registrados

- 49151 - 65535: portas dinâmicas para clientes

- especificado no RFC 793
- serviço orientado a conexão
- full duplex
- serviço confiável através de ACK, controle de fluxo, controle de congestionamento, recuperação de erros, timers

Sockets: ponto de conexão, par (IP porta), define comunicação de forma única

iP e porta de origem + protocolo + ip e porta de destino

- Gerencia dois streams de dados → um stream do cliente para o servidor e outro do servidor para o cliente ou seja a full-duplex
- Um único socket pode ser usado por vários clientes, sendo ip e portas diferentes ok
- Funções são tidas como confiabilidade para o tcp
    - Implementando a confiabilidade:
1. Números de sequência para identificação
2. Reconhecimento positivo: ACK, dados recebidos na sequência correta
3. Retransmissão de segmentos não reconhecidos dentro de um limite

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdMu1lAbSY7dyKyIBi1XJZDmdDA4ZIvWmme9uBo2EAuQxuEHMUakQyFJGH53fq4eqHQUPSn7D2k3PH4RPNBCyu-j01TEUlegkXD2wwQnh1c9CRlj0tRHpzN0MRlLt2p_S4-nxJ2_s0AVhlvKjNWUHdmpb8?key=AYwFhNlkYxPduN6_DeSwvA)

**FLAG:**

URG - validade do campo - urgent point

ACK - validade do campo - acknowledgment

PSH - passar segmento à aplicação imediatamente

RST - reset na conexão

SYN -  estabelecimento da conexão

FIN - fechamento de um dos lados da conexão

**Options:**

MSS - max segment size - para evitar a fragmentação

WSF - window scale factor - para fazer da janela um número de 32 bits

**Pseudo-Header:**

source iP address e destination iP address    |    não é transmitido no tcp    |    são utilizados na hora de fazer o cálculo do checksum

**Controle de Fluxo**

Espera e envia reconhecimento

Nenhum ACK em um certo tempo ele retransmite o pacote

Tem esse funcionamento por meio do window size - especifica quantos bytes o receptor está pronto para aceitar, enviado o total precisa esperar

Janela deslizante - receptor informa sua janela disponível, em bytes, nos pacotes de reconhecimento, e o remetente ajusta seus envios de acordo com a informação do destinatário

Receptor tem que enviar o ACK com o sequence number enviado

Remetente reseta o timer quando recebe o ACK

Se der time out o remetente reenvia o segmento - utilizado para recuperação de erros

Algoritmo de Karn:

- Leva em consideração ambiguidade de retransmissão
- Se foi retransmitido (recebeu ACK ambíguo) = não atualiza o RTT e timer Backoff = RTO*2
- Se o TCP usa timestamps o algoritmo não é utilizado

Timestamp:

- Melhorar o timeout
- medição mais precisa do RTT
- Quando envia um pacote: insere o tempo atual do relógio no cabeçalho (options), 4 bytes para envio e 4 bytes para o timestamp de reconhecimento do ACK ativo
- Receptor ecoa o timestamp
- Recebe o RTT de qualquer pacote

**DIAGRAMA DE ESTADOS**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcSClD9gYsA4-EDvFIbCEy42EympkRCFNgIE48IkSdyDzZ5qgGGoTWXGmOYcBv9hr80BJBsZ7NtsAHmj-S91vejWQ0l5lZvK5UDdEtut4n24p-248NObYbLaW-IOevpX-aJfQCpv_4Sutw3iak25J44azPB?key=AYwFhNlkYxPduN6_DeSwvA)

- Closed não está ouvindo nem recebendo nada
- Listen está esperando conexão

Passive open - pela listen e pelo accept

o tcp do cliente ainda está close (servidor = socket / bind)

chama o connect - active open - envia o SYN

- Syn sent o cliente envia que está aberto para conexão
- Syn recv o servidor recebe o syn sent do cliente e envia um syn ack (three-way-handshake)

o cliente recebe o syn ack e envia o ack indo para o established

o servidor que estava em syn recv recebe o ack e vai para o established

- Established é a troca de dados - conexão estabelecida
- Time wait
- Close wait recebeu um fin e enviou um ack
- Fin wait 1 tá esperando confirmar
- Fin wait 2 ainda tem dados pendentes
- Last ack espera o último ack para finalizar a conexão

Quem chama close envia FIN

cliente chamou o close e enviou o fin, o fin enviado vai para o servidor que o recebe e devolve um ack indo para o close  wait

quando o ACK é recebido vai para time wait

1. não tem nada para enviar, ele pode encerrar, chama close, e envia logo um fin ack, recebendo um fin ack ele envia um ack indo para o time wait e vai para closed

2. ainda tem dado: não chama close só envia o ack e o outro vai para fin wait 2 pois recebeu só o ack, aguardando que o outro parceiro envie os dados pendentes, quando o parceiro chamar o close ele envia um fin e vai para last ack, que é recebido e vai para o time o wait, devolve um ack, e vai para close

3. os dois chamaram close e foram para fin wait 1, se eu to lá e recebo um fin envio um ack e vou pro close quando o ack é recebido vai para time wait e vai para o closed

MSG_PEEK - retorna dados sem consumir

MSG_DONTWAIT - não bloqueia e caso não haja dados devolve o erro eagain

MSG_WAITALL - bloqueia até que todos os dados sejam lidos

Big-Endian: armazena o mais significativo em cima na parte mais baixa da memória, ex. 01 -  n

Little-Endian: armazena o mais significativo em baixo na parte mais alta da memória, ex. 01 - n+3

**SOCKETS**

API - conjunto de protocolos e apis para comunicação entre processos em máquinas distintas

Domínio Unix - mesma máquina

Internet (TCP/IP): máquinas distintas

→ uniformização do unix - tudo é arquivo

→ Modelo cliente/servidor

→ Praticamente todas as máquinas ligadas a rede utilizam

End Point ou socket: formado por um par ip/porta    |   Portas TCP e UDP são portas distintas  |  Conexão completamente definida por uma tupla de associação

**Rotinas TCP - servidor**

socket - especifica o tipo de socket -  cria o descriptor(n° inteiro que serve para acessar de forma indireta esse recurso dentro do so) de socket - criando um arquivo - especifica se é udp ou tcp

bind - vincula o descriptor com o conceito de socket, o protocolo é relacionado com o par ip porta

listen - o servidor vai estar ouvindo

accept - espera que o cliente se conecte

**Rotinas TCP - cliente**

socket

o cliente não tem o bind geralmente é zero pois pega uma porta livre

connect - especificar a porta que deve se conectar, a porta do cliente e seu endereço são gerados dinamicamente

há a conexão

o cliente chama o send e envia dados para o servidor, este chama o recv para e envia o send ou seja uma resposta, essa resposta é recebida pelo cliente com o recv

netget é monoprocesso - só permite um cliente por vez

para utilizar o fork é necessário que seja uma aplicação multi processo - cria um processo duplicado

**Rotinas UDP - servidor**

socket - especifica o tipo de socket -  cria o descriptor - especifica se é udp ou tcp

bind - vincula o descriptor com o conceito de socket, o protocolo é relacionado com o par ip porta

recvfrom - não tem listen pq não é estabelecido conexão - espera que alguma informação seja recebida

processa - processamento do dado / se for rápido dá entender que está atendendo vários clientes simultaneamente

sendto - envia resposta do servidor

**Rotinas UDP - cliente**

socket - especifica o tipo de socket -  cria o descriptor - especifica se é udp ou tcp

bind - indicando o número de porta zero, pois utiliza as disponíveis

sendto - não precisa estabelecer conexão, ele só envia

recvfrom - recebe a resposta do servidor

**HTTP**

Cliente como navegador web, servidores web

Serve de base para troca

em http pode-se trabalhar com tipos de mídias diferentes

Protocolo TCP, porta 80

1.0 conexões não persistentes

1.1 conexões persistentes / devolve em formato chunked que é em pedaços e mostra o tamanho em bytes de cada parte

2.0 uma série de recursos para melhorar o http 1.0

Não tem estado, pois o servidor não mantém info dos clientes entre as requisições, pois seria mais simples de ser implementado

A performance varia, juá que se trabalhou com o slow start do tcp

***Não persistente:***

1. cliente inicia conexão
2. cliente http envia requisição ao servidor buscando o objeto
3. Servidor recebe a solicitação, acessa o objeto solicitado, monta mensagem de resposta contendo o objeto
4. Servidor fecha imediatamente
5. cliente recebe resposta e fecha seu lado

obs: se precisar de mais objetos ele faz os mesmos passos anteriores, sempre estou abrindo novas conexões já que ela não é persistente, sempre em slow start, diminui a otimização

Pode se ter conexões em paralelo, todas começam com taxa de transferência baixa

***Persistente:***

1. Cliente http inicia conexão
2. cliente envia requisição
3. servidor recebe e acessa o objetou
4. servidor mantém sua conexão aberta
5. cliente recebe a resposta, trata o conteúdo do objeto, e observa que tem umas objeto
6. na mesma conexão ele envia os outros objetos
7. evita o slow start do tdp
8. podem ter paralelos, não necessariamente é otimizado

se botar só barra no GET, ele pega a página default

\r\n = terminadores de linha que indicam que terminou,u é uma linha em branco

***Métodos:***

No head é só o cabeçalho, o objeto não é devolvido

options: o que você suporta? Helo (quais os métodos suportados)

o put é mais usado em apis, alteração no servidor adicionando um novo objeto

trace: depuração, se algo não tá funcionando direito eu posso usar para verificar

Em cada linha tem um rn

No http 1.1 é obrigatório o host no 1.0 é opcional

no accept */* aceita qualquer tipo na resposta

Servidores virtuais na mesma máquina,  esse campo serve para fazer um distinção em quais sites estão sendo usados

O authorization é frágil e pode ser facilmente quebrado

se modificado em tal data traga o objeto se não o cliente usa o que está no cache

versão específica

solicita o login e a senha do usuário

Content-Length é o tamanho em bytes da resposta

Connection se tiver o keep alive mesmo que seja o 1.0 se for suportado pelo servidor ele vai trabalhar com persistente

Content-Encoding o objeto sendo enviado no corpo da entidade está nesse formato, é mais provável na resposta mas também pode ocorrer na requisição

echo -e “METODO /ananda.html HTTP/1.0\r\n\r\n” | nc 192.168.1.6 80

se colocar o host ele dá uma linha a mais com Host: blablabla

Action = ação a ser executada

O post os parâmetros passados através do corpo da entidade, é interessante quando quero passar algo como senhas, pois a informação passa protegida, na autenticação de um sistema por exemplo, ou muitos parâmetros. A query vem vazia

O uso do get pode ser interessante para pegar direto da url, repetir requisições

***Autenticação***

cliente envia

Basic = login e senhas do usuário, isso significa que eles vão trafegar pela rede, o que não é seguro, é apenas codificação não criptografia

o response é sempre o mesmo

Digest = desafio, função de hash que faz a criptografia, envia-se uma uma informação da senha, o servidor possui essa info, se for certo o que o cliente enviou ele libera o acesso

1. Navegador pede login e senha

response muda a cada requisição se as informações variarem

cnonce para cada um, não é possível reaproveitar, vou incrementando o valor da contagem para que o servidor saaiba quantas vezes foi feito

nonce = sequência gerada aleatoriamente pelo servidor

qop = operação devolvida pelo servidor explicitando o mecanismo utilizado

***Cookies:***

set-cookie é do servidor e cookie é do cliente

ambos no campo de cabeçalho

primeira vez que acesso não tenho cookie então o campo de cabeçalho devolve um set-cookie

Proxy: informações grandes e um acesso a internet de baixa qualidade, de modo

***Web Cache:***

Otimizar a performance do http, minimizando o número de requisições dos clientes, reduzindo a quantidade de respostas completas enviadas pelos servidores

Se eu tenho uma info já armazenada localmente ou um proxy web e ela não foi alterada pelo servidor eu envio ela pela rede

Expiração: se já acabou

Validação: se ele foi alterado

**SMTP**

Envio de emails entre servidores

imap - recebe e separa por caixas

pop - recebe

Utiliza conexões tcp, porta 25

mua = envio e recebimento de emails, mail user agent, ex.outlook utiliza o smtp para conversar com o mta

mta = mail transfer agent responsável por receber as solicitações smtp do usuário para enviar o email e utilizar o smtp para encaminhar o email para o destino final, pode-se ter uma cadeia deles

mda = mail delivery agent, responsável por receber e armazenar os emails na mailbox

o destinatário usa o mua para o maa

maa = faz a leitura das caixas de email do usuário

HELO - identifica o cliente junto ao servidor

MAIL FROM - remetente

MAIL TO - destinatário

DATA - informação, para finalizar digita “.”

QUIT - finaliza

220-dime32.dizinc.com ESMTP Exim 4.24 #1 Wed, 26

Mar 2014 05:14:04 -0500

220-We do not authorize the use of this system to

220 transport unsolicited, and/or bulk e-mail.

HELO tupi

250 dime32.dizinc.com Hello tupi [200.141.131.231]

MAIL FROM: leonidas.lima@ifpb.edu.br

250 OK

RCPT TO: leonidas@plugcell.com.br

250 Accepted

DATA

354 Enter message, ending with "." on a line by itself

Exemplo simples de sessão SMTP

From: Leonidas Lima Junior

<leonidas.lima@ifpb.edu.br>

To: leonidas@plugcell.com.br

Subject: Teste 1 do SMTP

Content-Type: TEXT/PLAIN; charset=US-ASCII

Oi SMTP

.

250 OK id=1B6oNf-0004fK-W3

QUIT

221 dime32.dizinc.com closing connection

**POP3**

simples, possui limitações, usa o TCP  como transporte

3 fases:

1. Autorização: cliente faz login no servidor
2. Transação: usuário catuca os emails
3. Atualização: após receber o quit o servidor apaga as mensagens

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe4yRJIh82UXmiUdUdMqg9rAgFIBQOFu347iZldhLS8xF373eikabTAEbwDyJxfQpsy1yiSw3PkaLt14CMAbweEBlDmwMu26iBVBo13MQxA78-4MC-7gyGToMuL-wB4GEACmZeBWi_7_M9-8xVibK5_aQsb?key=AYwFhNlkYxPduN6_DeSwvA)

Todas as respostas são formadas de um indicador de status (+ok e -err)

user - identifica o usuário

pass - envia a senha

stat - devolve informação de status da lista

list - devolve a lista de mensagens

dele - apaga a mensagem

retr - ver conteúdo da mensagem

rset - desmarca as mensagens marcadas como deletadas

quit - encerra a conexão

top - mostra linhas iniciais da mensagem

uidl - devolve emails não deletados

**DNS**

Identificação de hosts

endereços IP e nomes de host

utilizado para relacionar nomes a endereços

base de dados distribuídas

protocolo da camada de aplicação

função interna da internet

Não é relacionado a uma aplicação em particular (todas fazem uso do mesmo tipo de serviço, get host by name e get host by addr)

Por que não centralizar? ponto único de falha, volume de tráfego, problemas de manutenção e base de dados distantes. Não cresce junto com a rede

nenhum servidor dns contém todos os mapeamentos de nomes, se tem os locais, os hosts da rede locais vão primeiro para o servidor de dns

servidor de nomes autoritativo: quando perguntar quem é fulano, ele responde, ele pode fazer um mapeamento de nome para aquele endereço

nome raiz: servidor de nome local, se não ele vai para o de nome autoritativo, se ele encontrar devolve para o local e deixa armazenado

tem 13 tipos de a até m

host contacta o dns local, 200.129.77.52

o 200.129.77.52 contacta o servidor de nome raiz se necessário

e se necessário o servidor de nome raiz contacta o nome autoritativo

a cada passo a informação é adicionada ao cache para que caso seja feita a solicitação novamente o servidor já terá essa informação

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeOAWjeNl6OcGqjo61Rp9HcKeFXdyQGLeROTiKGulHEq7U5ShsLNh8A2As5PLUEBIXbpBM8aDqD_-eYN7HfDiN6fBrA8-tVcQiXibkbQYrsxJhy44CNVzfIlIPOibqCzIvhN09AIfplbMcE8TFJmMDbtk5x?key=AYwFhNlkYxPduN6_DeSwvA)

intermediários = aqueles que devem ser conectados para se encontrar os autoritativos

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXes86tmb_gHtzd5xPJbAuRlA621qH7a84soxSce30bJGhR4EJOgO2wCf-lGujk_-5nJ_vClPuJ3qm5FKYyAZFywEtoN2jAYgICAGZk9-5TjkMMH5eE8YMa9lBnLpNRQpxry1dWluAy552Zgprgw7u05fqAC?key=AYwFhNlkYxPduN6_DeSwvA)

consulta recursiva = o servidor que tá fazendo assume a tarefa de resolução, pode ficar pesada

consulta encadeada = o contactado responde com outro nome de servidor (esse que irá resolver), eu não sei, fala com fulano

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcY6ZYzw6NFJ3rAM6fGJID5djR5hhQ-n1tAwd4JF202Ht7DHm1k2dEe9lcvv2dR6ycJyphkbl8MyPPsgHq7vX882jd-mJbeUwfOpdkg0l-EizbMnYQHKQBHBNdpnZ_AzkOblH1ikADWXghmisZoXoUzebsF?key=AYwFhNlkYxPduN6_DeSwvA)

as informações armazenadas num registro do tipo cache após um tempo se tornam obsoletas

mecanismos de notificação para que essas zonas fiquem atualizadas RFC 1996(notify) e RFC 2136(update)

dns é uma base de dados distribuída que armazena registros de recursos, uma tupla com 5 elementos(name, ttl, class, type, value)

tipo a 1 - name é nome do computador e value é endereço ip

tipo ns 2 -  name é domínio e value é endereço ip do autoritativo para este domínio

tipo cname 5 - name é um apelido e value é nome canônico

tipo mx 15 - vale é o nome do servidor de correuio associado com name

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe5eAVMU6w488G4rQRkz7ciN4hXay-OqTDRSNKFDwi7DEnsLfQ7qJiw_-Ucr8fqNQHOmoabwfHxaLR292RzqDculY1o6yze-4_8hz8We7RLd3cbEAc-QsSDyfsNWEflJg4Fsd-aQq1mhW7KNfl-Ukd8xhM?key=AYwFhNlkYxPduN6_DeSwvA)

Identificação: número de 16 bits para consulta, resposta usa mesmo número

Flags: consulta ou resposta, recursão desejada, recursão disponível, resposta autoritativa

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdn591SaAw2-l1OJA-q1YKwlT8ajMxzX5NUF-u0349W9OsJZu8W1dlseO8pXVjP7rlKWfdwMPQrRzofyMQXvtplyrBF2ox-SoTl4PH-GHUYJPfnCRK37wlP6iOE54TIB43c92TKVqhvFrWEWFkOWO7k03tv?key=AYwFhNlkYxPduN6_DeSwvA)

Porta 53

UDP - até 512 bytes - longas ficam trncadas e chama-se o tcp

TCP - maior que 512 bytes - transmissão entre zonas

**DHCP**

Controle manual de ip

fornece para o servidor: endereço dos servidores dns, endereço de gateway da rede, máscara de sub-rede, endereço ip do host

RFCs 2131 e 2132

Criado para melhorar o funcionamento dos protocolos rarp e bootp

utiliza UDP - cliente → servidor - 67, servidor → cliente - 68

dhcp e rarp

rarp não pode atribuição de endereços hosts desconhecidos

rarp precisa conhecer o mac address, hoje se precisa de mais informações, estas não encontradas pelo rarp

dhcp e bootp

o dhcp tem ip dinâmico, este que tem tempo finito e após seu uso pode ser reutilizado por outro cliente

toda informação necessária para um host tcp/ip é fornecido pelo dhcp

permite a atribuição manual e automática de endereços ip

automática: servidor dhcp atribui endereços ip permanente ao host

manal: o endereço ip do host é estabelecido pelo admin, o servidor dhcp transmite para o cliente

dinâmica: servidor atribui um endereço ip ao host por um intervalo de tempo limitado, chamado lease period (período de aluguel)