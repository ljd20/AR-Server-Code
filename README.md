# Virtual Reality HeadSet

Group Members:  
*[Louise Davis](https://github.com/ljd20)*  
*[Chris Myers](https://github.com/chrischris531)*  
*[Luca Chammach](https://github.com/ljc20)*  
*[Kert Laansalu](https://github.com/kert114)*  
*[Kia Popat](https://github.com/kiapopat)* 

*[Henry Hausamann](https://github.com/)* 

We designed and built an augmented reality headset controlled by an FPGA and Arduino handset. The headset overlays data onto the real world, such as location, time and date, altitude and a map. There is a multiplayer element, where all the current users of the headsets share their locations live on the map. All the server communication is handled via TCP, with four servers running on AWS to enable reading and writing of two databases (one for hardware, one for GPS), while the hardware communication is performed serially via UART.
