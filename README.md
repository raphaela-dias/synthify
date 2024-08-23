<h1>Synthify</h1>

Desenvolvido em parceria com a empresa Softtek,  Sinthify é uma plataforma inovadora desenvolvida especificamente para  equipes de suporte técnico,
com o objetivo de tornar seu trabalho não só mais produtivo, mas também mais assertivo, elevando o atendimento ao  cliente a um novo patamar.
 <br><br>Utilizando tecnologias como HTML e CSS no front-end, JavaScript e Python no back-end, aliada à inteligência artificial generativa, 
a Sinthify transforma a maneira como as equipes de suporte técnico operam, analisando o histórico de tickets e documentações, 
resumindo e extraindo as informações mais relevantes, e sugerindo  respostas embasadas de forma rápida.

Assim, proporcionamos soluções  mais eficientes, precisas e adaptadas às necessidades de cada cliente.

<h2>Como utilizar</h2>

<b>Nota: É necessário ter uma API Key da OpenAI e uma Secret Key do Django</b>
<br><b>Nota 2: O upload de arquivos funciona apenas com .xml e .xlsx</b>
<br><b>Nota 3: O arquivo .xlsx obrigatoriamente deve conter as colunas 'Sintoma', 'Descrição' e 'Resolução'</b>

1. Instale o Python 3.11.9

2. Baixe os arquivos do projeto

3. Abra o projeto no VSCode

4. Crie um ambiente virtual `.venv` com `python3.11 -m venv .venv` no terminal ou use a barra de pesquisa do VS Code para configurar o ambiente ao abrir um arquivo Python

5. Ative o ambiente virtual com o comando `.venv/Scripts/Activate` (Windows) `nome_do_ambiente/bin/activate` (MacOS/Linux)

6. Instale as dependências que estão em `requirements.txt` na `.venv`

7. Aplique as migrações com o comando `python manage.py migrate`

8. Na raiz do projeto, crie um arquivo .env e insira as chaves nas variáveis `OPENAI_API_KEY=`'sua_chave_openai_aqui' e `SECRET_KEY=`'sua_chave_secreta_aqui' como strings

9. Execute o comando `python manage.py runserver` no terminal

10. Selecione as teclas Ctrl + click no link do servidor local
 
 
