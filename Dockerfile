# Usa una imagen oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala uv (rápido para resolver deps con pyproject.toml)
RUN pip install uv

# Copia los archivos al contenedor
COPY . .

# Instala las dependencias
RUN uv pip install --system --no-cache-dir .[dev]

# Expone el puerto del backend
EXPOSE 8000

# Comando por defecto para ejecutar el backend
CMD ["run-dev"]
