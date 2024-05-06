from django.db import models
choices=()

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('housing', 'Housing'),
        ('transportation', 'Transportation'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('clothing', 'Clothing'),
        ('other', 'Other'),]

    name=models.CharField(max_length=50)
    amount=models.IntegerField()
    Cateogry=models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    date=models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.name