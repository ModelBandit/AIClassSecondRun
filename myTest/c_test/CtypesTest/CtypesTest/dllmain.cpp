// dllmain.cpp : DLL 애플리케이션의 진입점을 정의합니다.
#include "pch.h"

extern "C" __declspec(dllexport) void MyFunc()
{
    MessageBox(NULL,
        "MyFunc Called",
        "DLLMessage",
        MB_OK);
}

extern "C" __declspec(dllexport) char* BubbleSort(int* arr, int len)
{
    int temp;
    for (int i = 0; i < len; ++i) {
        for (int j = 0; j < len; ++j) {
            if (arr[i] < arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    char cool[] = "cool";
    return cool;
}

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

