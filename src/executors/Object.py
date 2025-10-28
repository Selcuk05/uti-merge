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

        self.input_object_x = self.request.get_param("inputObjectX")
        self.input_object_y = self.request.get_param("inputObjectY")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def merge_objects(self, object_x, object_y):
        merged = {}

        for key, value in object_x.items():
            if key in object_y:
                merged[f"{key}_x"] = value
                merged[f"{key}_y"] = object_y[key]
            else:
                merged[key] = value

        for key, value in object_y.items():
            if key not in object_x:
                merged[key] = value

        return merged

    def run(self):
        self.merged = self.merge_objects(self.input_object_x, self.input_object_y)
        packageModel = build_response_object(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()
