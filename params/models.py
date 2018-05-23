from django.db import models
from marketplace.basemodel import BaseModel


class Vendor(BaseModel):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title
