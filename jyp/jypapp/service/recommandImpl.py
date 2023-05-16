from .recommand import Recommand


class RecommandImpl(Recommand):
    def recommand(self, keyword: list, job_posts: dict) -> list:
        return [1]

    def train_model(self) -> None:
        return None