from marshmallow import Schema, fields


class LivenessSchema(Schema):
    liveness = fields.Boolean()


class HealthCheckDependenciesSchema(Schema):
    is_database_healthy = fields.Boolean()


class HealthCheckSchema(Schema):
    is_healthy = fields.Boolean()
    dependencies = fields.Nested(HealthCheckDependenciesSchema)
