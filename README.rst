============================================
DjangoRest
============================================

.. image:: https://travis-ci.org/alynnefs/products.svg?branch=master
    :target: https://travis-ci.org/alynnefs/products
    :alt: Test Status
    
Esse projeto consiste em um CRUD de produtos.

Primeiramente, clone o projeto. Instale python3 e pip. É aconselhado fazer isso em uma virtualenv.

Requisitos
=======

- Python 3.6.7
- pip 19.0.1 (python 3.6)

Obs: todos os comandos a seguir devem ser executados na raiz do projeto (diretório products).

Install
=======

.. code-block:: console

    sudo apt install curl
    sudo apt install httpie
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

- Pelo navegador

Acesse ``http://127.0.0.1:8000``. Você irá se deparar com a seguinte imagem:

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

- Pelo terminal sem login:

- CREATE

.. code-block:: console

   $ http --form POST http://127.0.0.1:8000/products/ name="post" price=1
   HTTP/1.1 401 Unauthorized
   Allow: GET, POST, HEAD, OPTIONS
   Content-Length: 58
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 17:42:10 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   WWW-Authenticate: JWT realm="api"
   X-Frame-Options: SAMEORIGIN

   {
       "detail": "Authentication credentials were not provided."
   }

- READ

.. code-block:: console

   $ http GET http://127.0.0.1:8000/products/
   HTTP/1.1 401 Unauthorized
   Allow: GET, POST, HEAD, OPTIONS
   Content-Length: 58
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 17:41:23 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   WWW-Authenticate: JWT realm="api"
   X-Frame-Options: SAMEORIGIN

   {
       "detail": "Authentication credentials were not provided."
   }

- UPDATE

.. code-block:: console

   $ http --form PUT http://127.0.0.1:8000/products/1/ name="testeUpdateHTTP" price=2
   HTTP/1.1 401 Unauthorized
   Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
   Content-Length: 58
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 17:43:28 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   WWW-Authenticate: JWT realm="api"
   X-Frame-Options: SAMEORIGIN

   {
       "detail": "Authentication credentials were not provided."
   }

- DELETE

.. code-block:: console

   $ http --form DELETE http://127.0.0.1:8000/products/1/
   HTTP/1.1 401 Unauthorized
   Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
   Content-Length: 58
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 17:44:06 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   WWW-Authenticate: JWT realm="api"
   X-Frame-Options: SAMEORIGIN

   {
       "detail": "Authentication credentials were not provided."
   }

Obs: Todos eles com a mensagem "Authentication credentials were not provided.", já que não informamos usuário e senha.

- Pelo terminal com login:

- READ

.. code-block:: console

   $ http GET http://127.0.0.1:8000/products/ --auth alynne:123456
   HTTP/1.1 200 OK
   Allow: GET, POST, HEAD, OPTIONS
   Content-Length: 1413
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 17:24:08 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN

   {
       "count": 2,
       "next": null,
       "previous": null,
       "results": [
           {
               "description": "adasds",
               "name": "teste",
               "price": 3.14,
               "url": "http://127.0.0.1:8000/products/1/"
           },
           {
               "description": null,
               "name": "teste",
               "price": 9.0,
               "url": "http://127.0.0.1:8000/products/7/"
           }
       ]
   }

- CREATE

.. code-block:: console


   http --form POST http://127.0.0.1:8000/products/ name="testeHTTP" price=1.99 --auth alynne:123456
   HTTP/1.1 201 Created
   Allow: GET, POST, HEAD, OPTIONS
   Content-Length: 95
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 17:23:10 GMT
   Location: http://127.0.0.1:8000/products/10/
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN

   {
       "description": null,
       "name": "testeHTTP",
       "price": 1.99,
       "url": "http://127.0.0.1:8000/products/10/"
   }

Resultado:

