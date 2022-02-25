import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def post(self):
        pass

    @abc.abstractmethod
    def get_by_id(self, id_):
        pass

    @abc.abstractmethod
    def get(self):
        pass
