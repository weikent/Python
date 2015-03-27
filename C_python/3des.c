/*
 * =====================================================================================
 *
 *    Filename:  3des.c
 *
 * Description:  encry and decry of 3des, use des.h/c
 *
 *    
 *
 *     Version:  0.1
 *     Created:  18 Jul 2014  14:16:37
 *
 *     Authors:  weishijian
 *     Company:  DingQing Technology, Ltd.
 *    Revision:  
 * ======================================================================================
 * @0.1   weishijian   18 Jul 2014  14:16:37 , create orignal file
 * ======================================================================================
 * Copyright (c) , DingQing Technology, Ltd.
 * ======================================================================================
 */

/*----------------Includes---------------*/ 
//包含的头文件 
#include "des.h"
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


/*     //return   str;    */
/* } */



/* 
 * ===  FUNCTION  ========================================================================
 *         Name: encry
 *  Description: 3Des加密
 *   Parameters: 
/// @param jsonStr 值-value变量。是需要加密的字符串
/// @param len 字符串的长度。
* 
* Return Value: 
*      Created: Thu Apr 17 09:27:37 2014 by世建 魏
*     Revision: 
* =======================================================================================
* @0.1   世建 魏  Thu Apr 17 09:27:37 2014 , create orignal file
* =======================================================================================
* Copyright (c), DingQing Technology, Ltd.
* =======================================================================================
*/

int encry(unsigned char *jsonStr,int len)
{
//    unsigned char desOut[TEXT_SIZE + 8] = {0};
    unsigned char *desOut = (unsigned char*)malloc(len + 8);
    memset(desOut, 0, len + 8);
    unsigned char desTempOut[9] = {0};
    int i = 0;
    while(1)
    {
        unsigned char temp[8] = {0};
        bzero(desTempOut, 9);
        if ((i + 8) <= len)
        {
            memcpy(temp, jsonStr + i, 8);
            /* printf ("temp = %s\n", temp); */
  
            desD(temp, desTempOut);
/*             printf ("desTempOut = %s\n", desTempOut); */
/*             for (int i = 0; i < 8; ++i) */
/*             { */
/*                 printf ("%0X \n",desTempOut[i]); */
/*             } */
/* //            strncat(desOut, desTempOut, 8); */
            int j = 0;
            for (j = 0; j < 8; j++)
            {
                desOut[i+j] = desTempOut[j];
            }

            /* printf ("i = %d\n", i); */
            /* for (int k = 0; k < 8; ++k) */
            /* { */
            /*     printf ("======%0X \n",desOut[k+i]); */
            /* } */

            i += 8;


        }
        else
        {
            memcpy(temp, jsonStr + i, len - i);
            int k = 0;
            for (k = len - i; k < 8; k++)
            {
//                sprintf(temp + k, "%0x", 8 - (strlen(jsonStr) -i));
                temp[k] = 8 - (len -i);
            }
//            printf ("temp = %s\n", temp);
            desD(temp, desTempOut);
//            printf ("desTempOut = %s\n", desTempOut);
            /* for (int i = 0; i < 8; ++i) */
            /* { */
            /*     printf ("%0X \n",desTempOut[i]); */
            /* } */
            int j = 0;
            for (j = 0; j < 8; j++)
            {
                desOut[i+j] = desTempOut[j];
            }
            i += 8;

            break;
        }
    }

    memcpy(jsonStr, desOut, len + 8);
    free(desOut);
    return i;
}



/* 
 * ===  FUNCTION  ========================================================================
 *         Name: decry
 *  Description: 3Des解密
 *   Parameters: 
/// @param jsonStr 值-value变量。需要解密的字符串
/// @param len 字符串长度
* 
* Return Value: 
*      Created: Thu Apr 17 09:28:28 2014 by世建 魏
*     Revision: 
* =======================================================================================
* @0.1   世建 魏  Thu Apr 17 09:28:28 2014 , create orignal file
* =======================================================================================
* Copyright (c), DingQing Technology, Ltd.
* =======================================================================================
*/

int decry(unsigned char *jsonStr, int len)
{
    unsigned char desOut[2048 + 8] = {0};
    unsigned char desTempOut[9] = {0};
    int i = 0;


    /* for (int i = 0; i < len; ++i) */
    /* { */
    /*     printf ("%02X ", jsonStr[i]); */
    /* } */

    /* printf (" \n"); */

    while(1)
    {
        bzero(desTempOut, 9);
        unsigned char temp[8] = {0};

        if ((i + 8) <= len)
        {
            memcpy(temp, jsonStr + i, 8);

            /* for (int i = 0; i < 8; ++i) */
            /* { */
            /*     printf ("%02X \n", temp[i]); */
            /* } */

            desE(desTempOut, temp);

            //        strncat(desOut, desTempOut, 8);
            memcpy(desOut + i, desTempOut, 8);
            i += 8;
        }
        else
        {
            break;
        }
//        printf ("desTempOut = %s\n", desTempOut);
    }
//    printf("desOut = %s \n", desOut);
    
//    strcpy(jsonStr, desOut);
    memcpy(jsonStr, desOut, len);

    return 0;
}

