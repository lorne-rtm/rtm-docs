Raptoreum Documentation
=======================

Welcome to the Raptoreum Documentation! These "docs" will cover everything from the basics, to advanced use, to docs for developers looking to build on `Raptoreum <https://raptoreum.com>`_ (RTM). Raptoreum is looking to solve issues that are apparent on other Blockchain projects through innovation. 
RTM is a POW (Proof of Work) based Blockchain which is ASIC and FPGA resistant, and can be mined on common hardware (CPU / GPU) which increases and encourages decentralization. It also offers an alternative way to contribute to the network and earn passive income through collateralized Smartnodes.

.. note:: The current mainnet wallet version is 1.3.17.05. Please make sure you are using that version, you can download it `here <https://github.com/Raptor3um/raptoreum/releases/tag/1.3.17.05>`_.

Problems We Are Solving
-----------------------

.. tab-set::

    .. tab-item:: Decentralization

        Raptoreum employs GhostRider, a custom Proof of Work (POW) algorithm designed to resist ASIC and FPGA mining hardware. This strategic choice ensures that mining Raptoreum (RTM) remains accessible to everyone, using standard computing equipment. By avoiding the centralization risks associated with specialized mining hardware, Raptoreum fosters a more decentralized network. This inclusivity not only broadens participation but also enhances the network's resilience against censorship and attacks, reinforcing the core principles of blockchain technology.

    .. tab-item:: 51% Protection

        Raptoreum enhances security through quorums and chainlocks via its SmartNode network, significantly mitigating the risk of a 51% attack, a vulnerability many POW blockchains face. By requiring consensus among SmartNodes for transaction validation and block addition, it becomes exceedingly challenging for attackers to alter the blockchain. This mechanism not only deters potential attacks but also bolsters network integrity and trust.

    .. tab-item:: Assets

        Raptoreum introduces a versatile asset system, supporting both fungible and non-fungible assets. Its non-fungible assets (NFAs) leverage a unique root and sub-asset structure, ensuring each asset has a distinct name for easy identification. Only one instance of each name can exist on the blockchain. This clarity in naming simplifies asset verification and recognition. Users can effortlessly mint, transfer, and oversee these assets directly from the Raptoreum core wallet, eliminating the need for programming skills or deep blockchain understanding.

    .. tab-item:: Smart Contracts

        Raptoreum's smart contract solution stands out by supporting widely-used programming languages like Java, R, and Python, diverging from the niche languages like Solidity that are common in blockchain environments. This inclusivity taps into a vast pool of existing developers, significantly lowering the barrier to entry for blockchain development. For businesses, this approach translates to substantial cost savings in areas such as code audits and contract creation, making blockchain adoption more accessible and appealing. 

    .. tab-item:: Scaling

        Scalability is pivotal for blockchain networks to manage increasing transaction volumes efficiently. Raptoreum innovatively addresses this with transaction decoupling, relocating transactions off the main chain to a sidechain operated by the Smartnode network. This strategy not only alleviates congestion but also substantially elevates the network's transactions per second (TPS). Moreover, Raptoreum's smart contracts, distinct from Ethereum's, are stored and executed on Smartnodes, optimizing performance. A key feature ensuring user-friendliness is Raptoreum's adjustable fees, guaranteeing that users are never overcharged, thus maintaining the network's affordability and accessibility as it grows.

Explore Our Documentation
-------------------------

.. grid::

    .. grid-item-card:: Advanced Docs

        Dive deeper into the technical aspects of Raptoreum, including node setup, consensus mechanisms, and more.

    .. grid-item-card:: User Docs
        :link: user_docs/index.html

        Get started with Raptoreum, learn how to send and receive transactions, secure your wallet, and more.

.. toctree::
   :hidden:
   :maxdepth: 3
   
   user_docs/index