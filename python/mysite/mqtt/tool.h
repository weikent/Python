// -*- C++ -*-

/* @(#)tool.h
 */

#ifndef _TOOL_H
#define _TOOL_H 1

#ifdef __cplusplus
extern "C"
{
#endif

    extern int GetCurrentTime(char *time);
    extern int GetIP(char *name, char *ip);
    extern int CompareWithWavyLine(char *buffer);
    extern int SetSystemTime(char *dt);
    extern int C_Ping(char *IP);
    extern int GetMAC(char *name, char *mac);
    extern int AddWaveLineAndNumInJSON(char *strJson, int len);
//    extern int AddWaveLineAndNumInJSON(char *strJson);
    extern int AddSeqNumInJSON(char *strJson, int seqOfIns, char *dt, char *optcode);
//    extern int AddSeqNumInJSON(char *strJson, int seqOfIns);    
    extern int GetRandomSeqOfIns();
    extern int ReplaceDevID(char *strJson);
    extern int checkIsEmpty(char *str);
    extern int decry(unsigned char *jsonStr, int len);
    extern int encry(unsigned char *jsonStr,int len);
    extern int isRightIP(const char *str);

    extern int CloseTCPConnection();
#ifdef __cplusplus
}
#endif

#endif /* _TOOL_H */

