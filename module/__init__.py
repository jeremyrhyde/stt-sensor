from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration
from .speechtotext import MySTTSensor


Registry.register_resource_creator(Sensor.SUBTYPE,
                                   MySTTSensor.MODEL,
                                   ResourceCreatorRegistration(MySTTSensor.new))
