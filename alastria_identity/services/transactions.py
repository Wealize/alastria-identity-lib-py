class TransactionService:
    DEFAULT_GAS_LIMIT = 600000

    def __init__(self):
        self.transaction = self.config.basic_transaction.copy()

    def perform_transaction(self, function_call, function_arguments):
        # TODO
        pass
        # function_call_encoded = web3.eth.abi.encode_function_call(
        #     function_call, function_arguments
        # )

        # self.transaction.data = delegated(
        #     web3,
        #     function_call_encoded
        # )
        # self.transaction.to = self.config.identity_manager
        # self.transaction.gas_limit = self.DEFAULT_GAS_LIMIT
        # return self.transaction

    # function delegated(web3, delegatedData) {
    # return web3.eth.abi.encodeFunctionCall(
    #     config.contractsAbi.AlastriaIdentityManager.delegateCall,
    #     [config.alastriaCredentialRegistry, 0, delegatedData]
    # )
    # }