.. code-block:: console

   $ http GET http://127.0.0.1:8000/products/ --auth alynne:123456
   HTTP/1.1 200 OK
   Allow: GET, POST, HEAD, OPTIONS
   Content-Length: 1413
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 17:24:08 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN

   {
       "count": 3,
       "next": null,
       "previous": null,
       "results": [
           {
               "description": null,
               "name": "testeHTTP",
               "price": 1.99,
               "url": "http://127.0.0.1:8000/products/10/"
           },
           {
               "description": "adasds",
               "name": "teste",
               "price": 3.14,
               "url": "http://127.0.0.1:8000/products/1/"
           },
           {
               "description": null,
               "name": "teste",
               "price": 9.0,
               "url": "http://127.0.0.1:8000/products/7/"
           }
       ]
   }

- UPDATE

.. code-block:: console

   $ http --form PUT http://127.0.0.1:8000/products/1/ name="testeUpdateHTTP" price=2 --auth alynne:123456
   HTTP/1.1 200 OK
   Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
   Content-Length: 103
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 17:27:10 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN

   {
       "description": "adasds",
       "name": "testeUpdateHTTP",
       "price": 2.0,
       "url": "http://127.0.0.1:8000/products/1/"
   }

Resultado:

.. code-block:: console

   $ http GET http://127.0.0.1:8000/products/ --auth alynne:123456
   HTTP/1.1 200 OK
   Allow: GET, POST, HEAD, OPTIONS
   Content-Length: 1422
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 17:27:32 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN

   {
       "count": 3,
       "next": null,
       "previous": null,
       "results": [
           {
               "description": "adasds",
               "name": "testeUpdateHTTP",
               "price": 2.0,
               "url": "http://127.0.0.1:8000/products/1/"
           },
           {
               "description": null,
               "name": "testeHTTP",
               "price": 1.99,
               "url": "http://127.0.0.1:8000/products/10/"
           },
           {
               "description": null,
               "name": "teste",
               "price": 9.0,
               "url": "http://127.0.0.1:8000/products/7/"
           }
       ]
   }

- DELETE

.. code-block:: console

   $ http --form DELETE http://127.0.0.1:8000/products/7/ --auth alynne:123456
   HTTP/1.1 204 No Content
   Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
   Content-Length: 0
   Date: Thu, 24 Jan 2019 17:29:35 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN


Resultado

.. code-block:: console

   $ http GET http://127.0.0.1:8000/products/ --auth alynne:123456
   HTTP/1.1 200 OK
   Allow: GET, POST, HEAD, OPTIONS
   Content-Length: 978
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 17:29:57 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN

   {
       "count": 2,
       "next": null,
       "previous": null,
       "results": [
           {
               "description": "adasds",
               "name": "testeUpdateHTTP",
               "price": 2.0,
               "url": "http://127.0.0.1:8000/products/1/"
           },
           {
               "description": null,
               "name": "testeHTTP",
               "price": 1.99,
               "url": "http://127.0.0.1:8000/products/10/"
           }
       ]
   }


Outros exemplos de obtenção de dados sem GET:

- Pelo terminal com ``curl``

http://127.0.0.1:8000/

.. code-block:: console

    $ curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/
    {
        "detail": "Authentication credentials were not provided."
    }
    
http://127.0.0.1:8000/products/

.. code-block:: console

   $ curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/products/
   {
        "detail": "Authentication credentials were not provided."
   }
   
http://127.0.0.1:8000/products/1/

.. code-block:: console

   $ curl -H 'Accept: application/json; indet=4' http://127.0.0.1:8000/products/1/
   {
       "detail": "Authentication credentials were not provided."
   }
   
Observe que todos possuem a resposta "Authentication credentials were not provided". Isso acontece porque não há nenhum usuário logado. Vamos usar usuário e senha criados no setup. Nesse exemplo, o usuário é "alynne" e a senha é "123456".

http://127.0.0.1:8000/

.. code-block:: console

   $ curl -H 'Accept: application/json; indent=4' -u alynne:123456 http://127.0.0.1:8000/
   {
       "products": "http://127.0.0.1:8000/products/"
   }

http://127.0.0.1:8000/products/

