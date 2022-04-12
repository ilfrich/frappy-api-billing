from abc import ABC, abstractmethod
from datetime import datetime
from typing import Union, List


class Usage:
    def __init__(self):
        self.client_id: Union[str, int] = None
        self.timestamp: int = 0  # in seconds
        self.credits: Union[float, int] = 0

    def to_json(self):
        result = {
            "timestamp": self.timestamp,
            "credits": self.credits,
        }
        if self.client_id is not None:
            result["clientId"] = self.client_id
        return result

    @staticmethod
    def from_json(json: dict):
        result = Usage()
        if "clientId" in json:
            result.client_id = json["clientId"]
        if "timestamp" in json:
            result.timestamp = json["timestamp"]
        if "credits" in json:
            result.credits = json["credits"]
        return result


class AbstractUsageStore(ABC):

    @abstractmethod
    def track_usage(self, client_id: Union[str, int], credits_used: Union[int, float]):
        pass

    @abstractmethod
    def get_total_usage(self, client_id, start_datetime: datetime, end_datetime: datetime) -> Union[float, int]:
        pass

    @abstractmethod
    def get_daily_usage(self, client_id, start_datetime: datetime, end_datetime: datetime) -> List[Usage]:
        pass
