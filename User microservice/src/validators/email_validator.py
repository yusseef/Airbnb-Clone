import re
from sqlalchemy import String

class Email(String):
    def __init__(self, regex=r'^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.regex = re.compile(regex)
    
    def process_bind_param(self, value, dialect):
        if value is not None:
            if not self.validate(value):
                raise ValueError('Invalid email address')
        return value

    def validate(self, value):
        return self.regex.match(str(value)) is not None

