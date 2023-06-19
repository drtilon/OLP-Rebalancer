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

The [config.json](https://github.com/TJ-2/OLP-Rebalancer/blob/master/config.json) file contains the relevent contract addresses for this project, along with the RPCs and other relevent configurations.

[abis.py](https://github.com/TJ-2/OLP-Rebalancer/blob/master/abis.py) file contains the releveant ABIs used to interact with the relevant contracts. 

[reserve_config.json](https://github.com/TJ-2/OLP-Rebalancer/blob/master/reserve_config.json) contains an example output for the 
1. Create a web3 instance connected to TelosEVM using a primary web3 provider.
2. Check if the connection is successful. 
3. Fallback to a secondary web3 provider in case of connection failure using appropriate error capturing. 

 RPC1: https://mainnet.telos.net/evm 
 RPC2: https://rpc1.us.telos.net/evm 
 RPC3: https://mainnet.telos.caleos.io/evm  

### Task 2: ETH-Calls:

1. Read Vault data from the "vault_reader" contract by calling the "getVaultTokenInfoV4" function

### Task 3:  Data Handling pt1:

Use the data from Task 2 to calculate the following:

1. TargetShortSize For volatileToken:
*TargetShortSize = usdgAmounts(token) * *shortSizePoolRatio**

2. TargetLongSize For each volatileToken:
*TargetLongSize = usdgAmounts(token) * *longSizePoolRatio**

3. Shorts Deviation for each volatileToken:
*shortsDeviation  =  abs((target_short_size  -  maxGlobalShortSizes) /  maxGlobalShortSizes) *  100*

4. Longs Deviation for each volatileToken: 
*longsDeviation  =  abs((TargetLongSize  -  maxGlobalLongSizes) /  maxGlobalLongSizes) *  100*

Check if any of the longs/shorts deviations are greater than the GlobalMaxDeviation (this is set in config.json as 10%). If they are, call the "setMaxGlobalSizes' function on positionRouter passing in tokens[], longSizes[] and shortSizes[].  

### Task 3:  Running the program:

1. Run the program on a loop every X minutes. Choose an appropriate value for X. 

2. Generate a requiremenets.txt file

3. Run the script inside a Dockerfile. *Hint: Use the template for guidence.* 


### Bonus Task:








# Synchronization

Synchronization is one of the biggest features of StackEdit. It enables you to synchronize any file in your workspace with other files stored in your **Google Drive**, your **Dropbox** and your **GitHub** accounts. This allows you to keep writing on other devices, collaborate with people you share the file with, integrate easily into your workflow... The synchronization mechanism takes place every minute in the background, downloading, merging, and uploading file modifications.

There are two types of synchronization and they can complement each other:

- The workspace synchronization will sync all your files, folders and settings automatically. This will allow you to fetch your workspace on any other device.
	> To start syncing your workspace, just sign in with Google in the menu.

- The file synchronization will keep one file of the workspace synced with one or multiple files in **Google Drive**, **Dropbox** or **GitHub**.
	> Before starting to sync files, you must link an account in the **Synchronize** sub-menu.

## Open a file

You can open a file from **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Open from**. Once opened in the workspace, any modification in the file will be automatically synced.

## Save a file

You can save any file of the workspace to **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Save on**. Even if a file in the workspace is already synced, you can save it to another location. StackEdit can sync one file with multiple locations and accounts.

## Synchronize a file

Once your file is linked to a synchronized location, StackEdit will periodically synchronize it by downloading/uploading any modification. A merge will be performed if necessary and conflicts will be resolved.

If you just have modified your file and you want to force syncing, click the **Synchronize now** button in the navigation bar.

> **Note:** The **Synchronize now** button is disabled if you have no file to synchronize.

## Manage file synchronization

Since one file can be synced with multiple locations, you can list and manage synchronized locations by clicking **File synchronization** in the **Synchronize** sub-menu. This allows you to list and remove synchronized locations that are linked to your file.




