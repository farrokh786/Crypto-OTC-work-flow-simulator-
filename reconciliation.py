def reconcile(internal, fills, blockchain_tx):
    size_match = abs(internal["size"] - sum(f["size"] for f in fills)) < 1e-8
    notional_match = abs(
        internal["notional"] - sum(f["size"] * f["price"] for f in fills)
    ) < 1
    wallet_match = blockchain_tx["to"] == internal["client_wallet"]

    return size_match and notional_match and wallet_match
