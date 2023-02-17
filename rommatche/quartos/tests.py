from django.test import TestCase

# Create your tests here.


def bate_endpoint(db, client):
    client.post(api/quartos/list_quartos)
