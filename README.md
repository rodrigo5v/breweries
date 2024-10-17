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
Após a instalação do WSL, escolha uma distribuição de sua preferência. Você pode instalar uma distribuição a partir da Microsoft Store.
No meu caso utilizei o Ubuntu

###3. Configurar o Ambiente WSL
- Abra o WSL e atualize os pacotes:
   ```bash
   sudo apt update && sudo apt upgrade -y

- Instale o Python:
   ```bash
   sudo apt install python3

