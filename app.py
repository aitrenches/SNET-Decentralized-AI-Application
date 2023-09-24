from flask import Flask
from snet.sdk import SnetSDK
import config
import poetic_proto_pb2
import poetic_proto_pb2_grpc

app = Flask(__name__)

@app.route('/')
def invoke_service():
   snet_config = {"private_key": config.PRIVATE_KEY, "eth_rpc_endpoint": config.ETH_RPC_ENDPOINT}
   sdk = SnetSDK(config=snet_config)
   service_client = sdk.create_service_client(
      org_id=config.ORG_ID,
      service_id=config.SERVICE_ID,
      service_stub= poetic_proto_pb2_grpc.PoeticStub # replace service_stub
   )
   request = poetic_proto_pb2.String("Input text here") # replace input_method and arguments
   response = service_client.service.generate(request) # replace service_method
   message = f"service invoked successfully :: response :: {response}"
   
   return message


if __name__ == '__main__':
    app.run(debug=True)