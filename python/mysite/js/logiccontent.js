var logicStr="return:1,key:power,msg:Power(%d) is negtive!,condition:,calc:power,judge:_0)\n\
return:1,key:pf,msg:Powerfector(%d) is negtive!,condition:,calc:pf,judge:_0)\n\
return:2,key:pf,msg:Powerfector(%d) too low!,condition:,calc:pf,judge:(0_0.5)\n\
return:3,key:power,msg:Power(%d) is incorrect!,condition:power!=0&&current!=0,calc:power/voltage/current/pf,judge:_0.5)|(1.5_\n\
return:3,key:pf,msg:Powerfector(%d) is incorrect!,condition:,calc:pf/power*(power*power+q*q)^0.5,judge:_0.5)|(1.5_\n\
return:4,key:power,msg:Power(%d) has deviation!,condition:power!=0&&current!=0,calc:power/voltage/current/pf,judge:[0.5_0.9]|[1.1_1.5]\n\
return:4,key:pf,msg:Powerfector(%d) has deviation!,condition:,calc:pf/power*(power*power+q*q)^0.5,judge:[0.5_0.9]|[1.1_1.5]\n\
return:5,key:current,msg:Current(%d) too low!,condition:,calc:current,judge:(0_0.03]\n\
return:5,key:pf,msg:Powerfector(%d) is low!,condition:,calc:pf,judge:[0.5_0.7)";