from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True, default='')
    user_name = models.CharField(max_length=150, default="")
    user_email = models.EmailField(default="")

    def __str__(self):
        return f"UserID: {self.user_id} | Name: {self.user_name}"  # Corrigido para exibir o ID do usuário

class Tasks(models.Model):
    TASK_STATES = [
        ('A', 'A fazer'),
        ('P', 'Pronto')
    ]

    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=80, default="")
    task_desc = models.TextField(max_length=255, default="")
    task_state = models.CharField(max_length=1, choices=TASK_STATES, default='A')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=False, null=False)  # Corrigido para usar ForeignKey

    def __str__(self):
        return f"Task ID: {self.task_id} | Name: {self.task_name} | State: {self.get_task_state_display()}"
