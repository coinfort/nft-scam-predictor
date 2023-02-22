import dotenv
from sol.rpc import Endpoint, SolanaRpcClient

dotenv.load_dotenv()

rpc = SolanaRpcClient.from_endpoint(Endpoint.ChainStack)
times = []

metadata = rpc.nft_metadata("5pizxsxtBfABUeSd2WKgDCLPWYd9tMt4jtqyuUqiCFpg")
print(metadata)
