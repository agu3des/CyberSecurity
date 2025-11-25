# Certificação Digital |  SSL/TLS | Criptografia

- **Módulo Introdutório**
    
    **Segurança da Informação e Criptografia:** Conjunto de práticas sobre dados que visam garantir integridade, confidencialidade, disponibilidade e não repúdio
    
    - Integridade: não sofreu modificações indevidas (ilegítima ou fraudulenta), intencionalmente ou não.
    - Confidencialidade: acesso somente aos autorizados
    - Disponibilidade: acessíveis a quem for de direito quando solicitado ( ex. ataques: ransomware, DoS, DDoS)
    - Não Repúdio: comprovar se executou ou não uma ação
    
    ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image.png)
    
    **Ataque Man in The Middle:** o atacante se posiciona entre o usuário e o sistema, de modo a obter o tráfego transmitido
    
    **Algoritmos:** conjuntos de passos lógicos para obter um resultado
    
    **Dados:** representações e informações de algo que representa a realidade
    
    **Criptografia:** tornar algo inteligível em algo não inteligível, requer o uso de algoritmo e chave
    
    Tc = Alg (Tp, K) → texto criptografado é um algoritmo aplicado sobre o texto plano em conjunto de uma chave
    
    ex: texto plano=BRASIL - chave=1 - texto cifrado=CSBTJM
    
    ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%201.png)
    
    **Algoritmos Simétricos:** usam a mesma chave criptográfica para suas operações, capazes de cifrar dado largos e são mais rápidos que os assimétricos, porém são mais difíceis de combinar a chave e sua distribuição e são mais difíceis de usar para assinaturas digitais, pois são mais fáceis de serem repudiados.
    
    - 3DES: aplicava 3x o DES (chaves de 64 bits), utiliza chaves de 168 bits, algoritmo de bloco, chama iterações dele mesmo podendo ter as variações de EDE, DED e EEE
    - AES: chaves de 128, 192 e 256 bits, cifra de blocos (cada possui 128 bits) e é o padrão atual para cifras simétricas
    
    ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%202.png)
    
    **Algoritmos Assimétricos:** Não há necessidade de combinar as chaves e é fácil e rápido distribuir de forma segura. Não 
    
    **Chave Criptográfica:** pedaço de texto a ser utilizado por determinado algoritmo para cifrar um dado, também usadas em assinaturas digitais, devem ser protegidas.
    
    - Tamanhos podem variar: Simétricos (AES - 128, 192 e 256 bits | 3DES - 112 e 168 bits) e Assimétricos (RSA - 1024, 2048 e 4096 bits | ECC - 160, 224 e 256…)
    - **Criptografia Simétrica:**
        - Cifras de bloco: dados separados em tamanhos pré-determinados pelo algoritmo e encriptados um bloco por vez, ex: AES e 3DES
        - Cifras de Fluxo: dados encriptados geralmente 1 byte (8 bits) por vez, ex: RC4
    - **Criptografia Assimétrica:** não utiliza a mesma chave, mas sim um par de chaves (pública - encriptação e verificação de assinatura e privada - decriptação e assinatura)
        - Não precisa proteger a chave pública
        - Não permite o repúdio
        - Deve ser computacionalmente fácil gerar a chave pública a partir da privada
        - Deve ser computacionalmente inviável gerar a chave privada a partir da pública
        - Deve ser computacionalmente fácil decifrar uma mensagem encriptada pela chave pública equivalente, ao ter a privada
        - Deve ser computacionalmente inviável, sem a chave privada, decifrar uma mensagem encriptada por uma chave pública equivalente
        - RSA: utiliza dois números primos aleatórios grandes e multiplica os dois (dificultar ataques de força bruta)
            - Chaves de 512, 1024, 2048 e 4096 bits
            - A medida que o tamanho da chave aumenta a segurança também, e a velocidade do processo criptográfico é reduzida
        - ECC: baseado na teoria matemática das curvas elípticas, com velocidade maior e chaves menores (mesma segurança)
            - Chaves 160, 224, 256, 384 e 512 bits
        - Diffie-Hellman: utiçizado para troca de chaves entre pares por um meio inseguro (ex. in ternet), baseado em matemáica modular
        
        ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%203.png)
        
        - **Gestão de chaves:** geração, uso, armazenamento, transferência e expurgo
            - Geração: criar uma chave com base no seu algoritmo
                - Entropia: garantir a aleatoriedade da chave
                - Importação: trazer uma chave já existente para o interior do sistema
                - Exportação: gerar uma cópia de uma chave para ser usada em outro sistema
                - Rotação: troca da chave para outra
            - Transferência: envelope digital, criptograma ou componentes (pedaços da chave)
            - **Segurança da chave:**
                - Hardwares Criptográficos: Smart Card(cartão criptográfico, homologado no Brasil, requer o uso de uma leitora de cartão para uso, possui um chip onde as chaves são armazenadas), Token (token físico, possui conexão usb, possui um chip onde as chaves são armazenadas), HSM (hardware security module, é appliance - servidor, homologado no Brasil, possui conexão com rede, pode servir para diversas aplicações com alta velocidade de resposta, possui fronteira criptográfica - pode se apagar caso aberto, resistente a violação, possui um processador criptográfico)
