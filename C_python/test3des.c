/*
 * =====================================================================================
 *
 *    Filename:  test3des.c
 *
 * Description:  
 *
 *    
 *
 *     Version:  0.1
 *     Created:  18 Jul 2014  14:49:31
 *
 *     Authors:  weishijian
 *     Company:  DingQing Technology, Ltd.
 *    Revision:  
 * ======================================================================================
 * @0.1   weishijian   18 Jul 2014  14:49:31 , create orignal file
 * ======================================================================================
 * Copyright (c) , DingQing Technology, Ltd.
 * ======================================================================================
 */

/*----------------Includes---------------*/ 
//包含的头文件 
#include "3des.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*------------Local Variables----------- */ 
//定义一些本地变量 



/*------Local Structures and Typedefs ---*/ 
//要使用的一些数据结构 



/*-----------Extern Variables -----------*/ 
//使用到的一些外部变量 



/*-------------Definitions---------------*/ 
//一些#defines及具体的函数实现


int main(int argc, char *argv[])
{
    char a[10] = "aaa";
    encry(a, 3);
    printf ("%s\n",a);
    decry(a, 8);
    printf ("%s\n",a);
    printf ("%d\n",a[7]);
    return 0;
}