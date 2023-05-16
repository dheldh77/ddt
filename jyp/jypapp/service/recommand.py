from abc import abstractmethod, ABCMeta

class Recommand(metaclass=ABCMeta):
    @abstractmethod
    def recommand(self, keyword: list, job_posts: dict) -> list:
        """
        Args:
            keyword (list): list of string (ex : [SW Developer, JAVA, C++])
            job_posts (dict): dictionary type of job posting. key is post_id and value is list (ex: {1: ["#SW Developer#JAVA": "1.conetent.."]})

        Returns:
            list: list of recommand post_id (ex: [1, 2, 3, 5])
        """
        pass

    @abstractmethod
    def train_model(self) -> None:
        """train method to learn on server pc
        """
        pass 