.. code-block:: console
   
   $ curl -H 'Accept: application/json; indet=4' -u alynne:123456 http://127.0.0.1:8000/products/
   {
       "count": 4,
       "next": null,
       "previous": null,
       "results": [
           {
               "url": "http://127.0.0.1:8000/products/1/",
               "name": "teste",
               "price": 3.14,
               "description": "adasds"
           },
           {
               "url": "http://127.0.0.1:8000/products/2/",
               "name": "produto2",
               "price": 2.0,
               "description": null
           },
           {
               "url": "http://127.0.0.1:8000/products/3/",
               "name": "produto",
               "price": 1.0,
               "description": null
           },
           {
               "url": "http://127.0.0.1:8000/products/4/",
               "name": "produto",
               "price": 1.0,
               "description": null
           }
       ]
   }

http://127.0.0.1:8000/products/1/

.. code-block:: console

   $ curl -H 'Accept: application/json; indet=4' -u alynne:123456 http://127.0.0.1:8000/products/1/
   {
       "url": "http://127.0.0.1:8000/products/1/",
       "name": "teste",
       "price": 3.14,
       "description": "adasds"
   }

- Pelo terminal com ``http``

http://127.0.0.1:8000/

.. code-block:: console

   $ http http://127.0.0.1:8000/
   HTTP/1.1 401 Unauthorized
   Allow: GET, HEAD, OPTIONS
   Content-Length: 58
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 16:05:52 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   WWW-Authenticate: JWT realm="api"
   X-Frame-Options: SAMEORIGIN

   {
       "detail": "Authentication credentials were not provided."
   }
   
http://127.0.0.1:8000/products/

.. code-block:: console

   $ http http://127.0.0.1:8000/products/
   HTTP/1.1 401 Unauthorized
   Allow: GET, POST, HEAD, OPTIONS
   Content-Length: 58
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 16:06:11 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   WWW-Authenticate: JWT realm="api"
   X-Frame-Options: SAMEORIGIN

   {
       "detail": "Authentication credentials were not provided."
   }

http://127.0.0.1:8000/products/1/

.. code-block:: console

   $ http http://127.0.0.1:8000/products/1/
   HTTP/1.1 401 Unauthorized
   Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
   Content-Length: 58
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 16:06:32 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   WWW-Authenticate: JWT realm="api"
   X-Frame-Options: SAMEORIGIN

   {
       "detail": "Authentication credentials were not provided."
   }

Observe que todos possuem a resposta "Authentication credentials were not provided". Isso acontece porque não há nenhum usuário logado. Vamos usar usuário e senha criados no setup. Nesse exemplo, o usuário é "alynne" e a senha é "123456".

http://127.0.0.1:8000/

.. code-block:: console

   $ http -a alynne:123456 http://127.0.0.1:8000/
   HTTP/1.1 200 OK
   Allow: GET, HEAD, OPTIONS
   Content-Length: 46
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 16:07:00 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN

   {
       "products": "http://127.0.0.1:8000/products/"
   }

http://127.0.0.1:8000/products/

.. code-block:: console

   $ http -a alynne:123456 http://127.0.0.1:8000/products/
   HTTP/1.1 200 OK
   Allow: GET, POST, HEAD, OPTIONS
   Content-Length: 1222
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 16:07:17 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN

   {
       "count": 4,
       "next": null,
       "previous": null,
       "results": [
           {
               "description": "adasds",
               "name": "teste",
               "price": 3.14,
               "url": "http://127.0.0.1:8000/products/1/"
           }
           {
               "description": null,
               "name": "produto2",
               "price": 2.0,
               "url": "http://127.0.0.1:8000/products/2/"
           },
           {
               "description": null,
               "name": "produto",
               "price": 1.0,
               "url": "http://127.0.0.1:8000/products/3/"
           },
           {
               "description": null,
               "name": "produto",
               "price": 1.0,
               "url": "http://127.0.0.1:8000/products/4/"
           }
       ]
   }

http://127.0.0.1:8000/products/1/

.. code-block:: console

   $ http -a alynne:123456 http://127.0.0.1:8000/products/1/
   HTTP/1.1 200 OK
   Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
   Content-Length: 94
   Content-Type: application/json
   Date: Thu, 24 Jan 2019 16:07:38 GMT
   Server: WSGIServer/0.2 CPython/3.6.7
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN

   {
       "description": "adasds",
       "name": "teste",
       "price": 3.14,
       "url": "http://127.0.0.1:8000/products/1/"
   }
