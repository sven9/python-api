from marshmallow import Schema, fields


class LivenessSchema(Schema):
    liveness = fields.Boolean()
