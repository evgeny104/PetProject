import pytest
import allure
from main import Region
from src.config.url import BASE_URL

@pytest.fixture
def region_response(request):
    q, country_code, page_size, page = request.param

    with allure.step(f"Send GET request with params: q={q}, country_code={country_code}, page_size={page_size},"
                     f" page={page}"):
        region = Region(
            url=BASE_URL,
            q=q,
            country_code=country_code,
            page_size=page_size,
            page=page
        )
        status_code, data = region.get_data()

    with allure.step("Attach API response to the report"):
        allure.attach(
            str(data),
            name="Response body",
            attachment_type=allure.attachment_type.TEXT
        )

    return status_code, data