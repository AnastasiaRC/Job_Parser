from abc import ABC, abstractmethod


class ApiRequests(ABC):
    @abstractmethod
    def get_request(self, keyword):
        pass

