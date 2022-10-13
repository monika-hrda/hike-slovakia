from django.db import models


class Contact(models.Model):
    """
    A contact model for users to contact the company
    """
    contact_email = models.EmailField(max_length=80, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(max_length=350, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.subject)
