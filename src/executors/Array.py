import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../"))

from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.Merge.src.utils.response import build_response_array
from components.Merge.src.models.PackageModel import PackageModel


class Array(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))

        self.input_array_x = self.request.get_param("inputArrayX")
        self.input_array_y = self.request.get_param("inputArrayY")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def merge_arrays(self, array_x, array_y):
        return array_x + array_y

    def run(self):
        self.merged = self.merge_arrays(self.input_array_x, self.input_array_y)
        packageModel = build_response_array(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()
