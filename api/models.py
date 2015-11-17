from django.db import models
import uuid

class Image(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=1024)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return str('[%s] %s'%(self.uuid, self.url))
    def __unicode__(self):
        return str('[%s] %s'%(self.uuid, self.url))

    class Meta:
        ordering = ('created', )
        index_together = [
            ('uuid', 'url'),
        ]

class Tag(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ForeignKey(Image)
    text = models.CharField(max_length=256)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return str('[%s] %s'%(self.uuid, self.text))
    def __unicode__(self):
        return str('[%s] %s'%(self.uuid, self.text))

    class Meta:
        ordering = ('created', )
        index_together = [
            ('text', 'uuid', 'image'),
        ]

