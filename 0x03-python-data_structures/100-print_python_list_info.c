#include <Python.h>

/**
 * print_python_list_info -  Start of the function that
 * Prints basic information about Python lists
 * @p: The pointer to the Python
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t s, count;
	PyObject *it;

	size = PyList_Size(p);
	
	printf("[*] Size of the Python List = %ld\n", s);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (count = 0; count < s; count++)
	{
		item = PyList_GetItem(p, count);
		printf("Element %ld: %s\n", count, Py_TYPE(it)->tp_name);
	}
}
