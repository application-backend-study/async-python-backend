from typing import Dict
import uuid

class AddressBookServiceManager:

    def __init__(self, config: Dict) -> None:
        self.address: Dict[str, Dict] = {}

    def start(self):
        self.address = {}

    def stop(self):
        pass

    async def createAddress(self, value: Dict) -> str:
        key = uuid.uuid4().hex
        self.address[key] = value

        return key

    async def getAddress(self, key: str) -> Dict:
        return self.address[key]

    async def updateAddress(self, key: str, value: Dict) -> None:
        self.address[key] = value

    async def deleteAddress(self, key: str) -> None:
        del self.address[key]

    async def getAllAddress(self) -> Dict[str, Dict]:
        return self.address