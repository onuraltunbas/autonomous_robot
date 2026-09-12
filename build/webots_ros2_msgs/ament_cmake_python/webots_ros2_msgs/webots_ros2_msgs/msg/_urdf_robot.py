# generated from rosidl_generator_py/resource/_idl.py.em
# with input from webots_ros2_msgs:msg/UrdfRobot.idl
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


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_UrdfRobot(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'UrdfRobot'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class UrdfRobotConstants(typing.TypedDict):
        pass

    __constants: UrdfRobotConstants = {
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
                'webots_ros2_msgs.msg.UrdfRobot')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__urdf_robot
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__urdf_robot
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__urdf_robot
            cls._TYPE_SUPPORT = module.type_support_msg__msg__urdf_robot
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__urdf_robot

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class UrdfRobot(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_UrdfRobot):
    """Message class 'UrdfRobot'."""

    __slots__ = [
        '_name',
        '_urdf_path',
        '_robot_description',
        '_relative_path_prefix',
        '_translation',
        '_rotation',
        '_normal',
        '_box_collision',
        '_init_pos',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'name': 'string',
        'urdf_path': 'string',
        'robot_description': 'string',
        'relative_path_prefix': 'string',
        'translation': 'string',
        'rotation': 'string',
        'normal': 'boolean',
        'box_collision': 'boolean',
        'init_pos': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 name: typing.Optional[str] = None,  # noqa: E501
                 urdf_path: typing.Optional[str] = None,  # noqa: E501
                 robot_description: typing.Optional[str] = None,  # noqa: E501
                 relative_path_prefix: typing.Optional[str] = None,  # noqa: E501
                 translation: typing.Optional[str] = None,  # noqa: E501
                 rotation: typing.Optional[str] = None,  # noqa: E501
                 normal: typing.Optional[bool] = None,  # noqa: E501
                 box_collision: typing.Optional[bool] = None,  # noqa: E501
                 init_pos: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.name = name if name is not None else str()
        self.urdf_path = urdf_path if urdf_path is not None else str()
        self.robot_description = robot_description if robot_description is not None else str()
        self.relative_path_prefix = relative_path_prefix if relative_path_prefix is not None else str()
        self.translation = translation if translation is not None else str()
        self.rotation = rotation if rotation is not None else str()
        self.normal = normal if normal is not None else bool()
        self.box_collision = box_collision if box_collision is not None else bool()
        self.init_pos = init_pos if init_pos is not None else str()

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
        if not isinstance(other, UrdfRobot):
            return False
        if self.name != other.name:
            return False
        if self.urdf_path != other.urdf_path:
            return False
        if self.robot_description != other.robot_description:
            return False
        if self.relative_path_prefix != other.relative_path_prefix:
            return False
        if self.translation != other.translation:
            return False
        if self.rotation != other.rotation:
            return False
        if self.normal != other.normal:
            return False
        if self.box_collision != other.box_collision:
            return False
        if self.init_pos != other.init_pos:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def name(self) -> str:
        """Message field 'name'."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'name' field must be of type 'str'"

        self._name = value

    @builtins.property
    def urdf_path(self) -> str:
        """Message field 'urdf_path'."""
        return self._urdf_path

    @urdf_path.setter
    def urdf_path(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'urdf_path' field must be of type 'str'"

        self._urdf_path = value

    @builtins.property
    def robot_description(self) -> str:
        """Message field 'robot_description'."""
        return self._robot_description

    @robot_description.setter
    def robot_description(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'robot_description' field must be of type 'str'"

        self._robot_description = value

    @builtins.property
    def relative_path_prefix(self) -> str:
        """Message field 'relative_path_prefix'."""
        return self._relative_path_prefix

    @relative_path_prefix.setter
    def relative_path_prefix(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'relative_path_prefix' field must be of type 'str'"

        self._relative_path_prefix = value

    @builtins.property
    def translation(self) -> str:
        """Message field 'translation'."""
        return self._translation

    @translation.setter
    def translation(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'translation' field must be of type 'str'"

        self._translation = value

    @builtins.property
    def rotation(self) -> str:
        """Message field 'rotation'."""
        return self._rotation

    @rotation.setter
    def rotation(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'rotation' field must be of type 'str'"

        self._rotation = value

    @builtins.property
    def normal(self) -> bool:
        """Message field 'normal'."""
        return self._normal

    @normal.setter
    def normal(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'normal' field must be of type 'bool'"

        self._normal = value

    @builtins.property
    def box_collision(self) -> bool:
        """Message field 'box_collision'."""
        return self._box_collision

    @box_collision.setter
    def box_collision(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'box_collision' field must be of type 'bool'"

        self._box_collision = value

    @builtins.property
    def init_pos(self) -> str:
        """Message field 'init_pos'."""
        return self._init_pos

    @init_pos.setter
    def init_pos(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'init_pos' field must be of type 'str'"

        self._init_pos = value
