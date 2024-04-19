# Gateway

Repositorio del API Gateway implementado en la Aplicación *Match!* desarrollada para Taller de Programación III.

## Configuración

Se debe agregar el archivo *firebasekey.json* en la raiz del repositorio. La misma contiene la clave de aplicación de servicio generada por Firebase. La forma del json es la siguiente.

```json
{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "",
  "universe_domain": "googleapis.com"
}
```

## Pruebas con Swagger
Para realizar pruebas con Swagger, es necesario autenticarse con el token de acceso. El mismo se obtiene desde la aplicación cliente, o realizando el siguiente POST, configurando los parámetros necesarios:

```bash
curl -X POST -d '{"email":"${email}","password":"${password}","returnSecureToken":true}' -H "Content-Type: application/json" "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=${apikey}"
```

Por ejemplo, para el usuario de prueba string@email.com, con contraseña string, se puede obtener el siguiente token de acceso.

```bash
curl -X POST -d '{"email":"string@email.com","password":"string","returnSecureToken":true}' -H "Content-Type: application/json" "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyCb-baXdesmrzmTOvo4Xh6gL2c8SKxsfRo"
```
