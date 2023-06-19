# OmniDex OLP Rebalancer

## **Project Brief**


Write a python script to monitor and rebalnce the target weighting for assets within the OLP pool.

1.  Consistent Indentation: Please use tabs throughout your codebase. This improves readability and makes your code more maintainable.

2. Descriptive Variable and Function Names:  Avoid single-letter variable names unless they have clear meanings within the context.

3. Comments and Documentation: Include comments in your code to explain complex sections, provide context, and clarify your thought process.

4. Error Handling: Implement appropriate error handling mechanisms. Use try-except blocks to catch and handle exceptions gracefully, providing informative error messages to help with debugging and troubleshooting.

6.  Modular Code: Break your code into smaller, reusable functions and classes. Modular code promotes reusability, readability, and easier maintenance. Each function or class should have a single responsibility and be relatively small.



### Task 1: Getting Started

**Step 1.**
Clone the rebalancer template here: 
[OmniDex OLP Rebalancer Template](https://github.com/TJ-2/OLP-Rebalancer.git) 

***Template Information***

The [config.json](https://github.com/TJ-2/OLP-Rebalancer/blob/master/config.json) file contains the relevant contract addresses for this project, along with the RPCs and other relevant configurations.

[abis.py](https://github.com/TJ-2/OLP-Rebalancer/blob/master/abis.py) file contains the relevant ABIs used to interact with the relevant contracts. 

[reserve_config.json](https://github.com/TJ-2/OLP-Rebalancer/blob/master/reserve_config.json) contains an example output for the 
1. Create a web3 instance connected to TelosEVM using a primary web3 provider.
2. Check if the connection is successful. 
3. Fallback to a secondary web3 provider in case of connection failure using appropriate error capturing. 

 RPC1: https://mainnet.telos.net/evm 
 RPC2: https://rpc1.us.telos.net/evm 
 RPC3: https://mainnet.telos.caleos.io/evm  

### Task 2: ETH-Calls:

1. Read Vault data from the "vault_reader" contract by calling the "getVaultTokenInfoV4" function

### Task 3:  Data Handling:

Use the data from Task 2 to calculate the following:

1. TargetShortSize For volatileToken:
*TargetShortSize = usdgAmounts(token) * *shortSizePoolRatio**

2. TargetLongSize For each volatileToken:
*TargetLongSize = usdgAmounts(token) * *longSizePoolRatio**

3. Shorts Deviation for each volatileToken:
*shortsDeviation  =  abs((target_short_size  -  maxGlobalShortSizes) /  maxGlobalShortSizes) *  100*

4. Longs Deviation for each volatileToken: 
*longsDeviation  =  abs((TargetLongSize  -  maxGlobalLongSizes) /  maxGlobalLongSizes) *  100*

Check if any of the longs/shorts deviations are greater than the GlobalMaxDeviation (this is set in config.json as 10%). If they are, call the "setMaxGlobalSizes' function on positionRouter passing in tokens[], longSizes[], and shortSizes[]. Ensure you are passing values with correct decimal precision. (You will not be able to call this function without special admin privileges, for this task just make a dummy call). 

### Task 3:  Running the program:

1. Run the program on a loop every X minutes. Choose an appropriate value for X. 

2. Generate a requiremenets.txt file

3. Run the script inside a Dockerfile. *Hint: Use the template for guidance.* 






