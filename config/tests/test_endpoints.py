import json

import pytest

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:

    endpoint = "/category/"

    def test_category_get(self, category_factory, api_client):
        category_factory.create_batch(4, is_active=True)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestProductEndpoints:

    endpoint = "/product/"

    def test_return_single_product_by_slug(self, product_factory, api_client):
        obj = product_factory(slug="test-slug")
        response = api_client().get(f"{self.endpoint}{obj.slug}/")
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_return_products_by_category_slug(
        self, category_factory, product_factory, api_client
    ):
        obj = category_factory(slug="test-slug")
        product_factory(category=obj)
        response = api_client().get(f"{self.endpoint}category/{obj.slug}/")
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1
