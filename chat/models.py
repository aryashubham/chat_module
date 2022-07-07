from pyexpat import model
from venv import create
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
    updated_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class ConversationThread(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    recipients = models.ManyToManyField(User, blank=True)
    chat_started = models.BooleanField(default=False)
    last_seen_message = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        db_table = 'conversation_thread'


class ConversationMessage(BaseModel):
    conversation_thread = models.ForeignKey(ConversationThread, on_delete=models.CASCADE, null=True, blank=True)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sender_id')
    reciver_id = models.ManyToManyField(User, blank=True)
    message = models.TextField()
    seen_status = models.BooleanField(default=False)
    file = models.FileField(upload_to='chat_data/', blank= True)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        db_table = 'conversation'