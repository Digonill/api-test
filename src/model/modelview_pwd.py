from flask_restx import fields, Model

ModelViewPasswd = Model('Model', {
    'text': fields.String(description='Password text to validate', default='')
    }
)
