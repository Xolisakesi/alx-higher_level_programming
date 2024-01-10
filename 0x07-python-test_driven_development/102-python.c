#include "Python.h"
/**
* print_python_string - Prints information about a
* Python string.
* @p: A PyObject string object.
*/
void print_python_string(PyObject *p)
{
if (!PyUnicode_Check(p))
{
printf("[ERROR] Invalid String Object\n");
return;
}

printf("[.] string object info\n");
printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
printf("  length: %ld\n", ((PyASCIIObject *)p)->length);
printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &((PyASCIIObject *)p)->length));
}