- **Certificação Digital**
    - **Assinatura Digital:** possibilidade de validar assinatura no mundo digital, traz valor jurídico.
        - Componentes:
            - Chave pública: identificar o autor
            - Chave privada: serve para assinar os documentos
            - Algoritmos assimétricos: facilitar a distribuição das chaves e não repúdio
            - Função hash: determinar o valor único a um conjunto de dados, garante integridade daquilo que foi/será assinado, o resultado é um número hexadecimal, unidirecionais, resistentes a colisão, entrada de tamanho variável, saída de tamanho fixo, ex: MD5, SHA-1, SHA-2, SHA-3, RIPEMD
            
            ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%204.png)
            
            ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%205.png)
            
            Pode ser obtido por: linhas de comando (certutil, openssl), programas (HASHCALC) e linguagens de programação
            
            ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%206.png)
            
            - Dados a serem assinados
        - Passos:
            
            ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%207.png)
            
            1. Hc = função Hash (De)
                1. Hc - hash
                2. De - dados
            2. Ha = Cripto (Hc, Kpri)
                1. Ha - hash assinado
                2. Kpri - chave privada
            3. Anexar Ha no arquivo original
        - Conferência de Assinatura:
        1. Hc = função Hash (De)
            1. Hc - hash
            2. De - dados
        2. Hd = Cripto (Ha, Kpub)
            1. Hd - hash decriptado
            2. Kpub - chave pública
        3. Hc = Hd? Se sim, assinatura válida
            
            ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%208.png)
            
    - **Certificado Digital**
        
        Para conferir uma assinatura digital precisamos conferir o correspondente
        
        Como saber que a chave é de quem ela diz ser
        
        Como relacionar de maneira simples uma chave pública a uma pessoa ou entidade
        
        **Def:** Uma ligação entre uma chave pública e uma entidade através de um formulário chamdo x509, onde teremos as informações do dono da chave, possui propósito de existência (um motivo para o qual foi criado - um certificado digital de nota fiscal não protege uma aplicação web)
        
        **x509:** formulário onde estão escritos os dados relacionados ao certificado
        
        Campos podem variar conforme a autoridade cerificadora e tipo de certificado
        
        Um certificado pode ter cadeias de certificação
        
        **Campos:**
        
        Versão - do certificado
        
        Número de série - número serial de identificação
        
        Emissor: Autoridade certificadora que emitiu
        
        Válido a partir de - data e hora de início da validade
        
        Valido até - data e hora de fim da validade
        
        Requerente - dados do dono do certificado
        
        Chave pública - conteúdo da chave pública relacionada
        
        Nome alternativo - SANs
        
        Uso da chave - para que esta chave pode ser usada
        
        Pontos de distr. CRl - endereços onde se pode consultar lista de certificados relevantes
        
        .cer ou .crt - extensão do arquivo de certificado 
        
        O certificado pode estar em pessoal ou outras pessoas
        
    - **Autoridade Certificadora**
        
        Qualquer pessoa pode criar e utilizar das mesmas informações.
        
        Alguma instituição de confiança mútua confirme as entidades suas identidades, confirme a ligação da chave pública com o certificado e a entidade, conhecidas como terceiro confiável
        
        **PKI ou ISP:** infraestrutura de chaves públicas, são um conjunto de hardware, software e processos construídos para garantir a posse de uma chave pública às entidades 
        
        As autoridades podem ser de cadeia nacional ou internacional, são vinculadas a uma autoridade superior que as regulamenta, são responsáveis pela fiscalização das documentações das entidades
        
        Podem ser de dois tipos: 
        
        - Online: permanecem ligadas o tempo todo, assinam os certificados das ACs intermediárias e também das entidades finais
        - Offline: ficam desligadas a maioria sendo ativadas apenas para que uma nova AC tenha o seu certificado assinado
        
        Temos a ICP Brasil que é ligada ao ITI que a fiscaliza
        
    - **Cadeias de Certificação**
        
        Um site tem um certificado assinado pela chave privada de uma certificadora de nível intermediário, esta certificadora intermediária foi assinada por uma chave privada de uma autoridade certificadora raiz
        
        ACs de abrangência nacional vão, em sua maioria, requisitar a instalação manual
        
    - **Autoridades de Registro**
        
        São elas que conferem as documentações e informações enviadas das entidades que requisitam um certificado digital (ACs também podem fazer isso) as ACs
        
    - **Revogação de Certificados**
        
        Ocorre quando uma entidade final dona do certificado revoga seu uso por motivos de segurança
        
        Possíveis motivos:
        
        - Não será mais utilizado
        - Chave privada relacionada foi exposta
        - Erros na emissão
        - Roubo do certificado
        
        As ACs tem que ter meios para conferência da revogação. 
        
        1. CRL é uma lista com certificados revogados, é menos seguro pois pode demorar um tempo
        2. OCSP consulta em tempo real ao status do certificado, sendo considerado mais seguro
        
    
    ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%209.png)
    
