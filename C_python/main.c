/* 
 *     Created:  06 11月 2013 09:22:35
 *     Author:   weishijian@weishijian-MacUbuntu
       Description:  
 */

//#include <config.h>

#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

int main(int argc, char *argv[])
{
    Py_Initialize();  
    if(!Py_IsInitialized())   
    {  
        return -1;  
    }  
    
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./')");
    PyObject* pName;
    PyObject* pModule;
    PyObject* pDict;
    PyObject* pFunc;
    
    pName = PyString_FromString("call");
    pModule = PyImport_Import(pName);
    if(!pModule)
    {
        printf("can't find call.py");
        getchar();
        return -1;
    }
    
    pDict = PyModule_GetDict(pModule);
    if(!pDict)
    {
        return -1;
    }
    
    {
        pFunc = PyDict_GetItemString(pDict,"test");
        if(!pFunc || !PyCallable_Check(pFunc))
        {
            printf("can't find function [test]");
            getchar();
            return -1;
        }
        
        PyObject_CallObject(pFunc,0);
    }
    
    {
        pFunc = PyDict_GetItemString(pDict,"add");
        if(!pFunc || !PyCallable_Check(pFunc))
        {
            printf("can't find function [test]");
            getchar();
            return -1;
        }
        
        PyObject* args = PyTuple_New(2);
        PyTuple_SetItem(args,0,Py_BuildValue("l",3));
        PyTuple_SetItem(args,1,Py_BuildValue("l",4));
        PyObject *pAdded = PyObject_CallObject(pFunc,args);
        int ret = PyInt_AsLong(pAdded);  
        printf("add value:%d\n",ret);
        Py_DECREF(args);
    }    
    
    Py_DECREF(pName);
    Py_DECREF(pDict);
    Py_DECREF(pModule);
    Py_Finalize();    
    system("PAUSE");
    return 0;
}
