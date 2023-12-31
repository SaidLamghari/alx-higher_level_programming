#include <Python.h>

/**
 * print_python_list_info -  Start of the function that
 * Prints basic information about Python lists
 * @p: The pointer to the Python
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t num;
	Py_ssize_t count;
	PyObject *it;

	num = PyList_Size(p);
	
	printf("[*] Size of the Python List = %ld\n", num);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	
	count = 0;

	if (num > 0)
	{
		while (count < num)
		{


			it = PyList_GetItem(p, count);

			printf("Element %ld: %s\n", count, Py_TYPE(it)->tp_name);
		
			count++;
		}
	}
}
