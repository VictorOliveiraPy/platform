import abc


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get_user(self):
        pass
