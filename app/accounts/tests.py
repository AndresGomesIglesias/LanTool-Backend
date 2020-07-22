from django.test import TestCase

# # Create your tests here.
# from rest_framework.test import APITestCase

# from restful_example.models import Product, ProductSerializer


# class ProductTests(APITestCase):
#     def test_can_get_product_details(self):
#         product = Product.objects.create(name='Apple Watch', price=500, stock=3)
#         response = self.client.get(f'/products/{product.id}')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data, ProductSerializer(instance=product).data)

#     def test_can_delete_product(self):
#         product = Product.objects.create(name='Apple Watch', price=500, stock=3)
#         response = self.client.delete(f'/products/{product.id}/delete')
#         self.assertEqual(response.status_code, 204)
#         self.assertEqual(Product.objects.count(), 0)

#     def test_can_update_product(self):
#         product = Product.objects.create(name='Apple Watch', price=500, stock=3)
#         response = self.client.patch(f'/products/{product.id}/update', data={'name': 'Samsung Watch'})
#         product.refresh_from_db()
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(product.name, 'Samsung Watch')