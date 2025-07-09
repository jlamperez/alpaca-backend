# alpaca-backend

## 1. Crea y activa un entorno virtual

```bash
uv venv
source .venv/bin/activate
```

## 2. Instala tu propio paquete + dependencias declaradas

```bash
uv pip install -e ".[dev]"        # el ".": instala en editable, [dev] incluye extras
```

## 3. Ejecuta el servidor con el script definido

```bash
run-dev
```

## 4. Instala dependencias con uv

- *dentro del venv* -> `uv pip install httpx`
- *deja que uv resuelva y agregue la versión*

```bash
uv pip freeze --exclude-editable > /tmp/lock.txt   # opcional: inspeccionar lock
```

## 5. Swagger UI:

```bash
http://localhost:8000/docs
```

## 6. ReDoc (alternativa más elegante):

```bash
http://localhost:8000/redoc
```

## 7. OpenApi

```bash
http://localhost:8000/openapi.json
```

## 8. Run using Docker

```bash
docker-compose up --build
```