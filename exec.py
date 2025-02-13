from src.middlewares.profile import profiler_manager
from src.models.base.application import aplicacion
from src.main import iniciar


def main():
    """Inicializar el aplicativo."""
    profiler_manager.enabled = True

    aplicacion.pagina_sample_network = "A"

    iniciar()


if __name__ == "__main__":
    main()
