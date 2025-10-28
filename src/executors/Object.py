import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../"))

from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.Merge.src.utils.response import build_response_object
from components.Merge.src.models.PackageModel import PackageModel


class Object(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def run(self):
        packageModel = build_response_object(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()
