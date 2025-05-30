# Dataset_Toyota/assets.py

import papermill as pm
from dagster import asset
from pathlib import Path

@asset
def ejecutar_notebook_toyota():
    notebooks_dir = Path(__file__).resolve().parent.parent / "notebooks"
    input_path = notebooks_dir / "ToyotaCorolla-Sosa-ZuritaV2.ipynb"
    output_path = notebooks_dir / "ToyotaCorolla-Sosa-ZuritaV2-output.ipynb"

    pm.execute_notebook(
        input_path=str(input_path),
        output_path=str(output_path),
        parameters={} 
    )

