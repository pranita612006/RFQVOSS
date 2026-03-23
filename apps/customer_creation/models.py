from django.db import models

class CustomerInfo(models.Model):
    customer_id = models.CharField(max_length=20, primary_key=True)  # <-- make this the PK
    name = models.CharField(max_length=100)
    search_name = models.CharField(max_length=100)

    class Meta:
        db_table = "tbl_customerinfo"   # exact table name in PostgreSQL
        managed = False  # <-- add this if the table already exists and you don’t want Django to try creating/migrating it

    def __str__(self):
        return self.customer_id
