#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - Prints bytes object information
* @p: Python Object
* Return: no return
*/
void print_python_bytes(PyObject *p)
{
long i;
if (!PyBytes_Check(p))
{
printf("[ERROR] Invalid Bytes Object\n");
return;
}
printf("[.] bytes object info\n  size: %ld\n  trying string: %s\n  first %ld bytes:",
((PyVarObject *)p)->ob_size, PyBytes_AsString(p), (((PyVarObject *)p)->ob_size >= 10) ? 10 : ((PyVarObject *)p)->ob_size + 1);

for (i = 0; i < (((PyVarObject *)p)->ob_size >= 10 ? 10 : ((PyVarObject *)p)->ob_size + 1); i++)
printf(" %02x", ((unsigned char *)(PyBytes_AsString(p)))[i] & 0xff);
printf("\n");
}

/**
* print_python_list - Prints list information
* @p: Python Object
* Return: no return
*/
void print_python_list(PyObject *p)
{
long i, size;i
PyListObject *list;
size = ((PyVarObject *)p)->ob_size;
list = (PyListObject *)p;

printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, list->allocated);

for (i = 0; i < size; i++)
{
PyObject *obj = list->ob_item[i];
printf("Element %ld: %s\n", i, (obj->ob_type)->tp_name);
if (PyBytes_Check(obj))
print_python_bytes(obj);
}
}

