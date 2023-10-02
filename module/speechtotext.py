import asyncio
from datetime import datetime, timedelta
import json
import sys
import openai
from typing import List, ClassVar, Mapping, Optional

from viam.components.sensor import Sensor
from viam.components.component_base import ValueTypes
from viam.proto.app.robot import ComponentConfig, RobotConfig
from viam.proto.common import ResourceName, Geometry
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
from viam.logging import getLogger

from google.protobuf.json_format import ParseDict


class MySTTSensor(Sensor):
    MODEL: ClassVar[Model] = Model(ModelFamily("jeremyrhyde", "nlp"), "chatgpt")
    SUPPORTED_VERSIONS = ["gpt-3.5-turbo"]

    LOGGER = getLogger(__name__)

    request_key = ""
    messages = []

    # Constructor for chat-gpt model
    @classmethod
    def new(cls, config: ComponentConfig,
            dependencies: Mapping[ResourceName, ResourceBase]):
        chatGPTInstance = cls(config.name)
        chatGPTInstance.reconfigure(config, dependencies)

        return chatGPTInstance

    # Validates JSON Configuration
    @classmethod
    def validate(cls, config: ComponentConfig):
        return

    @classmethod
    # Reconfigure module by resetting chat gpt connection
    def reconfigure(self, config: ComponentConfig,
                    dependencies: Mapping[ResourceName, ResourceBase]):
        return




async def main():
    # chatgpt = MyChatGPTInstance(name="test")

    # with open("example_config.json") as f:
    #     robotConfigJson = json.load(f)
    #     robotConfig = ParseDict(robotConfigJson, RobotConfig())
    #     chatGPTConfig = robotConfig.components[0]

    #     chatgpt.validate(chatGPTConfig)
    #     chatgpt.new(chatGPTConfig, {})

    # i = 0
    user_input = input("Press enter to start")
    while True:
        # test = {"request": user_input}
        # resp = await chatgpt.do_command(test)

        # print("-------------------------------------------------------------")
        # print("RESPONSE : " + resp["response"])
        # print("TIMESTAMP " + str(resp["timestamp"]))
        # print("-------------------------------------------------------------")

        # i = i + 1

        # user_input = input("Enter new do command to run (" + str(i) + "): ")

    sys.exit()

if __name__ == '__main__':
    asyncio.run(main())
