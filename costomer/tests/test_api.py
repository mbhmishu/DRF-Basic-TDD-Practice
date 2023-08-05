# from django.urls import reverse,resolve
# from django.test import SimpleTestCase
# from costomer.views import CustomerView,CustomerDetail
# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework import status



# class ApiTestCase(SimpleTestCase):
#     def test_get_customer_is_resolved(self):
#      url = reverse('customer')
#      print(url)
#      res = resolve(url)
#      print(res)
#      print(res.func)
#      print(res.func.view_class)


#      self.assertEquals(resolve(url).func.view_class,CustomerView)


# class CutometerApiTestCase(APITestCase):
#     costomer_url = reverse('customer')

#     def setUp(self):
#       self.user = User.objects.create(username='abc',password='strong-Password234')
#       self.token = Token.objects.create(user=self.user)
#       self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
#     def tearDown(self):
#        pass


#     def test_get_customer_authentication(self):
#        response = self.client.get(self.costomer_url)
#        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
#     def test_get_customer_unauthentication(self):
#        self.client.force_authenticate(user=None,token=None)
#        response = self.client.get(self.costomer_url)
#        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
#     def test_post_customer(self):
#        data={
        
#         "title": "Iqbql",
#         "first_name": "Habibur",
#         "last_name": "baul",
#         "gender": "Maile",
#         "status": "draft",
        
#     }
#        response=self.client.post(self.costomer_url,data, format='json')
#        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
#        self.assertEqual(response.data['title'] , 'Iqbql')

# class CustomerDetailsTestCase(APITestCase):
#    customer_url = reverse('customer')
#    customerd_url = reverse('customer-detail', args=[1])

#    def setUp(self):
#       self.user= User.objects.create(username='fhjt',password='hihello-you65fj')
#       self.token= Token.objects.create(user=self.user)
#       self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

#       data={
        
#         "title": "Iqbqli",
#         "first_name": "Habibur",
#         "last_name": "baul",
#         "gender": "Maile",
#         "status": "draft",
        
#     }
#       response = self.client.post(self.customer_url, data,format='json')

#    def tearDown(self):
#       pass

#    def test_get_customerdetaile_is_authenticated(self):
#       response = self.client.get(self.customerd_url)
#       self.assertEqual(response.status_code,status.HTTP_200_OK)
#       self.assertEqual(response.data['first_name'],'Habibur')

#    def test_get_customerdetaile_unauthenticated(self):
#       self.client.force_authenticate(user=None,token=None)
#       response = self.client.get(self.customerd_url)
#       self.assertEqual(response.status_code,401)

#       def test_customer_delete(self):
#          response = self.client.delete(self.customerd_url)
#          self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
      


        

from django.test import SimpleTestCase
from django.urls import reverse,resolve
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from costomer.views import CustomerView,CustomerDetail
from rest_framework.authtoken.models import Token

class CustomerResolverTestCase(SimpleTestCase):
    def test_resolv_api(self):
        url= reverse('customer')
        self.url = reverse('customer-detail',args=[1])
        self.assertEqual(resolve(url).func.view_class,CustomerView)
        self.assertEqual(resolve(self.url).func.view_class,CustomerDetail)


class CustomerApiTest(APITestCase):
    customer_url = reverse('customer') 

    def setUp(self):
        self.user= User.objects.create(username='cosro',password='passeihgruier')
        self.token= Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    def test_is_authenticate(self):
        res=self.client.get(self.customer_url)
        self.assertEquals(res.status_code,200)

    def test_is_authenticate(self):
        self.client.force_authenticate(user=None)
        res=self.client.get(self.customer_url)
        self.assertEquals(res.status_code,401)

    def test_post(self):
               data={
        
        "title": "Iqbql",
        "first_name": "Habibur",
        "last_name": "baul",
        "gender": "Maile",
        "status": "draft",
        
    }
               res=self.client.post(self.customer_url, data=data,format="json")
               self.assertEquals(res.status_code,201)
               self.assertEqual(res.data["title"],'Iqbql')


         
   
  
class CustomerDetailTestCase(APITestCase):
     customer_url = reverse('customer')
     customer_detail_url=reverse('customer-detail', args=[1])

     def setUp(self):
          self.user= User.objects.create(username='chashi', password='himujdfjkdkj')
          self.token= Token.objects.create(user=self.user)
          self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


          data={
        
            "title": "Iqbqli",
            "first_name": "Habibur",
            "last_name": "baul",
            "gender": "Maile",
            "status": "draft",
        
          }
          responce= self.client.post(self.customer_url,data,format='json')

     def test_get(self):
          responce= self.client.get(self.customer_url)
          self.assertEquals(responce.status_code,status.HTTP_200_OK)
          print(responce.data[0])
          print(responce.data)
        #   self.assertEquals(responce.data[1]["title"],"Iqbqli")
          
          







    