# Proyecto Urban Grocers 

- previamente a la creacion de archivos, es necesario tener instalado pytest y la libreria request
- se necesita el documento configuration, en el cual se encuentran los enlaces al servidor y la 
extension de las api necesarias para crear un nuevo usuario y para la creacion de un kit.
- en el archivo data, se colocan los datos que se requieren en el cuerpo de la solicitud, tales 
como el tipo de formato que posee el cuerpo, en este caso json, los datos de creacion de usuario 
que estan en user_body y el nombre del kit que se almacena en kit_body.

- creamos el archivo sender_stand_request en el cual se debe importar la data de configuration para 
acceder a los enlaces necesarios, importar la data y la libreria requests.
en este archivo se definen las funciones para crear un nuevo usuario, insertando los enlaces de la 
ruta completa, de donde tambien obtenemos el authtoken que sera necesario para crear el kit posteriormente.
definimos tambien la funcion para la creacion de un nuevo kit, en donde usaremos el token que se 
extrajo de la funcion anterior y la autorizacion requerida.

- para proceder a la creacion de las pruebas de la lista de comprobacion, necesitamos crear el archivo 
create_kit_name_kit_test
en el cual importamos el archivo sender stand request que contiene las funciones principales para crear
 el usuario y tambien el kit
- importamos tambien el archivo data
- definimos una funcion para poder acceder al kit_body y cambiar de nombre al kit creado, para esto se 
crea una copia de data.kit_body
- creamos la funcion positive assert que nos permite pasar las pruebas positivas, para hacerlo accedemos
 a la funcion anterior con get para cambiarle el nombre a name, guardamos en la solicitud response el 
archivo sender stand request con acceso a la funcion post new client kit user
- comprobamos con assert que el codigo de estado sea 201 y que se muestre en formato json
- creamos tambien la funcion negative assert 400 para las pruebas negativas, guardando en la variable 
response  la funcion para crear un kit de sender stand request y con assert comprobamos que el codigo 
sea 400 y que la respuesta en json contenga el codigo 400.

- creamos cada una de las pruebas con def test y en cada una de las pruebas positivas usamos get_kit_body 
para cambiarle el valor a name de acuerdo a lo que necesitamos. y llamamos a la funcion positive assert
de la misma forma para las pruebas negativas, para estas llamamos a negative assert 400 para acceder a esta funcion.
