#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

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
 *
 */

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
