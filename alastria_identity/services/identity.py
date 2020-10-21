from alastria_identity.types import UserIdentity, Transaction


class UserIdentityService:
    def __init__(self, identity: UserIdentity):
        self.identity = identity

    def add_transaction(self, transaction: Transaction):
        self.identity.transactions.append(transaction)

    def get_signed_transactions(self):
        return map(self.sign_transaction, self.identity.transactions)

    def get_signed_transaction_from_anonymous(self, transaction):
        user_transaction = self.update_transaction_with_user_data(transaction)
        return self.sign_transaction(user_transaction)

    def update_transaction_with_user_data(self, transaction):
        transaction.nonce = self.get_user_nonce()
        transaction.gas_price = 0
        return transaction

    def sign_transaction(self, transaction: Transaction):
# TODO
#            try {
#       const tx = new EthereumTxAll(transaction)
#       const privKeyBuffered = Buffer.from(privateKey, 'hex')
#       tx.sign(privKeyBuffered)
#       const signedTx = `0x${tx.serialize().toString('hex')}`
#       return signedTx
#     } catch (err) {
#       console.log(err)
#       throw err
#     }
#   }
        return (transaction, self.identity.privatekey)

    def get_user_nonce(self):
        # TODO
    #     try {
    #   return await endPoint.eth.getTransactionCount(address)
    # } catch (err) {
    #   console.log(err)
    #   throw err
    # }
        pass
