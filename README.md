# TicketFast - Pruebas de Integración, Sistema y E2E

## Instalación rápida

1. Crear un entorno virtual e instalar dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --no-cache-dir -r requirements.txt
```

2. Instalar los navegadores de Playwright:

```powershell
python -m playwright install chromium
```

## Ejecutar la API localmente

```powershell
uvicorn src.reservas.api:app --host 0.0.0.0 --port 8001
```

## Ejecutar contenedores de prueba

```powershell
docker compose -f docker-compose.test.yml up --build
```

## Ejecutar pruebas de integración

```powershell
pytest tests/integration/test_api_integracion.py
```

## Ejecutar pruebas de sistema

Asegúrate que la API esté disponible en `http://localhost:8001`.

```powershell
pytest tests/system/test_sistema_e2e.py
```

## Ejecutar prueba E2E de frontend

Asegúrate que el frontend esté disponible en `http://localhost:4200`.

```powershell
pytest tests/e2e/test_frontend_reservas_e2e.py
```

## Notas

- `docker-compose.test.yml` usa PostgreSQL en memoria RAM con `tmpfs`, por lo que los datos se descartan al detener los contenedores.
- Si la API se ejecuta dentro de contenedores, el servicio de pruebas debe estar accesible en `localhost:8001`.
