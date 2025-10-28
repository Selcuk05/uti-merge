from typing import Optional, Union, Literal
from sdks.novavision.src.base.model import (
    Package,
    Inputs,
    Configs,
    Outputs,
    Response,
    Request,
    Output,
    Input,
    Config,
)


class InputArrayX(Input):
    name: Literal["inputArrayX"] = "inputArrayX"
    value: list
    type: str = "object"

    class Config:
        title = "Array 1"


class InputArrayY(Input):
    name: Literal["inputArrayY"] = "inputArrayY"
    value: list
    type: str = "object"

    class Config:
        title = "Array 2"


class InputObjectX(Input):
    name: Literal["inputObjectX"] = "inputObjectX"
    value: dict
    type: str = "object"

    class Config:
        title = "Object 1"


class InputObjectY(Input):
    name: Literal["inputObjectY"] = "inputObjectY"
    value: dict
    type: str = "object"

    class Config:
        title = "Object 2"


class OutputArray(Output):
    name: Literal["outputArray"] = "outputArray"
    value: list
    type: str = "object"

    class Config:
        title = "Array"


class OutputObject(Output):
    name: Literal["outputObject"] = "outputObject"
    value: dict
    type: str = "object"

    class Config:
        title = "Object"


class ArrayInputs(Inputs):
    inputArrayX: InputArrayX
    inputArrayY: InputArrayY


class ArrayOutputs(Outputs):
    outputArray: OutputArray


class ArrayRequest(Request):
    inputs: Optional[ArrayInputs]

    class Config:
        json_schema_extra = {"target": "configs"}


class ArrayResponse(Response):
    outputs: ArrayOutputs


class Array(Config):
    name: Literal["Array"] = "Array"
    value: Union[ArrayRequest, ArrayResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Array"
        json_schema_extra = {"target": {"value": 0}}


class ObjectInputs(Inputs):
    inputObjectX: InputObjectX
    inputObjectY: InputObjectY


class ObjectOutputs(Outputs):
    outputObject: OutputObject


class ObjectRequest(Request):
    inputs: Optional[ObjectInputs]

    class Config:
        json_schema_extra = {"target": "configs"}


class ObjectResponse(Response):
    outputs: ObjectOutputs


class Object(Config):
    name: Literal["Object"] = "Object"
    value: Union[ObjectRequest, ObjectResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Object"
        json_schema_extra = {"target": {"value": 0}}


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[Array, Object]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {"target": "value"}


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["Merge"] = "Merge"
