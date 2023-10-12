### API de Gerenciamento de Pessoas ✅

Uma RESTful API construída em Django Rest Framework, seguindo os princípios do SOLID.

## Principais Tecnologias
 - **Django**: Um poderoso framework web em Python que ajuda a criar aplicativos robustos e escaláveis.
 - **Docker**: Utilizando Docker Multi-Stage para otimização.
 - **Restframework (django)**: Uma poderosa e flexível toolkit para construir Web APIs.

## Diagrama de Classes (Domínio da API)

```mermaid
classDiagram
  class Pessoa {
    + nome: string
    + email: Email
    * birth_date: date
    + cpf: CPF
    + endereco: Endereco
    + cadastrar(nome: string, email: Email, cpf: CPF, endereco: Endereco): type
    + validar(): boolean
  }

  class Email {
    + address: string
    + validar(): boolean
  }

  class CPF {
    + cpf_number: string
    + validar(): boolean
  }

  class Endereco {
    + logradouro: string
    + numero: integer
    + complemento: string
    + bairro: string
    + cidade: string
    + estado: string
    + cep: string
    + validar(): boolean
  }

  Pessoa "1" *-- "1" Email
  Pessoa "1" *-- "1" CPF
  Pessoa "1" *-- "1" Endereco

```


URL de da api: http://localhost:8000/v1/api/users/
