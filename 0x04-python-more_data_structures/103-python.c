#include <Python.h>
void print_python_bytes(PyObject *p)
void print_python_list(PyObject *p)

/**
 * print_python_list - Start of function
 *		that prints basic information about Python lists
 * @p: The pointer to a Python
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t sz;
	Py_ssize_t ac;
	PyObject *itm;
	Py_ssize_t count;

	sz = PyList_Size(p);
	ac = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");

	printf("[*] Size of the Python List = %zd\n", sz);

	printf("[*] Allocated = %zd\n", ac);

	count = 0;
	while (count < sz)
	{
		itm = PyList_GetItem(p, count);

		printf("Element %zd: %s\n", count, Py_TYPE(itm)->tp_name);
		count++;
	}
}

/**
 * print_python_bytes - Start of function that prints
 *			basic information about Python bytes objects
 * @p: The pointer to a Python
 */
void print_python_bytes(PyObject *p)
{

	Py_ssize_t sz;
	char *str;
	Py_ssize_t count;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");

		return;
	}
	sz = PyBytes_Size(p);

	str = PyBytes_AsString(p);

	printf("  size: %zd\n", sz);

	printf("  trying string: %s\n", str);

	printf("  first %zd bytes:", sz + 1 > 10 ? 10 : sz + 1);

	count = 0;

	while (count < sz + 1 && count < 10)
	{
		printf(" %02x", str[count]);

		count++;
	}

	printf("\n");
}
