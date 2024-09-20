# [1.4.0](https://github.com/ernane/auction-house/compare/v1.3.0...v1.4.0) (2024-09-20)


### Features

* Add FastAPI, Uvicorn, and HTTPX dependencies ([177555b](https://github.com/ernane/auction-house/commit/177555bd4de2b9c27217a30eba6e4e28b4b58eb7))
* Add integration tests for submitting bids in auctions ([743d217](https://github.com/ernane/auction-house/commit/743d217c2460cf61702d6e8652d3130ea5577218))
* Add REST API router for submitting bids in auctions ([99cab54](https://github.com/ernane/auction-house/commit/99cab54c4e19f43e2f5e7dec6797630da7b5aba2))
* Add REST API router for submitting bids in auctions ([2332ce9](https://github.com/ernane/auction-house/commit/2332ce9c8501c80f977e89e5611a7730989f1143))
* Add schema router for REST API ([b855fbd](https://github.com/ernane/auction-house/commit/b855fbda71dfb82dbb5b40dc1287af16e3ed6c97))
* Adicionar roteador REST para enviar lances em leilões ([ef7d2e0](https://github.com/ernane/auction-house/commit/ef7d2e0fa26cd02106b0e774b8e189a8049b5382))

# [1.3.0](https://github.com/ernane/auction-house/compare/v1.2.0...v1.3.0) (2024-09-18)


### Features

* add engine dependency 3.5.1 ([97cfc1c](https://github.com/ernane/auction-house/commit/97cfc1c1d014f4fdeb49264b4c60d919ccdd07ed))
* Add MongoDB auction repository and exceptions ([600572c](https://github.com/ernane/auction-house/commit/600572ce86917082cd2856d36240e890dfd07744))
* Add MongoDB service for testing ([dee4d35](https://github.com/ernane/auction-house/commit/dee4d359c258136e3c1fcf42ac043332ef2ae2a7))
* Add test fixtures for MongoDB auction repository ([998d5b5](https://github.com/ernane/auction-house/commit/998d5b5ee5771016a9799d174c1425c7c39ff93f))

# [1.2.0](https://github.com/ernane/auction-house/compare/v1.1.0...v1.2.0) (2024-09-17)


### Features

* Add asyncio_default_fixture_loop_scope configuration option ([c8ec11b](https://github.com/ernane/auction-house/commit/c8ec11bff6554e3aa5675a3402ea7f53e3e59384))
* Add AuctionNotActiveError exception ([2e58323](https://github.com/ernane/auction-house/commit/2e5832374e6b08fe586ed7f4cdb617734f07b193))
* Add AuctionNotFoundError exception ([fc41957](https://github.com/ernane/auction-house/commit/fc41957a653cdce333ce84096a20747b6b6e9d4d))
* Add create_auction function to test utils ([b130db7](https://github.com/ernane/auction-house/commit/b130db7f75df4d6669ad182dacec224cba11c544))
* Add create_bid function to test utils ([8f78ae0](https://github.com/ernane/auction-house/commit/8f78ae02c491a3ca4908546f05e15769dd82ec3c))
* Add exception for inactive auction in submit bid use case ([1cae4b4](https://github.com/ernane/auction-house/commit/1cae4b42d3a35f4ab5a71ae204b8384abb68ce57))
* Add exception for low bid in submit bid use case ([790fc57](https://github.com/ernane/auction-house/commit/790fc57aa7d9174086dc2904b0eebd1831a7df5b))
* Add exception for low bid in submit bid use case ([916a802](https://github.com/ernane/auction-house/commit/916a80253c4417e9cb48659d6f1fab1e5a7a938f))
* Add in-memory auction repository ([c301f88](https://github.com/ernane/auction-house/commit/c301f884a35e36629953b3dfd9febc8562ca2bf5))
* Add in-memory auction repository ([ef46638](https://github.com/ernane/auction-house/commit/ef46638ad25766bc1aec6807569f910b83359dae))
* Add SubmitBidUseCase to handle bid submission ([0916897](https://github.com/ernane/auction-house/commit/09168977cac396a668b30d369998551b5c14ca4d))
* Add test for successfully adding a bid ([1e68c46](https://github.com/ernane/auction-house/commit/1e68c463a0d17de3b68cc40500643cbfe92aa94b))
* Add unit test for handling auction not found error in submit bid use case ([5e1ecc2](https://github.com/ernane/auction-house/commit/5e1ecc2b2ff8dd2ea09325383dcc0c8508633ae5))

# [1.1.0](https://github.com/ernane/auction-house/compare/v1.0.0...v1.1.0) (2024-09-15)


### Features

* Add Bid entity with dataclass implementation ([3bf5be1](https://github.com/ernane/auction-house/commit/3bf5be1ebbcf80389dd8e0ab858d35a2bb2ff3f7))
* Add Price value object with dataclass implementation ([8b00716](https://github.com/ernane/auction-house/commit/8b00716a05a9894524b492aea5e3712f896fda35))
* Add unit tests for Bid entity ([4ba91b0](https://github.com/ernane/auction-house/commit/4ba91b04905975e384f055851d07c83d9c7634fd))
* Adicionar entidade Leilão com implementação de dataclass ([2a04192](https://github.com/ernane/auction-house/commit/2a04192bda4ce82558add590712763bd866f19d1))

# 1.0.0 (2024-09-14)


### Features

* add Item entity and unit tests ([b63176c](https://github.com/ernane/auction-house/commit/b63176cab5b789f9889ba9aac1f74b4ac7ca176b))
