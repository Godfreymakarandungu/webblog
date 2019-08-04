from blog.views import index ,details
import pytest
from django.urls import reverse
from entries import views
from entries.views import EntryListView
from django.test import RequestFactory, TestCase
from entries.forms import EntryForm

@pytest.mark.django_db
def test_index(rf):
    request = rf.get('127.0.0.1:800/index')
    response = index(request)
    assert response.status_code == 200
class TestEntryListViews(TestCase):
    def test_EntryListView(self):
        req = RequestFactory().get('')
        respo = EntryListView.as_view()(req)
        assert respo.status_code == 200

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