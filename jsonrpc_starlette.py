from ajsonrpc.backend.common import CommonBackend


class JSONRPCStarlette(CommonBackend):
    async def handle(self, request_data: bytes):
        return await self.manager.get_payload_for_payload(request_data)