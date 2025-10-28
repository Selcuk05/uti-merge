from sdks.novavision.src.helper.package import PackageHelper
from components.Merge.src.models.PackageModel import (
    PackageModel,
    OutputArray,
    ArrayOutputs,
    ArrayResponse,
    Array,
    OutputObject,
    ObjectOutputs,
    ObjectResponse,
    Object,
    ConfigExecutor,
    PackageConfigs,
)


def build_response_array(context):
    outputArray = OutputArray(value=context.merged)
    Outputs = ArrayOutputs(outputArray=outputArray)
    packageResponse = ArrayResponse(outputs=Outputs)
    packageExecutor = Array(value=packageResponse)
    executor = ConfigExecutor(value=packageExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

def build_response_object(context):
    outputObject = OutputObject(value=context.merged)
    Outputs = ObjectOutputs(outputObject=outputObject)
    packageResponse = ObjectResponse(outputs=Outputs)
    packageExecutor = Object(value=packageResponse)
    executor = ConfigExecutor(value=packageExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
