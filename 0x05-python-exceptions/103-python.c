#define PY_SSIZE_T_MAX ((size_t) -1)
#include <Python.h>
/**
* print_python_list - Prints information about a Python list object.
* @p: Pointer to a Python object of type list.
* This function prints various details about a Python list object,
* including its size, allocated memory, and the type of each element.
*/
void print_python_list(PyObject *p)
{
Py_ssize_t i, size;
PyObject *item;

if (!PyList_Check(p))
{
fprintf(stderr, "Invalid List Object\n");
return;
}

size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
/**
* print_python_bytes - Prints information about a Python bytes object.
* @p: Pointer to a Python object of type bytes.
* This function prints details about a Python bytes object, including its size,
* the first 10 bytes (if available), and the representation as a string.
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t i, size;
char *str;

if (!PyBytes_Check(p))
{
fprintf(stderr, "Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n", PyBytes_AsString(p));

if (size > 10)
size = 10;

printf("  first %ld bytes: ", size);
str = PyBytes_AsString(p);

for (i = 0; i < size; i++)
{
printf("%02hhx", str[i]);
if (i < size - 1)
printf(" ");
}
printf("\n");
}
/**
* print_python_float - Prints information about a Python float object.
* @p: Pointer to a Python object of type float.
* This function prints various details about a Python float object,
* including its value and additional information.
*/
void print_python_float(PyObject *p)
{
if (!PyFloat_Check(p))
{
fprintf(stderr, "Invalid Float Object\n");
return;
}

printf("[.] float object info\n");

if (PyFloat_IS_INTEGER(p))
{
printf("  value: %0.1f\n", PyFloat_AS_DOUBLE(p));
}
else
printf("  value: %.17g\n", PyFloat_AS_DOUBLE(p));
}

