# Envio de emails c/python

## sobre:
- pequena aplicação feita com um codigo de envio de emails.
- utiliza a linguage python.
- utiliza o framework django.
- envia textos em html convertidos para txt.
- facil formatação do texto enviado.

## como rodar na sua maquina:
- primeiramente você deverá clonar esse projeto para sua maquina.
- crie uma venv no projeto.
- ative essa venv.
- instale o django no projeto.
- instale a biblioteca python decouple.
- crie um arquivo chamado .env na raiz do projeto.
- no .env cole o codigo disponibilizado, colocando seus dados corretamente.

<br>
<details>
 <summary> <b>👨‍💻 venv no Windows: </b> <i>(ver mais)</i> </summary>
  <br>
<div >
  <b>- digite no terminal:</b>
  <pre><code>
    $ python -m venv venv
    $ venv\Scripts\activate
  </code></pre>
 </div>
</details>

<details>
 <summary> <b>👨‍💻 venv no Linux/MacOs: </b> <i>(ver mais)</i> </summary>
  <br>
<div >
  <b>- digite no terminal:</b>
  <pre><code>
    $ python3 -m venv venv
    $ source venv/bin/activate
  </code></pre>
 </div>
</details>

<details>
 <summary> <b>👨‍💻 instalar python decouple: </b> <i>(ver mais)</i> </summary>
  <br>
<div >
  <b>- digite no terminal:</b>
  <pre><code>
    $ pip install python-decouple
  </code></pre>
 </div>
</details>

<details>
 <summary> <b>👨‍💻 codigo do .env: </b> <i>(ver mais)</i> </summary>
  <br>
<div >
  <b>digite no arquivo .env:</b>
  <pre><code>
    EMAIL_HOST_USER=seu_email
    EMAIL_HOST_PASSWORD=sua_senha
    EMAIL_USE_TLS=True
    EMAIL_PORT=587
    EMAIL_HOST=smtp_do_seu_provedor_de_email
  </code></pre>
 </div>
</details>
- Para entrar em contato, me mande um <a href="mailto:devglaubermonteiro@gmail.com">Email</a>.
