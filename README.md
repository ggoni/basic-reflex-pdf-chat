# Protipo de Chatbot institucional

## Instrucciones

- Instalar ambiente virtual de Python 3.11 con venv (Por ejemplo: ```python3.11 -m venv .venv```)
- Instalar Reflex y otros requerimientos usando ```pip install -r requirements.txt```
- ```reflex init```
- ```reflex run```
- La aplicación estará corriendo , según indica el mensaje ```App running at: http://localhost:3000```

## Definiciones

- Respuestas se ciñen a contenido de los archivos cargados en la aplicación (temperatura = 0)
- No se ha definido explícitamente mecanismo para trabajar con el contexto
- En esta versión se trabajó con FAISS: dado un conjunto de vectores, podemos indexarlos mediante FAISS y, a partir de otro vector (el vector de consulta), buscar los vectores más similares dentro del índice. Detalles [acá](https://www.pinecone.io/learn/series/faiss/faiss-tutorial/)

## Fuentes

- Basado en documentación y ejemplos de [Reflex](https://reflex.dev/docs/getting-started/introduction/)
- Documentos en PDF son de dominio público, disponibilizados por la Universidad del Desarrollo (UDD)


## Roadmap (potencial)

- [ ] Agregar feedback de procesamiento al usario (_Spinning Circle_ u otro: Revisar componentes)
- [ ] Manejo de sesiones
- [ ] Administración de usuario y clave
- [ ] Diseñar reglas en lugar de respuestas ante preguntas con información crítica o sensible
- [ ] Persistir tuplas (pregunta, respuesta)


![chat](https://github.com/ggoni/basic-reflex-pdf-chat/assets/7189084/dda854fa-3e36-43c0-b3ee-17b4d216328d)



