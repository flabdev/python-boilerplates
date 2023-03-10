import uvicorn

from fission_project_template.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "fission_project_template.web.application:get_app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.value.lower(),
        factory=True,
    )


if __name__ == "__main__":
    main()
