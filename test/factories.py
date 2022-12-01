# model factories that behave like django models
# lazy attributes

import factory
from apps.profiles.models import Profile
from django.db.models.signals import post_save
from faker import Factory as FakerFactory
from real_estate.settings.base import AUTH_USER_MODEL

# instance of faker
faker = FakerFactory.create()
# create profile factory
@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.factories.UserFactory")
    phone_number = factory.LazyAttribute(lambda x: faker.phone_number)
    about_me = factory.LazyAttribute(lambda x: faker.sentence(nb_words=5))
    license = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=6))