##testing views
# ################################
# from django.urls import resolve
# from django.test import TestCase
# from django.http import HttpRequest

# from blog.views import details
# from blog.views import index

# ###################################
# ##views 

# class HomePageTest(TestCase):

#     def test_root_url_resolves_to_details_view(self):
#         found = resolve('/')
#         self.assertEqual(found.func, index)


#     def test_details_returns_correct_html(self):
#         request = HttpRequest()  
#         response = details(request)  
#         html = response.content.decode('utf8')  
#         self.assertTrue(html.startswith('<html>'))  
#         self.assertIn('<title>Makara Test Blog  </title>', html)  
#         self.assertTrue(html.endswith('</html>'))


# class  DetailsPageTest(TestCase):

#     def test_root_url_resolves_to_details_view(self):
#         found = resolve('/Details')
#         self.assertEqual(found.func, details)


#     def test_details_returns_correct_html(self):
#         request = HttpRequest()  
#         response = details(request)  
#         html = response.content.decode('utf8')  
#         self.assertTrue(html.startswith('<html>'))  
#         self.assertIn('<title>Makara Test Blog  </title>', html)  
#         self.assertTrue(html.endswith('</html>'))        
# #################################################################        
# from django.urls import reverse, resolve


# class TestUrls:

#     def test_details_url(self):
#         path = reverse('details', kwargs={'id': 1})
#         assert resolve(path).views.details == 'details/1'
#     def test_details_url(self):
#         path = reverse('')
#         assert resolve(path).views.details == 'index'   
         
# from django.test import TestCase
# from django.urls import reverse, resolve

# class TestUrls(TestCase):

#     def test_details_url(self):
#         path = reverse('details', kwargs={'id': 1})
#         self.assertEqual('details', resolve(path).views.details)

#     def test_unit_index_url(self):
#         path = reverse('',)
#         self.assertEqual('index', resolve(path).views.index)
#     def test_unit_index_url(self):
#         path = reverse('index',)
#         self.assertEqual('index', resolve(path).views.index)            