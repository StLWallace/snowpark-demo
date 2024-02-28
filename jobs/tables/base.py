"""This is an idea to create an abstract base class that's a subclass of snowpark.DataFrame for all table models
This isn't implemented and it might not be worth doing

What:
    - Create a pattern for additional tables and views
    - Every subclass instance will have a create() method and other things that support it that define that dataframe transformations
    - The subclass will have all the same attrs and methods as a DataFrame

Why:
    - Enforces a blueprint for all future models
    - slightly abstracts some of the inheritance complexity

Why not:
    - Kind of an unusual pattern and I'm not sure how to best make it work
"""

from abc import ABC, abstractmethod, ABCMeta
from snowflake.snowpark import DataFrame, Session


class SnowflakeModel(DataFrame, metaclass=ABCMeta):
    """An abstract base class that defines the required methods for all table models"""

    def __init__(self, session: Session, **kwargs) -> None:
        """"""
        table = self.create(**kwargs)
        super().__init__(session=session, plan=table._plan)

    @abstractmethod
    def create(self) -> DataFrame:
        pass
