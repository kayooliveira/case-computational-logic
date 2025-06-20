## **Estudo de Caso Computational Logic using Python**

**Desenvolvendo um Sistema de Controle de Estoque com Python: Soluções para Gerenciamento em uma Loja de Eletrônicos**

## **Cenário**

Este projeto visa a criação de um sistema de controle de estoque para uma loja de eletrônicos. O sistema deve ser capaz de gerenciar produtos, incluindo a adição de novos itens, a atualização de produtos existentes e a visualização do estoque, além de prever funcionalidades adicionais para um gerenciamento completo.

## **Desafio (Foco Inicial)**

A primeira etapa do projeto concentra-se em desenvolver a **estrutura inicial do sistema**, aplicando conceitos fundamentais de **lógica computacional** e **controle de fluxo em Python**. O objetivo é construir a base que permitirá futuras expansões e integrações.

### **Funcionalidades Essenciais da Primeira Etapa**

*   **Menu de Opções**: Implementar um menu interativo para o usuário, permitindo a seleção de diferentes funcionalidades do sistema.
*   **Adicionar Produto**: Solicitar **Nome**, **Preço** e **Quantidade em estoque** para registrar novos produtos. Deve-se verificar se o produto já existe para adicionar novas entradas.
*   **Atualizar Produto**: Pedir o **nome do produto** a ser atualizado e solicitar as novas informações de **Preço** e **Quantidade em estoque**.
*   **Excluir Produto**: Pedir o **nome do produto** a ser removido do estoque.
*   **Visualizar Estoque**: Mostrar uma lista clara e organizada de todos os produtos, incluindo **Nome**, **Preço** e **Quantidade em estoque**.
*   **Sair do Sistema**: Opção para finalizar a execução da aplicação.

## **Conceitos de Teoria na Prática (Fundamentação Técnica)**

O desenvolvimento deste sistema é uma oportunidade prática para aplicar conceitos teóricos de programação:

*   **Lógica Computacional, Controle de Fluxo e Estruturas de Dados**: São a base para transformar o conhecimento em soluções funcionais.
*   **Estruturas Condicionais (IF, ELSE)**: Essenciais para verificar situações específicas, como a existência de um produto ao adicionar ou a validade de dados (e.g., em futuras funcionalidades de vendas).
*   **Loops (FOR, WHILE)**: Desempenham um papel crucial ao percorrer listas de produtos (e vendas), permitindo que o sistema organize e exiba informações de forma eficiente. Também auxiliam na repetição contínua de verificações.
*   **Estruturas de Dados**: A escolha adequada de **listas**, **dicionários** ou **classes de objetos** é fundamental para armazenar e organizar informações de produtos, garantindo que os dados sejam acessíveis e eficientes.
*   **Interface Amigável**: Mesmo em um sistema simples de linha de comando, um menu de opções claro melhora a experiência do usuário.
*   **Boas Práticas de Programação**: A aplicação de técnicas como a **organização clara do código**, **comentários explicativos** e **modularização** é vital para tornar o sistema legível e fácil de manter.

## **Levantamento de Soluções (Estratégias de Implementação)**

Antes de iniciar o código, é crucial planejar as estratégias:

*   **Funcionalidades Necessárias (Visão Geral)**: Além das funcionalidades da primeira etapa, o sistema final deve também registrar e controlar vendas, vinculando-as a produtos e clientes.
*   **Mecanismos de Controle de Fluxo**: Uso estratégico de `IF/ELSE` para validações e `FOR/WHILE` para iteração e exibição de dados.
*   **Interface do Usuário e Experiência**: Foco na criação de uma interação clara e intuitiva através de menus, mesmo que em um ambiente de linha de comando.
*   **Boas Práticas de Programação**: Implementar modularização, usar variáveis com nomes claros e adicionar comentários para garantir um código limpo e de fácil manutenção.

## **Tecnologias Utilizadas**

*   **Linguagem de Programação**: Python

## **Entregável**

O resultado do projeto deve ser um **arquivo `.py`** contendo toda a programação desenvolvida.

---

# **Passo-a-Passo para Desenvolver a Aplicação**

Este roteiro guiará você no desenvolvimento do sistema de controle de estoque em Python, aplicando os conceitos de lógica computacional e controle de fluxo, conforme os requisitos do projeto.

### 1. **Configuração Inicial e Estrutura de Dados**

*   **Crie um arquivo Python**: Inicie seu projeto criando um arquivo `.py` (ex: `controle_estoque.py`).
*   **Defina a estrutura de dados para o estoque**:
    *   Escolha uma estrutura apropriada para armazenar seus produtos, como uma **lista de dicionários** ou uma **lista de objetos de uma classe `Produto`** (se preferir uma abordagem orientada a objetos).
    *   Exemplo (lista de dicionários): `estoque = []`.
    *   Esta estrutura conterá os campos: `Nome do produto`, `Preço do produto` e `Quantidade em estoque` para cada item.

