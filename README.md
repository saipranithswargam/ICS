# ICS Group-9 Instructions to Execute Code :-

## Requirements

    1. WSL on windows system.
    2. python3
    3. ubuntu version 22^*

## Steps for Executing Python Codes :-

    1. Run the files in terminal as python3 fileName.py
    2. Make sure that you are in the same directory in terminal
    3. If opened in vs code click on play Button on top right to run the code

## Steps for Executing and checking Vulnarability Files :-

-   ### For MD-5 Vulnarability :-
    -   Open CMD and navigate to directory of **vulnarability_md5**
    -   Enter **erase.exe** and click Enter to see contents of **erase.exe**
    -   Enter **hello.exe** and click Enter to see contents of **hello.exe**
    -   Now Navigate to **vulnarability_md5** on WSL
    -   `By Entering cd /mnt/c` you will be in **C** Directory of windows
    -   From Navigate to **vulnarability_md5** on WSL
    -   Enter **MD5sum hello.exe** it will give MD5 hash of hello.exe
    -   Similarly Enter **Md5sum erase.exe** it will give MD5 hash of erase.exe which will be same **which it should not**
-   ### For SHA-1 Vulnarability :-
    -   Navigate to **vulnarability_sha-1** on WSL
    -   `By Entering cd /mnt/c` you will be in **C** Directory of windows
    -   From There Navigate to **vulnarability_sha-1** on WSL
    -   Enter **shasum shattered-1.pdf** it will give SHA-1 sum of that PDF
    -   Simularly Enter **shasum shattered-2.pdf** it will give SHA-1 sum of the second PDF
    - Compare them they will be equal which it should not

