# desafio-venda-mais
 
1 - baixe o arquivo zip.
2 - extraia o arquivo zip.
3 - abra o arquivo descompactado.
4 - va na barra de endereço da pasta, click e digite 'cmd' e Enter, para abrir essa pasta usando o cmd.
5 - digite 'venv\Scripts\activate' e Enter, para ativar ambiente virtual.
6 - digite 'cd admin_django' e Enter, para acessar a sub-pasta 'admin_django'.
7 - digite 'python manage.py runserver' e Enter, para rodar o servidor.
8 - o endereço do server será informado logo em seguida, algo como: http://127.0.0.1:8000/. 
9 - Acesse o server usando o endereço informado, ao acessar você vera apenas 'TESTES' na página.
-----------------------------------------------ACESSANDO A ÁREA ADMINISTRATIVA----------------------------------------------------------
10 - digite '/admin' logo apos o enderenço, http://127.0.0.1:8000/admin.
11 - o superusuario criado que tem total autorização é o 'gerente' seu usuário é 'gerente' e sua senha é 'gerente123' (senha muito fácil apenas para fins de testes).
12 - na área 'usuarios' é possível criar novos usuarios (atendentes, helpers ou até novos gerentes).
13 - na área 'grupos' é possível adicionar ou retirar usuarios nos grupos de ' atendentes' e 'helpers', onde é possível limitar seu acesso as funcionalidades do projeto.
14 - em 'atendimentos' é possível registrar, consultar serviços cadastrados pelos atendentes ou gerentes, ao ir em adicionar será possível adicionar o seu primeiro serviço.
-----------------------------------------------CRIANDO UM ATENDIMENTO----------------------------------------------------------
15 - depois de logado, ao ir em 'Atendimento' e 'ADICIONAR ATENDIMENTO' você é redirecionado para a página em que preenche os detalhes do atendimento.
16 - Para adicionar o atendimento, preencha as informações a seguir:
 16.1 - informe o Servico que inclui limpeza simple e profunda.
 16.2 - informe qual Atendente cadastrado no site está atendendo.
 16.3 - informe qual Helper está executando o serviço.
 16.4 - em 'preço', Este campo não é necessário preencher, ao selecionar o serviço ele preenchera automaticamente.
 16.5 - informe a forma de pagamento, onde tem disponível 'espécie, cartão de crédito, cartão de débito, PIX e cheque'.
 16.6 - informe a 'Data de cadastro'.
 16.7 - informe a 'Data do servico'.
 16.8 - selecione 'Status' entre 'pendente, realizado ou cancelado'.
 16.9 - informe o 'Nome do cliente'.
 16.10 - informe o 'Telefone do cliente'.
 16.11 - informe o 'Endereço do cliente'.
 16.12 - Por fim, com todos os dados obrigatórios preenchidos, click em salvar.
17 - ao acessar 'Atendimentos' novamente será possível ver o atendimento adicionado e os outros existentes (se houver)
