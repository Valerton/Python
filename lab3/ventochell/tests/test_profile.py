import pytest
from ventochell.models import Profile


class TestsProfile:

    @pytest.mark.django_db
    def test_profile(self):
        profile = Profile.objects.create(name="test_1", surname="test_2", username="test_3", location="test_4", age="test_5", img="test_6", hobbies="test_7")
        assert profile.name == "test_1"
        assert profile.surname == "test_2"
        assert profile.username == "test_3"
        assert profile.location == 'test_4'
        assert profile.age == 'test_5'
        assert profile.img == 'test_6'
        assert profile.hobbies == 'test_7'