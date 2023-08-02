# Introduction to Programmable Logic Controllers (PLC)

## What is a Microcontroller
  - Technically, its a more well adjusted setup for microprocessor.
  - Microcontroller is a complete microprocessor system, consisting of microprocessor, ROM / EPROM, RAM, parallel I/O ports, serial ports, timer, clock all built on a single integrated circuit.
  - It can be used to perform control funtions so it is like a microcomputer.
  - More complex than a microprocessor.

## Advantages of Microcontroller over microprocessor
  - Cost wise, Microcontroller is cheaper than microprocessor.
  - Microcontroller has more I/O components than microprocessor based systems. 
  - Microcontrollers have a wide variety of applications of intelligent products such as personal computer keyboards or AI devices.
  - Low cost products like toys, washing machine, microwave, ovens, electric drills are made up of microcontrollers not microprocessors. 

## Features of Microcontroller 8051
  1. 8051 has 8-bit ALU
  2. 4 KB ROM (EPROM)
  3. 128 byte RAM
  4. Dual 16 bit timer, event counter
  5. 32 I/O lines for four 8 bit I/O ports 
  6. Full featured serial port. 
  7. It can address 64 KB of program memory
  8. It can address 64 KB of data memory.
  9. 111 instructions 
  10. Two external interrupts (INTR ? NMI ?)
  11. Clock 12 MHz frequency 

## The Need for PLC 
  - Suppose in a huge setup / factory even, there are many panels, devices, controllers, processors. Hardwired panels were very time consuming to wire, debug and change.
  - This led to the identification of the following requirements for computer controllers to replace hardwired panels 
  1. Solid-state not mechanical (In electronics, "solid state" refers to devices or systems that are built entirely with solid materials, typically semiconductors such as silicon.)
  2. Easy to modify I/O devices. 
  3. Easy to be accessed and maintained by plant electricians.
  4. Be able to function in an industrial environment.

## Some PLC facts
  - Introduced in late 1960's 
  - Intended to replace replay logic system 
  - Programmable, reusable, reliable
  - Used Ladder logic for programming 
  - no hard drive, they had battery backup.
  - sturdy as hell, strong af 

## Formal PLC 
  - A PLC is a specialized computer used to control machines and processes.
  - It uses a Programmable memory to store instructions and specific functions that include 
    - On / Off control
    - timing
    - counting
    - sequencing
    - arithmetic  
    - data handling 

## Advantages of PLC control systems 
  1. Flexible as hell 
      - Original Equipment manufacturers (OEMs) can provide system updates for a process by somply sending out a new program.
      - It is easier to creat and change a program in a PLC than to wire and rewire a circuit. End-users can modify the program in the field.
  2. Faster response time, less and simpler wiring | easy to maintain
      - Eliminates much of the hard wiring that was associated with conventional relay control circuits. 
      - PLCs operate in realtime which means that an event taking place in the field will result in an operation or output taking place.
  3. Solid state | no moving parts bitch | no mechanical parts
      - Increased Rreliability 
        - Once a program has been written and tested it can be downloaded to other PLCs.
        - Since all the logic is contaied in the PLC's memory, there is no chance of making a logic wiring error.
  4. Modular design - easy to repair and expand. | divided in modules 
  5. Handles much more complicated systems | has control over the whole system so accessing complicated areas wouldn't be a burden.
  6. Sophisticated instruction sets available | 111 instructions available.
  7. Allows for diagnostics "Easy to troubleshoot"
      - PLCs have resident diagnostic and override functions allowing users to easily trace and correct software and hardware problems.
  8. Cheap as hell | less expensive
      - The intention to replace relay control system had a huge backbone of cost cutting. If an applcation applies more than 6 relay controls, its more cost efficient to install a PLC instead.
  9. Communication Capability
      - A PLC can communicate with other controllers or computer equipment. 
      - They can be networked to perform such functions as: supervisory control, data gathering, monitoring devices and process paramters and downloading and uploading of programs.


