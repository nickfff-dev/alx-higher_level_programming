#include <Python.h>
/**
* print_python_list_info - function that prints a pylist info
* @p: pointer to a Pyobject struct array
* Return: void
*/
void print_python_list_info(PyObject *p)
{
    long int size, alloc;
    int i;
    PyObject *item;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
