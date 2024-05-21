## Sistema Bancário Simples em Python

Este projeto é um sistema bancário básico desenvolvido em Python, permitindo que os usuários realizem operações como depósito, saque e visualização de extrato.

### Funcionalidades:

- **Depósito:** Permite que os usuários depositem valores positivos em suas contas.
- **Saque:** Permite que os usuários sacam dinheiro, com um limite diário de 3 saques e R$ 500,00 por saque. 
- **Extrato:** Exibe um histórico de todas as operações (depósitos e saques) realizadas na conta, incluindo o saldo atual.

### Como Executar:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/dio-sistema-bancario.git
   ```

2. **Navegue até o diretório do projeto:**

   ```bash
   cd dio-sistema-bancario
   ```

3. **Execute o script:**

   ```bash
   python banco.py
   ```

4. **Interaja com o sistema bancário:**
   - Selecione as opções do menu para realizar as operações desejadas.
   - Siga as instruções na tela para inserir os valores necessários.

### Observações:

- O sistema trabalha com apenas um usuário e não possui autenticação.
- O saldo inicial é R$ 0,00.
- O limite diário de saques é de 3 saques, com R$ 500,00 por saque.

### Melhorias Potenciais:

- Implementar autenticação de usuários.
- Adicionar funcionalidades como transferências entre contas, histórico de extratos e cálculo de juros.
- Criar uma interface gráfica (GUI) para melhorar a experiência do usuário.

### Contribuições:

Contribuições são bem-vindas! Se você tiver alguma sugestão ou melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Licença:

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