- **Protocolo SSL/TLS**
    - Arquitetura Computacional
        - Processador: executa tarefas consultadas a partir da memória principal (RAM)
        - Memória Principal (RAM): armazena instruções a serem consultadas pelo processador para execução, sendo volátil.
        - Hard Disk (HD): mantém dados de arquivos e programas salvos (persistidos) mesmo com o desligamento do computador. Capaz de armazenar dados mais largos do que a RAM e o processador. Mais lento.
        
        ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%2010.png)
        
    - Processos
        
        Um programa quando armazenado na RAM se chama processo
        
        Um processo pode estar isolado dentro de sua máquina, ou se comunicar com outros computadores
        
        Socket: um processo em um computador fica em listening esperando a conexão de outros processos de outros computadores, para a obtenção de dados.
        
    - Modelo Cliente Servidor
        
        Um processo rodando em um computador servidor servindo um processo a um computador cliente
        
        Servidores: HTTP, servidor de emails
        
        Clientes: MS Outlook, web browser
        
        ex: chrome <=>  apache
        
        - Comunicação entre computadores
            - HTTP: hipertext tranfer protocol, é o principal protocola da web, e basicamente toda a internet se desenvolveu sobre ele. Não tem criptografia nativa.
            - HTTP + SSL: hipertext transfer protocol over secure socket layer - https
            - SMTP: Simple mail transfer protocol, utilizado na transmissão de emails, não faz criptografia nativa mas suporta o SSL
            - FTP: file transfer protocol, utilizaddo na transferência de arquivos, não faz criptografia nativa mas suporta o SSL
        
        Fragilidade de segurança: os protocolos não são baseados em criptografia
        
        Qualquer MITM pode interceptar a comunicação e pegar os dados trafegados.
        
        O desenvolvedor pode aplicar diretamente no programa e isso torna necessário conhecimento de criptografia, não haveria padrão de mercado nem testes seguros e confiáveis.
        
    
    SSL - Secure Socket Layer: traz segurança através de algoritmos públicos e testados, com padrão de aplicação. 
    
    Originalmente desenvolvido pela NETSCAPE. 
    
    O seu sucessor é o TLS - Transport layer security, que é o que utilizamos atualmente. 
    
    Capaz de prover autenticidade e confidencialidade às comunicações.
    
    Dados são criptografados na camada 6 do modelo OSI.
    
    - Versões:
        - SSL 1.0 - nunca lançada devido às falhas de segurança
        - SSL 2.0 - lançada em 1995, declarada obsoleta em 2011
        - SSL 3.0 - lançada em 1996, declarado obsoleto em 2015
        - TLS 1.0 - lançado em 1999, atualização do SSL 3.0
        - TLS 1.1 - lançado em 2006, atualmente obsoleto
        - TLS 1.2 - lançado em 2008, em vigência atualmente
        - TLS 1.3 - lançado em 2018, em vigência atualmente
    
    Componentes: chave privada e pública, certificado digital, autoridade certificadora, algoritmos simétricos e assimétricos
    
    - **Funcionamento do protocolo:**
        
        → Processo cliente requisita recurso ao servidor 
        
        → Processo servidor envia o certificado digital (que foi emitido por uma autoridade certificadora 
        
        → Processo cliente checa o certificado 
        
        → Processo cliente encripta uma chave simétrica com uma chave diffie-hellman (para transportar com segurança)
        
        Ciphersuíte: conjunto de algoritmos que protegem uma comunicação em rede
        
        Escolhe um set5 de algoritmos, cada qual com sua finalidadde. 
        
        Ex: TLS_DHE_DSS_WITH_AES_256_CBC_SHA256     
        
        ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%2011.png)
        
        ![image.png](Certifica%C3%A7%C3%A3o%20Digital%20SSL%20TLS%20Criptografia%201fa2e5a697c380129c4cc6fcc2390c78/image%2012.png)
        
    
    Cliente Hello: inicia a comunicação
    
    Cipher swite: seleção de protocolos de vários tipos para a comunicação criptografada. Fala para o chrome que consegue se comunicar de forma segura através desses protocolos
    
    Server Hello: servidor responde como deseja se comunicar dentre os que o cliente enviou
    
    Change cipher spec: já temos um acordo pode-se iniciar a comunicação criptografada. Inicialmente enviada pelo servidor e depois confirmada pelo cliente
    
    Application data: informações protegidas e criptografadas 
    
    - **Caso de Uso**
        
        **APACHE:** servidor web (http), pode ser instalado em win ou linux. Normalmente roda aplicações feitas em PHP e outras linguagens de programação.
        
        **TOMCAT:** servidor web (http), pode ser instalado no win ou no linux. Normalmente roda aplicações feitas em java.
        
        **IIS:** servidor web (http), pode ser instalado em win. Roda aplicações feitas em linguagens de programação ASP.NET.
        
        **SMTP:** servidor envio de emails (bind9, exchange, etc). Pode ser instalado em diversos sistemas, a depender da implementação.
        
        Ao manipular tecnicamente certificados SSL, é importante compreender da melhor forma possível seu caso de uso.
        
        Isso permitirá entender as instruções técnicas conforme sua necessidade, proporcionando uma solução mais rápida e adequada.
        
        Atente-se para: sistema utilizado, versões, localização da implementação, entre outras informações.
        
        Outros exemplos: proteção de APIs, mobile, autenticação, proxys, firewalls, openbanking
        
    
    **Assinatura de código:**
    
    Não criptografa comunicações, criptografam sistemas.
    
    Ao compilar o código se tem um exe, pode ser benéfico ou maléfico, de modo que se faz necessário algo que valide.
    
    Utilizar programas assinados por um desenvolvedor conhecido.
    
    - **Emissões de certificados:**
        1. Gerar a chave privada 9pode ser pela aplicação que fará o uso ou ferramentas externas)
        2. CSR (PKCS#10) - requisição de assinatura de certificado
        3. Formatos dos arquivos de certificados: 
            - PEM (certificados, CSR, cadeias de codificação, chaves públicas, chaves privadas),
            - CER (certificados e chaves públicas, não armazenam chaves privadas e utiliza a codificação base64)
            - CRT (representam certificados/chaves públicas, não armazenam chaves privadas e utiliza a codificação base64)
            - DER (representam certificados/chaves públicas, não armazenam chaves privadas e utiliza a codificação binária)
            - KEY (representa certificados/chaves públicas, podem armazenar chaves privadas, utiliza codificação base64)
            - PFX (pode conter chave privada/pública/cadeias de determinado certificado digital, é criptografado, pode ser protegido por senha quando importado ou exportado)
            - P12 (pode conter chave privada/pública/cadeias de determinado certificado, é criptografado, pode ser protegido por senha quando importado ou exportado)
            - JKS (pode conter chave privada/pública/cadeias de determinado certificado, largamente utilizado para proteção de aplicações feitas em java)
            
            Ferramentas comuns: 
            
            1. OPENSSL: ferramenta opensource, de linha de comando, é uma das mais completas ferramentas para o uso criptográfico   
            2. CERTUTIL: de linha de comando, roda em windows, possui suíte de diversos comandos para criptografia e certificação digital
            3. linha de comando, roda em ambientes onde há java instalado, assim como o OPENSSL é uma suíte muito completa de comandos para servidores java
    
    **Tipos de Validação de Certificados**
    
    - Diversos processos são feitos para testar a validação da entidade (dono) de um certificado antes de sua emissão
    - Isso serve para minimizar o risco de fraudes, o que representaria sérios problemas para a segurança dos usuários e aplicações
        - Domain Validation - feito apenas sobre o domínio do cliente após alguma prova de controle, é mais barata, porém mais simples e menos segura (ex: alguém pode ter acesso ao email do dono do site e ter emitido o certificado)
        - Organization Validation - checagem de domínio + checagens adicionais, preço intermediário, nesta modalidade ganha-se muito mais segurança no processo contra fraudes
        - Extended Validation - extensa e profunda validação da instituição é feita antes da emissão do certificado, mais cara, processo mais seguro para emissões
    
    **Wildcard** - um tipo de certificado que funciona quando temos um domínio único, utilizando-se diversos nomes na primeira parte do FQDN.
    
    ex: *.meusite.com.br → domínios: vendas.meusite.com.br, tecnologia.meusite.com.br
    
    **San Subject Alternative Name** - um domínio alheio ao domínio principal daquele certificado, mas que também será protegido por ele.
    
    ex: [treinamentossl.com.br](http://treinamentossl.com.br) | [treinamentos-seginfo.com.br](http://treinamentos-seginfo.com.br) | [treinamento-it.com.br](http://treinamento-it.com.br) 
    
    **Prova de Controle:** é uma ação que o administrador do sistema faz perante a AC para comprovar o controle técnico sobre aquele domínio a receber um certificado
    
    - Prova de controle por email: envia-se um e-mail de validação para o e-mail cadastrado no whois (com token de validação). Caso as instruções sejam bem sucedidas, entende-se que o controle do domínio existe. É mais fácil de ser implementada, sendo que sempre deve-se avaliar se a mesma é possível.
    - Validação por URL: é enviado um token de validação para o cliente, se o cliente conseguir adicionar o token em determinado arquivo de seu site, e o sistema da AC puder ler, o controle está aprovado. Usar quando o cliente não possui acesso na conta whois por algum motivo.
    - Validação por DNS: é enviado um token de validação para o cliente, se o cliente conseguir adicionar o token em um TXT RECORD em seu DNS autoritativo, e o sistema da AC puder ler, o controle está aprovado. Deve ser usado apenas em último caso devido a necessidade de um tempo de até 2h para sua replicação.

    Validação de CAA: Configuração de segurança, trata-se de uma configuração com o DNS autoritativo permitindo que determinada AC emita certificados em nome do domínio 

    IIS - recurso do windows que pode ser ativado

    https://support.globalsign.com/pt-br

    Para te ajudar com a tarefa de geração e manipulação de certificados SSL, preparei um guia detalhado com os comandos `openssl` para cada etapa que você solicitou.

    -----

    ### **Gerando um Certificado Autoassinado**

    Um certificado autoassinado é útil para ambientes de teste e desenvolvimento, pois ele não é emitido por uma Autoridade Certificadora (CA) confiável.

    * **Comando:**
        ```bash
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout minha_chave_privada.key -out meu_certificado.crt
        ```
    * **O que você precisa saber:**
        * `-x509`: Cria um certificado autoassinado em vez de uma requisição de certificado (CSR).
        * `-nodes`: "No DES" — não encripta a chave privada.
        * `-days 365`: Define a validade do certificado para 365 dias.
        * `-newkey rsa:2048`: Gera uma nova chave privada RSA de 2048 bits.
        * `-keyout minha_chave_privada.key`: Nome do arquivo onde a chave privada será salva.
        * `-out meu_certificado.crt`: Nome do arquivo onde o certificado será salvo.
        * Durante a execução, você precisará preencher algumas informações, como país, estado, cidade, organização e, o mais importante, o **Common Name (CN)**, que deve ser o nome de domínio ou o endereço IP do servidor.

    -----

    ### **Testando um Certificado em Serviço de Rede**

    Você pode usar o `openssl` para verificar a conexão SSL com um servidor e inspecionar o certificado que ele está apresentando.

    * **Comando:**
        ```bash
        openssl s_client -connect www.exemplo.com:443
        ```
    * **O que você precisa saber:**
        * `s_client`: O comando que atua como um cliente SSL/TLS.
        * `-connect www.exemplo.com:443`: O endereço do servidor e a porta (geralmente 443 para HTTPS).
        * Após o comando, o terminal mostrará os detalhes da conexão, como a versão do protocolo, a cifra utilizada e os dados do certificado do servidor. Pressione `CTRL+C` para sair.

    -----

    ### **Gerando um Arquivo PFX (PKCS\#12)**

    O formato **PFX** (ou PKCS\#12) é um contêiner que armazena a chave privada e o certificado em um único arquivo, protegido por senha. É muito comum em servidores Microsoft IIS e em algumas outras plataformas.

    * **Comando:**
        ```bash
        openssl pkcs12 -export -out meu_certificado.pfx -inkey minha_chave_privada.key -in meu_certificado.crt
        ```
    * **O que você precisa saber:**
        * `pkcs12 -export`: Indica que a ação é de exportar para o formato PKCS\#12.
        * `-out meu_certificado.pfx`: Nome do arquivo de saída.
        * `-inkey minha_chave_privada.key`: Arquivo da chave privada.
        * `-in meu_certificado.crt`: Arquivo do certificado.
        * Você será solicitado a criar uma senha para proteger o arquivo PFX.

    -----

    ### **Gerando PFX com Cadeias de Certificação**

    Quando você tem um certificado emitido por uma CA, é essencial incluir os **certificados intermediários** (cadeias) para que o navegador do usuário possa validar a confiança do seu certificado.

    * **Comando:**
        ```bash
        openssl pkcs12 -export -chain -out meu_certificado_com_cadeia.pfx -inkey minha_chave_privada.key -in meu_certificado.crt -certfile cadeia_intermediaria.crt
        ```
    * **O que você precisa saber:**
        * `-chain`: Comando que instrui a inclusão da cadeia de certificação.
        * `-certfile cadeia_intermediaria.crt`: O arquivo que contém os certificados intermediários. Você pode concatenar vários certificados intermediários em um único arquivo `.crt`.

    -----

    ### **Desmembrando um Arquivo PFX**

    Para extrair a chave privada, o certificado e a cadeia de certificados de um arquivo PFX, você pode usar este comando. Isso é útil quando você precisa migrar um certificado para um servidor que exige arquivos separados.

    * **Comando:**
        ```bash
        openssl pkcs12 -in meu_certificado.pfx -out meu_arquivo_extraido.pem -nodes
        ```
    * **O que você precisa saber:**
        * `pkcs12 -in meu_certificado.pfx`: Especifica o arquivo PFX de entrada.
        * `-out meu_arquivo_extraido.pem`: Define o nome do arquivo de saída. Este arquivo `.pem` conterá a chave privada, o certificado e a cadeia.
        * `-nodes`: Desabilita a encriptação na chave privada extraída.
        * Você precisará fornecer a senha do arquivo PFX.

    Após a execução, o arquivo `meu_arquivo_extraido.pem` conterá todos os elementos. Para separá-los em arquivos individuais, você pode simplesmente copiar e colar o conteúdo em arquivos separados, respeitando as marcações de `-----BEGIN ...` e `-----END ...`.

- **KEYTOOL**
    

- **TROUBLESHOOTING SSL/TLS**

    - **SSL SHOPEE**

        Esse termo não é um problema técnico padrão. Geralmente, ele pode se referir a um erro específico que ocorre ao tentar acessar o site da Shopee ou a problemas com a segurança de transações online.

        **Como resolver:**

        * **Verifique o relógio do sistema:** Se a data e a hora do seu computador estiverem incorretas, isso pode causar erros de certificado. Corrija-as para a data e hora atuais.
        * **Limpe o cache e os cookies:** Dados antigos de navegação podem causar conflitos. Tente limpar o cache do seu navegador.
        * **Teste em outro navegador:** Se o problema persistir, tente acessar o site da Shopee em um navegador diferente para ver se o problema está no navegador que você usa.
        * **Atualize seu navegador:** Certifique-se de que a versão do seu navegador está atualizada.


    - **Common Name incorreto**

        O **Common Name (CN)** é o nome de domínio principal que o certificado SSL protege. Se o CN no certificado não corresponder ao domínio que o usuário está tentando acessar, o navegador exibirá um aviso de segurança.

        **Como resolver:**

        * **Gerar um novo certificado:** A solução mais eficaz é gerar um novo **CSR** (Certificate Signing Request) com o **Common Name** correto.
        * **Verificar o URL:** Certifique-se de que a URL digitada no navegador corresponde exatamente ao nome de domínio no certificado. Inclua ou remova o `www.` conforme o caso.
        * **Usar um certificado Wildcard:** Se você precisa proteger múltiplos subdomínios, considere usar um certificado **Wildcard** (ex.: `*.seudominio.com.br`) que cobrirá todos eles.


    - **Certificado desaparecendo do IIS**

        Isso pode ser um problema de permissões, corrupção do certificado ou um bug no próprio **IIS (Internet Information Services)**.

        **Como resolver:**

        * **Verificar o Certificado no Repositório:** Use o `MMC (Microsoft Management Console)` para verificar se o certificado ainda está no armazenamento de certificados do computador. Se estiver, pode ser necessário reimportá-lo no IIS.
        * **Checar Permissões:** Certifique-se de que a conta de serviço do IIS tem permissão de leitura para a chave privada do certificado.
        * **Reiniciar o IIS:** Em alguns casos, um simples `iisreset` no Prompt de Comando (executado como administrador) pode resolver o problema.

    - **Caminho da chave ou certificado incorretos**

        Se o servidor não conseguir encontrar o arquivo do certificado ou da chave privada, a instalação falhará.

        **Como resolver:**

        * **Verifique o caminho:** Certifique-se de que o caminho especificado para o certificado (arquivo `.crt` ou `.cer`) e para a chave privada (arquivo `.key`) está correto e não contém erros de digitação.
        * **Checar as permissões:** A conta do usuário ou serviço que está tentando acessar o certificado precisa de permissões de leitura para os arquivos e o diretório onde estão armazenados.
        * **Usar o formato correto:** Verifique se os arquivos estão no formato esperado pelo seu servidor web (por exemplo, Apache e Nginx usam arquivos `.crt` e `.key`).

    - **Checando match entre key, CSR e Certificado Digital**

        A chave privada, o **CSR** e o certificado devem ser gerados em conjunto. Se houver uma incompatibilidade, a instalação do certificado falhará.

        **Como resolver:**

        * **Use OpenSSL:** Você pode usar o **OpenSSL** para verificar se os arquivos correspondem. Execute os seguintes comandos para extrair e comparar os hashes:

            * **Extrair o hash da chave privada:**
                `openssl rsa -noout -modulus -in seuchave.key | openssl md5`
            * **Extrair o hash do CSR:**
                `openssl req -noout -modulus -in seucsr.csr | openssl md5`
            * **Extrair o hash do certificado:**
                `openssl x509 -noout -modulus -in seucertificado.crt | openssl md5`

            Se os hashes **não forem idênticos**, você precisará gerar um novo **CSR** e solicitar um novo certificado.

    - **Problema de validação CAA - Zona de DNS**

        **CAA (Certificate Authority Authorization)** é um registro DNS que permite que o proprietário de um domínio especifique quais **CAs (Certificate Authorities)** estão autorizadas a emitir certificados para esse domínio. Se você tiver um registro **CAA** e a CA que você usou não estiver na lista, a validação falhará.

        **Como resolver:**

        * **Verifique seu registro CAA:** Use uma ferramenta de pesquisa de DNS para ver se seu domínio tem um registro **CAA**.
        * **Remova ou atualize o registro:** Se você tiver um registro **CAA** que não inclui a sua **CA**, você deve removê-lo ou adicionar um novo registro que permita a emissão pela sua **CA** preferida.

    - **Problemas de cadeia de certificação**

        Um certificado **SSL** não é um arquivo único. Ele é parte de uma cadeia de confiança que vai do seu certificado de domínio até a CA raiz. Se o servidor não enviar a cadeia completa para o navegador do cliente, o navegador não conseguirá validar a confiança. Isso resulta no erro "cadeia de certificação incompleta" ou "não confiável".

        **Como resolver:**

        * **Instale o certificado intermediário:** Você deve instalar o seu certificado de domínio e também os certificados **intermediários** que foram fornecidos pela sua **CA**.
        * **Verifique a instalação:** Use uma ferramenta online como o **SSL Shopper Checker** para verificar se a cadeia de certificação está completa e se não há problemas de configuração.