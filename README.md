<h1>Synthify</h1>

Desenvolvido em parceria com a empresa Softtek,  Sinthify é uma plataforma inovadora desenvolvida especificamente para  equipes de suporte técnico,
com o objetivo de tornar seu trabalho não só mais produtivo, mas também mais assertivo, elevando o atendimento ao  cliente a um novo patamar.
 <br><br>Utilizando tecnologias como HTML e CSS no front-end, JavaScript e Python no back-end, aliada à inteligência artificial generativa, 
a Sinthify transforma a maneira como as equipes de suporte técnico operam, analisando o histórico de tickets e documentações, 
resumindo e extraindo as informações mais relevantes, e sugerindo  respostas embasadas de forma rápida.

Assim, proporcionamos soluções  mais eficientes, precisas e adaptadas às necessidades de cada cliente.

<h1>Guia de Instalação e Configuração</h1>
<p>Este guia fornece instruções para configurar e executar a aplicação localmente. Certifique-se de seguir todos os passos para garantir o correto funcionamento do projeto.</p>

<h2>Requisitos</h2>
<ul>
<li><strong>Python 3.11.9</strong> instalado no sistema.</li>
<li><strong>Virtualenv 20.26.2</strong> para criação de ambientes virtuais.</li>
<li>API Key da OpenAI.</li>
<li>Secret Key do Django para a configuração da aplicação.</li>
<li>O upload de arquivos atualmente é suportado apenas para os formatos <strong>.docx</strong> e <strong>.xlsx</strong>.
<ul>
<li>O arquivo <strong>.xlsx</strong> deve obrigatoriamente conter as seguintes colunas: <strong>'Sintoma'</strong>, <strong>'Descrição'</strong> e <strong>'Resolução'</strong>.</li>
</ul>
</li>
</ul>
<h2>Passo a Passo para Configuração</h2>

<h3>1. Instale o Python e o Virtualenv</h3>
<ul>
<li><strong>Python 3.11.9</strong>: Caso ainda não tenha instalado, baixe a versão mais recente do Python em <a href="https://www.python.org/downloads/">python.org</a>.</li>
<li><strong>Virtualenv 20.26.2</strong>: Instale o virtualenv com o seguinte comando:
<pre><code>pip install virtualenv==20.26.2</code></pre>
</li>
</ul>

<h3>2. Baixe o Projeto</h3>
<p>Clone o repositório ou faça o download dos arquivos do projeto.</p>

<h3>3. Abra o Projeto no VSCode</h3>
    <p>Certifique-se de ter o <a href="https://code.visualstudio.com/">Visual Studio Code</a> instalado.</p>

<h3>4. Crie um Ambiente Virtual</h3>
<p>No terminal integrado do VSCode ou em outro terminal de sua preferência, navegue até o diretório do projeto e crie um ambiente virtual utilizando o seguinte comando:</p>
<pre><code>python3 -m venv .venv</code></pre>
<p><strong>Dica:</strong> Caso o VSCode não configure automaticamente o ambiente virtual, você pode ir até a barra de pesquisa do VSCode e configurar o ambiente Python para o diretório do seu <code>.venv</code>.</p>

<h3>5. Ative o Ambiente Virtual</h3>
<p>Dependendo do sistema operacional que você estiver utilizando, o comando para ativar o ambiente virtual será diferente:</p>
<ul>
<li><strong>Windows</strong>:
<pre><code>.venv\Scripts\activate</code></pre>
</li>
<li><strong>MacOS/Linux</strong>:
<pre><code>source .venv/bin/activate</code></pre>
</li>
</ul>

<h3>6. Instale as Dependências</h3>
<p>Com o ambiente virtual ativado, instale todas as dependências necessárias que estão listadas no arquivo <code>requirements.txt</code>:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>7. Aplique as Migrações</h3>
<p>Para garantir que o banco de dados esteja devidamente configurado, execute as migrações do Django:</p>
<pre><code>python manage.py migrate</code></pre>

<h3>8. Configure as Variáveis de Ambiente</h3>
<p>Na raiz do projeto, crie um arquivo <code>.env</code> com as seguintes variáveis:</p>
<pre><code>OPENAI_API_KEY='sua_chave_openai_aqui'
SECRET_KEY='sua_chave_secreta_aqui'</code></pre>

<p><strong>Gerar a SECRET_KEY do Django</strong>: Se ainda não tiver uma chave secreta, você pode gerar uma utilizando o comando abaixo (com o ambiente virtual ativado):</p>
<pre><code>python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'</code></pre>
<p>Caso ocorra algum erro, você pode optar por inserir a chave manualmente no arquivo <code>settings.py</code> do projeto.</p>

<h3>9. Execute o Servidor Local</h3>
<p>Agora, execute o servidor local do Django com o seguinte comando:</p>
<pre><code>python manage.py runserver</code></pre>

<h3>10. Acesse a Aplicação</h3>
 <p>No terminal, aparecerá um link para o servidor local (geralmente, <code>http://127.0.0.1:8000/</code>). Segure a tecla <strong>Ctrl</strong> e clique no link para abrir a aplicação no navegador.</p>

<h2>Notas Adicionais</h2>
<ul>
<li>O arquivo <strong>.docx</strong> deve estar formatado corretamente, sem elementos que possam comprometer a extração dos dados.</li>
<li>O formato <strong>.xlsx</strong> deve seguir as colunas obrigatórias mencionadas acima para que o sistema processe corretamente as informações.</li>
<li>Certifique-se de que a chave da API OpenAI tem permissões adequadas para utilizar os serviços necessários (ex: GPT-4).</li>
</ul>
