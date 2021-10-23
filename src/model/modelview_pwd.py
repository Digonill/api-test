from flask_restx import fields, Model

ModelViewPasswd = Model('Model', {
    'text': fields.String(required=True, min_length=9, max_length=20, description='Password text to validate', default='')
    }
)
