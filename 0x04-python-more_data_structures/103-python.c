nclude <Python.h>

/**
 * print_python_list - Python lists
 *   * @p:pointer
 *    */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i = 0;
	PyObject *item;
	
	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);
	
	while (i < size)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		i++;
	}
}

/**
 * print_python_bytes - Prints basic information
 * @p: pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i = 0;
	char *str;

	printf("[.] bytes object info\n");
	
	
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", size + 1 > 10 ? 10 : size + 1);
	while (i < size + 1 && i < 10)
	{
		printf(" %02x", (unsigned char)str[i]);
		i++;
	}
	printf("\n");
}
