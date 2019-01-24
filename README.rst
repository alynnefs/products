============================================
DjangoRest
============================================

Esse projeto consiste em um CRUD de produtos.

Primeiramente, clone o projeto. Instale python3 e pip. É aconselhado fazer isso em uma virtualenv.

Requisitos
=======

- Python 3.6.7
- pip 19.0.1 (python 3.6)

Obs: todos os comandos a seguir devem ser executados na raiz do projeto (pasta products).

Install
=======

.. code-block:: console

    make setup
    
Durante o setup será solicitado nome de usuário, email e senha, que serão usados para fazer login no sistema.

Documentação
=======

.. code-block:: console

    make showdoc
    
Está configurado para abrir no Firefox. Caso não tenha instalado, você pode consultar a documentação abrindo esse arquivo: ``djangoRest/doc/_build/html/index.html``

Testes
=======
.. code-block:: console

    make test
    
Como executar
=======
.. code-block:: console

    make run

Pelo navegador, acesse ``http://127.0.0.1:8000``. Você irá se deparar com a seguinte imagem:

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/01.png
   :width: 600
   
Note que em detail há a mensagem "Authentication credentials were not provided". Isso acontece porque você não está logado.

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/02.png
   :width: 600
   
Após se logar, aparecerá o link ``http://127.0.0.1:8000/products/``. Você pode clicar nele ou adicionar ``products/`` na barra de endereço.

Obs: se você não estiver logado, por mais que mude o link pela barra de endereço, continuará aparecendo a mensagem "Authentication credentials were not provided".

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/03.png
   :width: 600
   
Após clicar no link, aparecerá essa tela de listagem de produtos. Como ainda não adicionamos nenhum produto, "results" está vazio.

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/04.png
   :width: 600
   
Você pode adicionar produtos através desse formulário:

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/05.png
   :width: 600
   
A seguir temos o resultado da adição:

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/06.png
   :width: 600
   
Você pode adicionar quantos produtos quiser.

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/07.png
   :width: 600

Se você clicar, por exemplo, em ``http://127.0.0.1:8000/products/1``, é possível editar o produto selecionado.

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/08.png
   :width: 600
   
Lista de produtos depois da edição:

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/09.png
   :width: 600
   
Na tela de edição também é possível excluir.

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/10.png
   :width: 600
   
Vamos excluir o produto2 (``http://127.0.0.1:8000/products/2``) clicando no botão "delete".

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/11.png
   :width: 600
   
Após confirmar, o produto2 não estará mais presente na lista de produtos.

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/12.png
   :width: 600
   
Adicionei mais dois produtos para mostrar o funcionamento dos filtros.

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/13.png
   :width: 600
   
Nomes ordenados de forma crescente:

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/14.png
   :width: 600
   
O resultado está a seguir:

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/15.png
   :width: 600
   
   
Também é possível procurar por nome.

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/16.png
   :width: 600
   
Resultado do filtro:

.. image:: https://github.com/alynnefs/testeConceptu/blob/master/img/17.png
   :width: 600
