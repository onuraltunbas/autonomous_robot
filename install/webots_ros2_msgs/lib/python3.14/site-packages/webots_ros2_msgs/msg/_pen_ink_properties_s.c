// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from webots_ros2_msgs:msg/PenInkProperties.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "webots_ros2_msgs/msg/detail/pen_ink_properties__struct.h"
#include "webots_ros2_msgs/msg/detail/pen_ink_properties__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool webots_ros2_msgs__msg__pen_ink_properties__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
    if (class_attr == NULL) {
      return false;
    }
    PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
    if (name_attr == NULL) {
      Py_DECREF(class_attr);
      return false;
    }
    PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
    if (module_attr == NULL) {
      Py_DECREF(name_attr);
      Py_DECREF(class_attr);
      return false;
    }

    // PyUnicode_1BYTE_DATA is just a cast
    assert(strncmp("webots_ros2_msgs.msg._pen_ink_properties", (char *)PyUnicode_1BYTE_DATA(module_attr), 40) == 0);
    assert(strncmp("PenInkProperties", (char *)PyUnicode_1BYTE_DATA(name_attr), 16) == 0);

    Py_DECREF(module_attr);
    Py_DECREF(name_attr);
    Py_DECREF(class_attr);
  }
  webots_ros2_msgs__msg__PenInkProperties * ros_message = _ros_message;
  {  // color
    PyObject * field = PyObject_GetAttrString(_pymsg, "color");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->color = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // density
    PyObject * field = PyObject_GetAttrString(_pymsg, "density");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->density = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * webots_ros2_msgs__msg__pen_ink_properties__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of PenInkProperties */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("webots_ros2_msgs.msg._pen_ink_properties");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "PenInkProperties");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  webots_ros2_msgs__msg__PenInkProperties * ros_message = (webots_ros2_msgs__msg__PenInkProperties *)raw_ros_message;
  {  // color
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->color);
    {
      int rc = PyObject_SetAttrString(_pymessage, "color", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // density
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->density);
    {
      int rc = PyObject_SetAttrString(_pymessage, "density", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
