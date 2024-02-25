# Usa la imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 para la aplicación Flask
EXPOSE 5000

# Define el comando por defecto para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "./frutas.py"]
