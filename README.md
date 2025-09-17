# Pasos

1. clonar repositorio con:
    ```
    git clone https://github.com/nowchri/arquitectura_software.git
    ```

2. Cambiarse a la carpeta del proyecto que acabas de clonar, crear entorno virtual con:
    ```
    python -m venv venv
    ```

3. Activar entorno virtual con:
    ```
    .\venv\Scripts\activate
    ```

4. Instala las dependencias del `requirements.txt` con el entorno virtual **ACTIVADO**:
    ```
    pip install -r requirements.txt
    ```

5. Ejecuta el siguiente comando para correr la aplicación:
    ```
    uvicorn app.main:app --reload
    ```
    > **Nota:** Debes estar en la carpeta raíz del proyecto completo para que funcione, no en la carpeta `/app`.
    ---
    **Otra nota:** En el archivo `database.py` en la carpeta `/app` fíjate que esta línea:
    ```
    DATABASE_URL = "postgresql://postgres:1234@localhost:5432/ACADEMIA_ARTE"
    ```
    Tenga el nombre de la base de datos correctamente, ya que si en local la llamaste por ejemplo `db_academia_arte` tendrás que cambiar eso que dice `ACADEMIA_ARTE` para que funcione.
