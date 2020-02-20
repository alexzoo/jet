import requests
import pytest
from hamcrest import *


def get_request(url, **kwargs):
    return requests.get(url=url, params=kwargs)


class TestHH:
    hh_url = 'https://api.hh.ru/vacancies'

    # test data for parametrize
    text = ['test', 'qa']
    experience = ['noExperience', 'between1And3']
    vacancy_label = ['with_address', 'not_from_agency']
    vacancy_type = ['open', 'anonymous']
    vacancy_relation = ['favorited', 'got_response']

    @pytest.mark.parametrize('text', text)
    @pytest.mark.parametrize('experience', experience)
    @pytest.mark.parametrize('vacancy_label', vacancy_label)
    @pytest.mark.parametrize('vacancy_type', vacancy_type)
    @pytest.mark.parametrize('vacancy_relation', vacancy_relation)
    def test_hh_ru(self, text, experience, vacancy_label, vacancy_type, vacancy_relation):
        # When
        r = get_request(url=self.hh_url, text=text, experience=experience, vacancy_label=vacancy_label,
                        vacancy_type=vacancy_type, vacancy_relation=vacancy_relation)
        # That
        assert_that(r.json(), has_items(anything(text)))
        assert_that(r.json(), has_items(anything(experience)))
        assert_that(r.json(), has_items(anything(vacancy_label)))
        assert_that(r.json(), has_items(anything(vacancy_type)))
        assert_that(r.json(), has_items(anything(vacancy_relation)))
