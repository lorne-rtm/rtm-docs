.. _features:

==================
Raptoreum Features
==================

.. _specifications:

Specifications
==============

- First block mined: `2021-02-26 21:18:18 UTC <https://explorer.raptoreum.com/block-height/1>`_
- No premine, no iCO, and a fair launch (first 24 hours 4 RTM block reward)
- Custom POW algorithm (GhostRider). ASIC & FPGA resistant
- 2 minute block time, 2MB blocks. DGW difficulty adjustment
- Smooth emissions and rewards, no halvings
- 21 billion total supply
- 51% protection (Chainlocks)
- Smartnodes
- Privacy as an option with CoinJoin
- Instant transactions using InstantSend
- Futures transactions @ protocol level (industry first)
- Assets with unique naming (non-fungible). Fungible also
  available (testnet)
- Transaction decoupling (development)
- Easy IPFS upload and attach for assets (development)
- Smart Contracts in common programming languages (development)



.. _smartnode-network:

Smartnodes
==========

Smartnodes are a special type of Raptoreum node which usually are run on a VPS or dedicated server.
Smartnodes help secure and expand the Raptoreum networks capabilities, they enable the following features.

- 51% protection / double spend attack
- InstantSend, transactions fully confirmed within seconds
- Chainlocks, these are what make the above two features possible
- Store and execute Smart Contracts (development)
- Run side chain for transaction decoupling (development)

They also contribute to the network in the same way as other Raptoreumcore
full nodes such as:

- Block and transaction validation and propagation
- Serving chaindata to other nodes

Anybody can setup and operate a Smartnode helping strengthen and decentralize the network and earning passive income as reward for doing so. Smartnodes need to show their commitment to the network by locking up a collateral of 1.8 million RTM. A VPS or dedicated server with a static IPv4 is also required. Smartnodes are paid for their service from block rewards as wll as a percentage from special transactions.

- Block reward 20%
- 80% of transaction fees from futures transactions and asset transactions.
- They will also be paid in the future for Smart Contracts storage and execution.

You :download:`Download <../../_static/papers/Raptoreum_Rewards_Structure.pdf>` the Raptoreum block reward and smooth reduction schedule or view it below.

.. raw:: html

    <embed src="../../_static/papers/Raptoreum_Rewards_Structure.pdf" type="application/pdf" width="700px" height="500px" />

.. _instantsend:

InstantSend
===========

InstaSend on Raptoreum speeds up transactions, which is vital in today's
fast-paced financial landscape.

How InstaSend Works:
--------------------

- **Quorum System:** Utilizes the Smartnode network to form voting quorums 
of diffrent, sizes which vote on if transactions are valid.
- **ChainLocks:** If transaction is valid, the Smartnodes lock the input and
broadcast it to the network.

Importance in Financial Transactions:
-------------------------------------

- **Faster Confirmations:** Contrary to Bitcoin or Ethereum, which need
  multiple confirmations over time, Raptoreum confirms transactions within seconds.
- **Speed and Spendability:** This rapid processing ensures funds are readily
  available, essential for trading, payments, and remittances.

Understanding Confirmations:
----------------------------

- When a transaction is made and broadcasted to the network it is placed in
the mempool. It waits here for the miners to pick it up and include it in
a block. Once it is added to a block and that block is added to the blockchain
it has one confirmation. Each block added after that increass the confirmations.

.. _chainlocks:

ChainLocks
==========




