#include <Python.h>
/**
 * print_python_list_info - list info
 * @p: pointer to object
 * Return: list
 */
void print_python_list_info(PyObject *p)
{
	int i;

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = PyList_GET_ALLOC(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		PyObject *type = PyObject_Type(item);

		printf("Element %d: %s\n", i, type->tp_name)
	}
}
