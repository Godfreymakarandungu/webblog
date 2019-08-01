import pytest
from django.core.management import call_command
# from django.contrib.auth import get_user_model
# User = get_user_model()

def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200
    
def test_new_user(django_user_model):
    django_user_model.objects.create(username = "makara", password = "kiugokiega") 
     
# @pytest.mark.django_db
# def test_my_user():
#     me = User.objects.get(username='godfrey')
#     assert me.is_superuser
    
# # pytestmark = pytest.mark.django_db

# # @pytest.mark.django_db
# # class TestUsers:
# #     pytestmark = pytest.mark.django_db
# #     def test_my_user(self):
# #         me = User.objects.get(username='godfrey')
# #         assert me.is_superuser    