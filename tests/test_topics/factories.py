import factory

from apps.topics.models import Topic, TopicMessage
from tests.test_users.factories import UserFactory


class TopicFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('word')
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Topic


class TopicMessageFactory(factory.django.DjangoModelFactory):
    topic = factory.SubFactory(TopicFactory)
    user = factory.SubFactory(UserFactory)
    content = factory.Faker('text', max_nb_chars=100)

    class Meta:
        model = TopicMessage
