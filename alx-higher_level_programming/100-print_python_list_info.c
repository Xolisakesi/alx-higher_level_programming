#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h> 
#include <listobject.h>

void print_python_list_info(PyObject *p) 
{
Py_ssize_t size, i;
PyObject *obj;

size = PyList_Size(p);
printf("[*] Size of the Python List = %ld\n", size);

printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; ++i) 
{
obj = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
}
}
