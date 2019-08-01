from blog.views import index ,details
import pytest
@pytest.mark.django_db
def test_index(rf):
    request = rf.get('127.0.0.1:800/index')
    response = index(request)
    assert response.status_code == 200
@pytest.mark.django_db    
def test_index(rf):
    request = rf.get('127.0.0.1:800')
    response = index(request)
    assert response.status_code == 200
@pytest.mark.django_db    
def test_index(rf):
    request = rf.get('127.0.0.1:800/')
    response = index(request)
    assert response.status_code == 200
@pytest.mark.django_db    
def test_index(rf):
    request = rf.get('127.0.0.1:800/blog/details/1/')
    response = index(request)
    assert response.status_code == 200    