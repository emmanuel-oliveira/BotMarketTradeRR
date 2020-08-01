from pathlib import Path


def getProjectFolder() -> str:
    """Retornando a pasta do projeto."""
    return str(Path(__file__).parent.parent)