## PLC Architecture
  - **An Open Architecture** design allows the system to be connected easily to devices and programs made by other manufacturers.
  - **A closed architecture or proprietary** system is one whose design makes it more difficult to connect devices and programs made by other manufacturers. Such as Apple :D
  - **REFER SLIDE 17 for DIAGRAM**
  1. **I/O Configurations**
      1. Fixed I/O
          - Is commonly used in small PLCs setups
          - Comes in one package with no separate removable units. 
          - The processor and I/O are packed together.
          - Low cost but lacks Flexiblility.
      2. Modular I/O 
          - Is divided into blocks/compartments in which separate modules can be plugged.
          - This feature greatly increases your options and the unit's Flexiblility. You can choose from all the modules available and mix them in any way you desire.
          - When a module is setup, it makes an electrical connection with a series of contacts, called backplane. The blackplace is located at the rear of the rack. Its like the way we setup fuse, just slide it into the rack and it connected to metal plates in the back. If difficulty visualizing, refer to slide no. 21.
  3. **Power Supply**
      - Supplies DC power to other modules that plug into the rack.
  4. **Processor (CPU)**
      - Brain
      - microprocessor which controls logic and communcations among the modules.
      - logic can be entered into relay ladder logic form.
      - Accepts input from various sensing devices => executes the stored user program and sends appropiate ouput commands to control devices.
  5. **Programming devices**
      1. Personal Computer
          - A Personal Computer is the most commonly used programming device. 
          - Create, edit, store document, troubleshoot programs.
          - Communicates with the PLC via serial or parallel data communications link 
      2. Hand Held unit with Display
          - Hand held programming devices are sometimes used to program small PLCs 
          - They are Compact, inexpensive and easy to use, but are not able to display as much logic on screen as computer monitor normally would.
          - They are often used on the factory floor for troubleshooting, modifying programs and transferring programs to multiple machines.
  6. **I/O Section**
      - Consists of Input | output modules 
      - Basic Mdule types
          - Digital (discrete) output modules 
              1. Optical isolation provided 
                  Optical isolation is implemented to ensure electrical isolation between the internal circuitry of the PLC and the external devices being controlled. It helps protect the PLC's sensitive electronics from potential electrical disturbances or faults that may occur in the external devices.
              2. Relay, transistor
              3. Transistor based outputs may be either Current sourcing or Current sinking.
          - Digital (discrete) output modules 
              1. Optical Isolation provided 
              2. Diode based - Current sinking, sourcing or both depending on the device. 
          - Sinking means internally connected with the common (-ve terminal). Input or output card wired internally to common is typically regarded as a sinking input or sinking output card. 
          REFER Slide 29
          - Sourcing means internally connected with the source (+ve terminal). Input or output card connected directly to power, its typically called as sourcing input or sourcing output card.

      - Input Module
          1. Forms the interface by which input fiel devices are connected to the controller. Basically an adaptor like thing for input devices?
          2. The terms "field" and "real world" are used to distinguish actual external devices that exist and must be physically wired into the system.
          3. Input Module levels from 5V to 240 V in an input channel SLIDE 32 
          4. PLC handles AC and DC inputs separately, see SLIDE 33 for diagram.
          5. Theres a multiplexer for handling various inputs. 
      - Output Module 
          1. Forms the interface by which output field devices are connected to the controller.
          2. PLCs employ an optical isolator which used light to electrically isolate the internal componenets from the input and output terminals. SLIDE 35 for diagram.
          3. Output differ in Relay output unit and Triac Output unit 
          4. For handling various outputs, demultiplexer is used. 

  7. **PLC Ladder Diagrams**
      - Ladder diagram is a symbolic and schematic way of represnting both the system hardware and the process controller.
      - It is called a ladder diagram because the various circuit devices connected in parallel across the ac line form something that looks like a ladder, with each parallel connection a "rung" on the ladder.
      - In the construction of a ladder diagram, it is undestood that each rung of the ladder is composed of a number of conditions or input states and a single command output. 
      - Special symbols are used to represent the various circuit elements in a ladder diagram.
      - The term latch circuit is used for the circuit used to carry out a continous supply of electrical signal. It is a self maintaining circuit in that, after being energised, it maintains that state until another input is received.
  - Example of Ladder Programming
      - **PLC MIXER PROCESS CONTROL PROBLEM**
      - Intention: Mixer motor to automatically stir the liquid in the vat when the temperature and pressure reach a certain value.
      - Alternate manual push button control of the motor to be provided.
      - The temperature and pressure sensor switches close their respective contacts when conditions reach their certain values.
      - Process Control Relay ladder diagram
      - Simple circuit lol 
      -  
![[Pasted image 20230608111406.png]]

   - PLC Input Module Connections
   - ![[Pasted image 20230608111847.png]]
   - PLC Output Module Connections
   - ![[Pasted image 20230608111906.png]]
   - ![[Pasted image 20230608111923.png]]
   - Triac switches motor ON and OFF in accordance  with the control signal from  the processor
   - ![[Pasted image 20230608111940.png]]
   - The format used is similar to that of the hard-wired  relay circuit
   - I/O address format will differ, depending on the PLC  manufacturer. You give each input and output device  an address. This lets the PLC know where they are  physically connected
   - ![[Pasted image 20230608112055.png]]
   - **PLC Operating Cycle**
   - During each operating cycle, the controller examines the status of input devices, executes the user program and changes outputs accordingly.
   - The completion of one cycle of this sequence is called a scan.
   - The scan time, the time required for one full cycle, provices a measure of the speed of response of the PLC.
   - ![[Pasted image 20230608112250.png]]
   - Modifying A PLC program
   - The change requires that the manual pushbutton control should be permitted to operate at any pressure but  not unless the specified temperature setting has been  reached.
   - ![[Pasted image 20230608112425.png]]
   - If a relay system were used, it would require some rewiring of the system, as shown to acheive the same desired change.
   - In this case, no rewiring is necessary all thanks to PLC.

## PLC vs Personal Computers

| PLCs                                                                | Personal Computers                                                                                    |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Operates in the industrial Environment                              | Personal Usage                                                                                        |
| Is programmed in relay ladder logic                                 | Capable of executing several programs simultaneously in any order                                     |
| Has no Keyboard, CD drive or other peripherals.                     | Has various peripheral devices                                                                        |
| Has communication ports and terminals for input and output devices. | Some manufacturers have software and interface cards available so that a PC can do the work of a PLC. |

## PC Based Control Systems 
1. Advantages
	- Lower initial cost
	- Less proprietary hardware and software required
	- Straightforward data excchange with other systems
	- Speedy information processing
	- Easy customization
## PLC Size Clarification
1. Criteria 
	- Number of inputs and outputs 
	- Cost 
	- Physical size 
- Nano PLC 
	- Smallest sized PLC 
	- Handles up to 16 I/O points 
- Micro PLC 
	- Handles up to 32 I/O points 
	- 
