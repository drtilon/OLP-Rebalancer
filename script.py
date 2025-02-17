import json
from abis import *
from web3 import Web3
import time

config = json.load(open('config.json'))


# checking providers
def check_provider(tlos_providers):
    for provider in tlos_providers:
        if tlos_provider := Web3(Web3.HTTPProvider(provider)):
            return tlos_provider


# retrievs the usdgamount 
def getSizes(data, config):
    targetSize = [data[2], data[17], data[32]]
    return [x * config for x in targetSize]


# calculates the deviation
def deviation(sizeType, maxGlobalSize):
    deviations = []
    for x in range(3):
        deviations.append(abs((sizeType[x] - maxGlobalSize[x]) / maxGlobalSize[x]) * 100)
    return all


def main():
    tlos_provider = check_provider(config["telos_mainnet"])

    contract_address = config["vault_reader"]
    contract = tlos_provider.eth.contract(address=contract_address, abi=vaultReader())
    data = contract.functions.getVaultTokenInfoV4(config['vault'],
                                                  config['position_router'],
                                                  config['WTLOS'],
                                                  0,
                                                  config['volatileTokens']
                                                  ).call()
    # calculating target sizes
    targetShortSize = getSizes(data, config["SHORT_SIZE_POOL_RATIO"])
    targetLongSize = getSizes(data, config["LONG_SIZE_POOL_RATIO"])

    # getting max global sizes from the contract
    maxGlobalShortSize = [data[8], data[23], data[38]]
    maxGlobalLongSize = [data[9], data[24], data[39]]

    # calculating deviations
    shortDeviation = deviation(targetShortSize, maxGlobalShortSize)
    longDeviation = deviation(targetLongSize, maxGlobalLongSize)

    if ((shortDeviation or longDeviation) > config["GlobalMaxDeviation"]
        for (shortDeviation, longDeviation) in zip(shortDeviation, longDeviation)):
        contract_address = config["position_router"]
        contract = tlos_provider.eth.contract(address=contract_address,
                                          abi=positionManager())
        # contract.functions.setMaxGlobalSizes(config['volatileTokens'], targetLongSize, targetShortSize)


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(300)
