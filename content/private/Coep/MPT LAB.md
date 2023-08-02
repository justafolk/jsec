D) write program to read flags register
name "add-sub"

org 100h

ADD AX, 00h
PUSHF 
POP BX    
      
MOV BX, 01h      
SUB BX, 02h
PUSHF 
POP BX    
ret

C) Write a program to add FFH with 01H, analyse the result for reflected changes 8n all flag bits

name "add-sub"

org 100h

MOV AX, 00ffh
MOV BX, 01h

ADD AX, BX
    
ret

B) Use this subroutine in A above in the main program to add two series of 32 bit numbers. Store the result from 1000:3000 onwards. If carry is generated in double word addition store it at third location  in sequence of the result.

name "add-sub"

org 100h

MOV [2000h], 1234h

MOV [1000h], 1234h

MOV [2002h], 1234h

MOV [1002h], 1234h

MOV DI, 1000h
MOV SI, 2000h
MOV BP, 3000h

MOV BX, 0000h

MOV DX, 02h

addcarry:
ADD BX, [DI]
ADD BX, [SI]
MOV [BP], BX

ADD DI, 02h
ADD AX, 02h
INC BP
INC BP

DEC DX
JNZ addcarry


Experiment 3:
Write an assembly language program in 8086 using EMU86:
A) as a subroutine to add two  32 bit numbers when operand pointers are initialised in main program.

First number is stored from 1000:1000H
Second number is stored from 1000:2000H
Result can be stored from 1000:3000H

B) Use this subroutine in A above in the main program to add two series of 32 bit numbers. Store the result from 1000:3000 onwards. If carry is generated in double word addition store it at third location  in sequence of the result.

C) Write a program to add FFH with 01H, analyse the result for reflected changes 8n all flag bits

D) write program to read flags register


ret

Write an assembly language program in 8086 using EMU86:
A) as a subroutine to add two  32 bit numbers when operand pointers are initialised in main program.

![[Pasted image 20230423230844.png]]


| G:Game              |             | You (Player 2) |             |
| ------------------- | ----------- | -------------- | ----------- |
| ------------------- |             | -------------- | ----------- |
| ------              |             | A: Remote      | B:On-campus |
| Examiner (Player 1) | 1: Lenient  | (75, 80)       | (10, 70)    |
|                     | 2: Moderate | (60, 50)       | (50, 60)    |
|                     | 3: Strict   | (40, 20)       | (90, 20)    | 

|              | Doc ID | Words in Document            | In class=Gujarat? |
| ------------ | ------ | ---------------------------- | ----------------- |
| Training Set | 1      | Gandhinagar Ahmedabad        | Yes               |
|              | 2      | Rajkot Ahmedabad Anand       | Yes               |
|              | 3      | Malad Borivali               | No                |
|              | 4      | Borivali Dadar Ahmedabad     | No                |
| Test Set     | 5      | Ahmedabad Ahmedabad Borivali | ?                 | 
