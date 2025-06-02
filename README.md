# dataset_toyota
Integrantes:
- Zurita, Matias
- Sosa, Santiago

Para iniciar proyecto

Primero crear un entorno conda

```bash
conda create -n "env_name" python=3.11
```

```bash
conda activate "env_name"
```

```bash
pip install -e ".[dev]"
```

```bash
pip install poetry
```

```bash
poetry install
```

Then, start the Dagster UI web server:

```bash
dagster dev
```
Then, start the Mlflow UI web server:

```bash
mlflow ui
```
En el buscador ingresar a http://localhost:3000
