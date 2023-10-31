# API REST

RESTful: Arquitectura de software que se utiliza en el desarrollo de los servicios web.
REST: Representational State Transfer::Transferencia de representación de estado.

## Primera parte: Definición y aclaración del nombre REST

El nombre "representational State Transfer" inicialmente no es muy diciente, sin embargo, una vez comprendido el concepto de estado en los sistemas, (el nombre) es clave para entender la arquitectura, por esto, a continuación la definición de estado en sistemas: 

### Sistemas con estado y sin estado

Un estado en un sitema se refiere a una condición de existencia bajo alguna circunstancia. 
Asimismo, un estado depende del tiempo y de la forma en la que se hace  la interección con el sistema.

#### Sistema sin estado

Una operación no hace referencia a otra operación. Cada una se lleva a caboo desde cero como si fuera la primera vez. Por ejemplo, si hago una búsqueda en duckduckgo como un usario no registrado, cada búsqueda será independiente de alguna otra que haya hecho y si yo busco: imágenes de fonde de bikini y después busco imágenes de la Sra Puff, cada búsqueda será independiente de la anterior, esto es más fácil de demostrar si realizo la misma búsqueda muchas veces, pues el hecho de que vuelva a hacer la búsqueda no va a cambiar los datos que ya antes encontré. (Hacer un duckduckgo)

#### Sistema con estado

Una operación hace referencia a otra operación. Una operación actual puede verse afectada por otra que ocurrió previamente. Por ejemplo, un retiro en el banco, afecta el estado del sistema porque disminuye mi cantidad de dinero actual y la próxima vez que utilice el sistema, evidenciaré que tengo menos dinero. (¿Hacer ejemplo?)

___

Volviendo al nombre, representational State Transfer o TRANSFERENCIA de REPRESENTACIÓN de ESTADO.

Si entendemos transferencia como cambio (de un sistema a otro), y representación de estado como una idea abstracta que se refiere al estado de un sistema con otro, entonces, podríamos decir en palabras simples que:

Una arquitectura REST, tiene como principio fundamental darle la carga de la prueba del estado entre los sistemas al cliente porque TRANSFIERE la REPRESENTACIÓN DEL ESTADO.

Por ejemplo:

Si quiero que un servicio REST me recuerde, debo indicarle quien soy en cada llamada. Lo cual podría hacer con un usuario y una contraseña, o un token. (EJEMPLO CON JAVA SPRING)

___

Con el nombre entendido, vamos por la segunda parte


## Segunda Parte: Principios de la arquitectura RESTful

La arquitectura RESTful es una estructura para hacer código que se basa en principios de diseño que permiten crear aplicaciones web escalables (precisamente por no tener estado), fáciles de entender (), y que utilizan el protocolo HTTP (utiliza pocos verbos simples para operar), sus principios son los siguientes:

- Protocolo HTTP: Utiliza las operaciones estandar del protocolo HTTP, como get, post, put, delete, etc.

- Recursos: A diferencia de SOAP (Simple Object Access Protocol) que utiliza el protocolo RPC (Remote Procedure Call::Llamada a método remoto) y por lo tanto se fundamenta en los servicios, RESTful hace uso de recursos a los que se puede acceder a través de URLs únicas

- Operaciones bien definidas: Al utilizar HTTP las operaciones CRUD están mapeadas y son fáciles de usar.

- Stateless: En cada solicitud el deber de entregar la información completa al servidor es el cliente. El servidor no mantiene un estado de la sesión del cliente.

- Formatos de datos estandar: Como Json, XML, o texto plano.