# generated from rosidl_generator_py/resource/_idl.py.em
# with input from webots_ros2_msgs:msg/CameraRecognitionObject.idl
# generated code does not contain a copyright notice

from __future__ import annotations

import collections.abc
import os
import typing

import rosidl_pycommon.interface_base_classes

if typing.TYPE_CHECKING:
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
ros_python_check_fields = os.getenv('ROS_PYTHON_CHECK_FIELDS', default='')


if typing.TYPE_CHECKING:
    import geometry_msgs.msg  # noqa: E402, I100, I201, I300
    import std_msgs.msg  # noqa: E402, I100, I201, I300
    import vision_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CameraRecognitionObject(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'CameraRecognitionObject'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CameraRecognitionObjectConstants(typing.TypedDict):
        pass

    __constants: CameraRecognitionObjectConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('webots_ros2_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'webots_ros2_msgs.msg.CameraRecognitionObject')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__camera_recognition_object
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__camera_recognition_object
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__camera_recognition_object
            cls._TYPE_SUPPORT = module.type_support_msg__msg__camera_recognition_object
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__camera_recognition_object

            from geometry_msgs.msg import PoseStamped
            if PoseStamped._TYPE_SUPPORT is None:
                PoseStamped.__import_type_support__()

            from std_msgs.msg import ColorRGBA
            if ColorRGBA._TYPE_SUPPORT is None:
                ColorRGBA.__import_type_support__()

            from vision_msgs.msg import BoundingBox2D
            if BoundingBox2D._TYPE_SUPPORT is None:
                BoundingBox2D.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CameraRecognitionObject(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_CameraRecognitionObject):
    """Message class 'CameraRecognitionObject'."""

    __slots__ = [
        '_id',
        '_pose',
        '_bbox',
        '_colors',
        '_model',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'id': 'int32',
        'pose': 'geometry_msgs/PoseStamped',
        'bbox': 'vision_msgs/BoundingBox2D',
        'colors': 'sequence<std_msgs/ColorRGBA>',
        'model': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['vision_msgs', 'msg'], 'BoundingBox2D'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'ColorRGBA')),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 id: typing.Optional[int] = None,  # noqa: E501, A002
                 pose: typing.Optional[geometry_msgs.msg.PoseStamped] = None,  # noqa: E501
                 bbox: typing.Optional[vision_msgs.msg.BoundingBox2D] = None,  # noqa: E501
                 colors: typing.Optional[collections.abc.Sequence[std_msgs.msg.ColorRGBA]] = None,  # noqa: E501
                 model: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.id = id if id is not None else int()
        from geometry_msgs.msg import PoseStamped
        self.pose = pose if pose is not None else PoseStamped()
        from vision_msgs.msg import BoundingBox2D
        self.bbox = bbox if bbox is not None else BoundingBox2D()
        self.colors = colors if colors is not None else []
        self.model = model if model is not None else str()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    from rosidl_buffer import Buffer as _RosidlBuffer
                    if not isinstance(field, _RosidlBuffer):
                        if self._check_fields:
                            assert fieldstr.startswith('array(')
                        prefix = "array('X', "
                        suffix = ')'
                        fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CameraRecognitionObject):
            return False
        if self.id != other.id:
            return False
        if self.pose != other.pose:
            return False
        if self.bbox != other.bbox:
            return False
        if self.colors != other.colors:
            return False
        if self.model != other.model:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property  # noqa: A003
    def id(self) -> int:  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value: int) -> None:  # noqa: A003

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'id' field must be of type 'int'"
                assert value >= -2147483648 and value < 2147483648, \
                    "The 'id' field must be an integer in [-2147483648, 2147483647]"

        self._id = value

    @builtins.property
    def pose(self) -> geometry_msgs.msg.PoseStamped:
        """Message field 'pose'."""
        return self._pose

    @pose.setter
    def pose(self, value: geometry_msgs.msg.PoseStamped) -> None:
        from geometry_msgs.msg import PoseStamped

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, PoseStamped), \
                    "The 'pose' field must be a sub message of type 'PoseStamped'"

        self._pose = value

    @builtins.property
    def bbox(self) -> vision_msgs.msg.BoundingBox2D:
        """Message field 'bbox'."""
        return self._bbox

    @bbox.setter
    def bbox(self, value: vision_msgs.msg.BoundingBox2D) -> None:
        from vision_msgs.msg import BoundingBox2D

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, BoundingBox2D), \
                    "The 'bbox' field must be a sub message of type 'BoundingBox2D'"

        self._bbox = value

    @builtins.property
    def colors(self) -> typing.Annotated[typing.Any, list[std_msgs.msg.ColorRGBA]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'colors'."""
        return self._colors

    @colors.setter
    def colors(self, value: collections.abc.Sequence[std_msgs.msg.ColorRGBA]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from std_msgs.msg import ColorRGBA

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, ColorRGBA) for v in value) and
                     True), \
                    "The 'colors' field must be sequence and each value of type 'ColorRGBA'"

        if isinstance(value, list):
            self._colors = value
            return
        self._colors = list(value)

    @builtins.property
    def model(self) -> str:
        """Message field 'model'."""
        return self._model

    @model.setter
    def model(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'model' field must be of type 'str'"

        self._model = value
