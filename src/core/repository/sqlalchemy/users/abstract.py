import abc


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get_user(self):
        pass


class AbstractRepositoryUser(abc.ABC):
    @abc.abstractmethod
    def post(self):
        pass
