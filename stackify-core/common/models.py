from schematics.models import Model


class BaseModel(Model):
    @classmethod
    def new(cls, **kwargs):
        obj = cls()
        for attr, value in kwargs.items():
            obj[attr] = value
        return obj
