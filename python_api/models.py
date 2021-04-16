class HealthCheck:
    is_healthy: bool
    is_database_healthy: bool
    dependencies: dict

    def __init__(self, is_database_healthy: bool):
        self.dependencies = {
            "is_database_healthy": is_database_healthy,
        }

        self.is_healthy = is_database_healthy
