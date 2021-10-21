from flask_restplus import fields
from server.server import server

Password = server.api.models('password', {
    'text': fields.String(required=True, min_length=9, max_length=20, description='Password text to validate')
})