### 2. **Criação do Menu Principal e Loop de Execução**

*   **Implemente um loop principal**: Utilize um **loop `while True`** para que o sistema continue em execução até que o usuário decida sair.
*   **Exiba o menu de opções**: Dentro do loop, use `print()` para mostrar as opções ao usuário: "1. Adicionar Produto", "2. Atualizar Produto", "3. Excluir Produto", "4. Visualizar Estoque", "5. Sair".
*   **Solicite a escolha do usuário**: Peça ao usuário para digitar um número correspondente à opção desejada.
*   **Utilize estruturas condicionais**: Empregue **`if/elif/else`** para direcionar o fluxo do programa com base na entrada do usuário, chamando a função correspondente para cada opção. A opção "Sair" deve usar `break` para finalizar o loop.

### 3. **Implementação da Funcionalidade "Adicionar Produto"**

*   **Crie uma função** (ex: `adicionar_produto()`):
    *   Dentro dela, solicite o **Nome**, **Preço** e **Quantidade em estoque** do novo produto ao usuário.
    *   **Verifique duplicidade**: Antes de adicionar, percorra a lista `estoque` (com um **loop `for` ou `while`**) e utilize uma **estrutura condicional `if`** para verificar se um produto com o mesmo nome já existe.
    *   **Adicione o produto**: Se o produto não for encontrado, crie um novo dicionário (ou objeto) com as informações fornecidas e adicione-o à sua lista `estoque`. Caso contrário, informe o usuário que o produto já existe.

### 4. **Implementação da Funcionalidade "Atualizar Produto"**

*   **Crie uma função** (ex: `atualizar_produto()`):
    *   Peça ao usuário o **Nome do produto** que deseja atualizar.
    *   **Localize o produto**: Percorra a lista `estoque` (com um **loop `for` ou `while`**) para encontrar o produto correspondente ao nome informado.
    *   **Atualize as informações**: Se o produto for encontrado, solicite o **novo Preço** e a **nova Quantidade em estoque**. Em seguida, atualize os valores no dicionário (ou objeto) do produto. Informe o usuário se o produto não for encontrado.

### 5. **Implementação da Funcionalidade "Excluir Produto"**

*   **Crie uma função** (ex: `excluir_produto()`):
    *   Peça ao usuário o **Nome do produto** a ser excluído.
    *   **Localize e remova**: Percorra a lista `estoque` (com um **loop `for` ou `while`**) para encontrar o produto pelo nome.
    *   Se encontrado, remova o produto da lista `estoque`. Informe o usuário se a exclusão foi bem-sucedida ou se o produto não foi encontrado.

### 6. **Implementação da Funcionalidade "Visualizar Estoque"**

*   **Crie uma função** (ex: `visualizar_estoque()`):
    *   **Verifique se o estoque está vazio**: Primeiro, verifique se a lista `estoque` não está vazia. Se estiver, informe ao usuário.
    *   **Exiba os produtos**: Se houver produtos, utilize um **loop `for` ou `while`** para percorrer a lista `estoque`.
    *   Para cada produto, imprima de forma organizada o **Nome**, **Preço** e **Quantidade em estoque**.

### 7. **Aplicação de Boas Práticas de Programação**

*   **Modularize o Código**: Mantenha cada funcionalidade em sua própria função para melhorar a **legibilidade** e a **manutenção** do código.
*   **Comentários Explicativos**: Adicione **comentários** (`#`) ao longo do seu código para explicar a lógica complexa ou partes importantes.
*   **Nomes de Variáveis Claros**: Use nomes descritivos para variáveis e funções (ex: `nome_produto`, `quantidade_estoque`).
*   **Validação de Entrada**: Embora não detalhado no desafio inicial, é uma boa prática validar as entradas do usuário (ex: garantir que preço e quantidade sejam números). Isso pode ser feito com blocos `try-except` para tratamento de erros.

### 8. **Testes e Refinamento**

*   **Execute e Teste**: Após implementar cada funcionalidade, execute seu sistema e teste todas as opções (adicionar, atualizar, excluir, visualizar e sair) para garantir que funcionam conforme o esperado.
*   **Refine a Experiência do Usuário**: Faça pequenos ajustes na formatação das mensagens ou no menu para tornar a interação mais agradável.

### 9. **Preparação para o Entregável**

*   **Verifique o arquivo `.py`**: Certifique-se de que todo o seu código está contido em um único arquivo `.py` e que ele pode ser executado sem erros.
