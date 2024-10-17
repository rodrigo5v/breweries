<div align="center">
    <img src="https://github.com/user-attachments/assets/b7d9a629-d340-4ba2-a8a5-23d42164b364" alt="Minha Imagem" width="500"/>
</div>

# Configurando WSL

Este guia fornece um passo a passo para configurar e executar o case em um ambiente Windows Subsystem for Linux (WSL).

## Pré-requisitos

- **Windows 10 ou superior** com WSL instalado
- **Python 3.6 ou superior** instalado no WSL
- **Pip** (gerenciador de pacotes do Python)

## Passo a Passo

### 1. Instalar o WSL

Se você ainda não tem o WSL instalado, siga estes passos:

- Abra o PowerShell como Administrador e execute:

  ```bash
  wsl --install
  
### 2. Escolher uma distro Linux
Após a instalação do WSL, escolha uma distribuição de sua preferência, no meu caso utilizei o Ubuntu. A instalação da distribuição é a partir da Microsoft Store.

### 3. Configurar o Ambiente WSL
- Abra o WSL e atualize os pacotes:
   ```bash
   sudo apt update && sudo apt upgrade -y

- Instale o Python:
   ```bash
   sudo apt install python3

- Instale o Java (JDK):
  ```bash
  sudo apt install default-jdk
Obs: será preciso inserir a senha que você definiu para seguir essa etapa.

- Espere o download ser realizado e ao final utilize esse comando para verificar a instalação:
  ```bash
  java --version

- Instalando o Spark
Para instalar o Apache Spark será necessário mudar para o usuário root, então utilize esse comando:
    ```bash
    sudo su
    
Em seguida será preciso criar um diretório para o spark, então rode o seguinte comando:
    ```bash
    mkdir -p /opt/spark
    cd /opt/spark

Acesse [akafa](https://spark.apache.org/downloads.html) e selecione a versão desejada do Apache Spark (em vermelho). Em seguida clique no link apresentado (em preto):
<div align="center">
    <img src="[https://github.com/user-attachments/assets/b7d9a629-d340-4ba2-a8a5-23d42164b364](https://github.com/user-attachments/assets/2e0cbb2f-f3cb-4a71-9daa-aa0b9b09f287)" alt="Minha Imagem" width="500"/>
</div>

Você será redirecionado para outra página. Copie qualquer um dos links (em vermelho):
<div align="center">
    <img src="https://github.com/user-attachments/assets/7a91d9b3-e7e8-4b99-bb20-9728e6e2f201" alt="Minha Imagem" width="500"/>
</div>

No meu caso utilizei a versão **3.5.3 do Apache Spark**.

Voltando ao seu terminal utilize o seguinte comando:
    ```bash
    wget https://dlcdn.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz

Espere o download ocorrer e utilize o seguinte comando:
    ```bash
    
