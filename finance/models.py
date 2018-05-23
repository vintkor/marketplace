from django.db import models
from marketplace.basemodel import BaseModel


class Currency(BaseModel):
    title = models.CharField(max_length=150)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title
