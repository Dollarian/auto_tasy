Guia de Instalação e Configuração do Ambiente
Este documento orienta sobre como configurar o ambiente para o funcionamento de um sistema automatizado usando Python, Selenium, e outras ferramentas necessárias. Ele descreve o processo de instalação, execução dos arquivos de configuração e também fornece uma solução manual para casos de erro.

Passo 1: Instalação do Python
1.1 Baixar e Instalar o Python 3.12
Acesse o site oficial do Python:
https://www.python.org/downloads/

Faça o download da versão mais recente do Python 3.12.

Durante a instalação, marque a opção "Add Python to PATH" para garantir que o Python seja configurado corretamente no seu sistema.

Complete a instalação.

Passo 2: Executar o Arquivo setup.bat
Após a instalação do Python, siga os seguintes passos para executar a configuração automática do ambiente:

Abra o Explorador de Arquivos e navegue até a pasta onde o arquivo setup.bat está localizado.

Execute o arquivo setup.bat. Este script irá realizar os seguintes processos automaticamente:

Executar no_rest: Desabilita a restauração de abas no Chrome.
Executar pip: Instala os drivers necessários do Selenium para o Python.
Executar reg: Modifica o registro do Windows para garantir que o sistema inicie automaticamente para o usuário cadastrado.
Executar start: Copia o arquivo tasy para a pasta de inicialização do Windows.
Para iniciar o processo, basta dar um duplo clique no arquivo setup.bat.

Passo 3: O que Cada Arquivo Realiza
Arquivo no_rest
Esse arquivo contém a configuração necessária para desabilitar a restauração automática de abas no Google Chrome. Isso pode ser importante para a automação, garantindo que o navegador não restaure sessões anteriores.

Arquivo pip
Este arquivo instala os drivers do Selenium, permitindo que o Python interaja com o Chrome de maneira automatizada. A instalação dos pacotes e drivers será feita automaticamente por este script.

Arquivo reg
O arquivo reg altera o registro do Windows para adicionar a aplicação à inicialização automática do usuário cadastrado. Isso garante que o sistema esteja sempre em funcionamento sem necessidade de intervenção manual.

Arquivo start
O arquivo start copia o arquivo tasy para a pasta de inicialização do Windows. Isso significa que, ao iniciar o Windows, o arquivo será executado automaticamente.

Passo 4: Resolução Manual de Problemas
Caso o processo automático falhe ou você prefira realizar as configurações manualmente, siga as etapas descritas abaixo.

4.1 Pasta "Arquivos de Instalação Manual"
Dentro do diretório de instalação, você encontrará uma pasta chamada "Arquivos de Instalação Manual". Esta pasta contém os scripts necessários para realizar as configurações manualmente.

Desabilitar a Restauração de Abas no Chrome (no_rest)

Navegue até o diretório Arquivos de Instalação Manual.
Abra o arquivo no_rest.bat e execute-o manualmente. Isso garantirá que a restauração de abas seja desabilitada no Google Chrome.
Instalar os Drivers do Selenium (pip)

Abra o terminal (cmd) e navegue até o diretório Arquivos de Instalação Manual.
Execute o arquivo pip.bat para instalar o Selenium e os drivers necessários:
bash
Copy
pip install selenium
Modificar o Registro do Windows (reg)

Navegue até a pasta Arquivos de Instalação Manual.
Execute o arquivo reg.bat para realizar a modificação no registro do Windows que adiciona o aplicativo à inicialização.
Copiar Arquivo para Inicialização (start)

Navegue até a pasta Arquivos de Instalação Manual.
Execute o arquivo start.bat, que irá copiar o arquivo tasy para a pasta de inicialização do Windows.
4.2 Verificando e Corrigindo Erros
Caso algum dos scripts falhe, verifique os seguintes pontos:

Python: Certifique-se de que o Python foi instalado corretamente e está no PATH do sistema.
Permissões de Administrador: Alguns scripts podem precisar de permissões elevadas para modificar o registro do Windows ou acessar pastas de sistema. Se necessário, execute o arquivo .bat como Administrador (clique com o botão direito e escolha "Executar como administrador").
Dependências do Selenium: Verifique se o Selenium foi instalado corretamente com o comando pip show selenium no terminal. Caso não tenha sido, execute novamente o script pip.bat ou instale manualmente via terminal:
bash
Copy
pip install selenium
