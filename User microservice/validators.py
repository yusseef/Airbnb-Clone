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

class Password(String):
    def __init__(self, regex = None, *args, **kwargs):
        regex = regex or r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W])[A-Za-z\d\W]{8,}$'
        super().__init__(*args, **kwargs)
        self.regex = re.compile(regex)

    def process_bind_param(self, value, dialect):
        if value is not None:
            if not self.validate(value):
                raise ValueError(
                    'Password must contain at least one uppercase letter, '
                    'one lowercase letter, one number and one special character, and be at least 8 characters long.')
        return value
    
    def validate(self, value):
        return self.regex.match(str(value)) is not None