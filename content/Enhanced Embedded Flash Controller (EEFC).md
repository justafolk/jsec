- 1 word = 16 bits = 2 bytes
- 

- Provides an interface of the flash block with 32 bit internal bus.
- Has 128 bit wide memory interface
	- Increase performance (in thumb-2 mode) 
	- up to 150 Mhz
- Manages
	- Programming, erasing, locking and unlocking sequences of the flash using a full set of commands.
- Code Loop Optimization
- 128 lock Bits 
	- One by One lock Bit Programming 
	 - locking and unlocking operations 
- 9 General purpose GPNVM Bits 
- Erasing
	- Entire flash
	- by plane
	- by sector
	- by page
	- Supports Erasing before programming
 - Error Flags
	 - ECC Singe
	 - Multiple 
 - Reading of Calibration Bits 
	- Calibration Bits NVM bits are used to calibrate the brownout detector and the voltage regulator
 - Register Write Protection 

### Functional Description
- One memory plane organized in several pages of the same size.
- Buffers
	- 2x   128bit buffers for code read optimization 
	- 1x    128bit buffer for data read optimization.
	- 1x     Write Buffer 
		- Manages page programming.
		- Equal size as page size  == 512 bytes
		- write only 
		- accesible along 1 Mbyte address space 
### Read Operations 
- Flash memory accesible through 8, 16, 32 bit reads.

### Code Read Optrimization
- Code read optimization is enabled if the bit EEFC_FMR.SCOD is cleared.

![[Pasted image 20230217193110.png]]

- Command State Chart 
![[Pasted image 20230217193225.png]]

![[Pasted image 20230217193555.png]]

### Write commands 
- DMA write accesses must be 32 bit aligned. 
- if single byte is to be written in a 32 bit word, the rest of the bits should be 1s
- Only 0 values can be programmed using Flash technology;
- To program words in a page, first the page must be erased.
- 1 is the erased value
- 

partial page programming
- Data to be programmed must be contained in integer multiples of 128-bit address-aligned words.  128-bit words can be programmed only if all the corresponding bits in the Flash array are erased (at logical value 1)

![[Pasted image 20230217195506.png]]

![[Pasted image 20230219173817.png]]

![[Pasted image 20230219173903.png]]

![[Pasted image 20230219173943.png]]


- there are sectors of 128 kbytes each
- 1 page == 512 bytes pages == 256 pages == 1 sectors 

- the first sectore is divided into 3 parts
  - 8kb
  - 8kb
  - 112kb
- there are 4 pages of data 
- 1 word = 2 bytes 
- 1 pages = 256 words = 2 * 128 words
- Flash write can only convert 1 to 0
- Flash erase sets all bits to 0

- internal rom : 0x00800000
- flash : 0x400000

- lock and unlock flash addresses to protect data from write and erase.

- When security is enabled, any access to the Flash,
SRAM, core registers and internal peripherals, either through the SW-DP, the ETM interface or the Fast Flash
Programming Interface, is blocked.


- Erase by 
  - Erase al memory
  - Erase by pages 
  - Erase by sectors