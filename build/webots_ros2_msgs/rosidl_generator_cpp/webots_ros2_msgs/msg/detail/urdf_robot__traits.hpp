// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from webots_ros2_msgs:msg/UrdfRobot.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "webots_ros2_msgs/msg/urdf_robot.hpp"


#ifndef WEBOTS_ROS2_MSGS__MSG__DETAIL__URDF_ROBOT__TRAITS_HPP_
#define WEBOTS_ROS2_MSGS__MSG__DETAIL__URDF_ROBOT__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "webots_ros2_msgs/msg/detail/urdf_robot__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace webots_ros2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const UrdfRobot & msg,
  std::ostream & out)
{
  out << "{";
  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << ", ";
  }

  // member: urdf_path
  {
    out << "urdf_path: ";
    rosidl_generator_traits::value_to_yaml(msg.urdf_path, out);
    out << ", ";
  }

  // member: robot_description
  {
    out << "robot_description: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_description, out);
    out << ", ";
  }

  // member: relative_path_prefix
  {
    out << "relative_path_prefix: ";
    rosidl_generator_traits::value_to_yaml(msg.relative_path_prefix, out);
    out << ", ";
  }

  // member: translation
  {
    out << "translation: ";
    rosidl_generator_traits::value_to_yaml(msg.translation, out);
    out << ", ";
  }

  // member: rotation
  {
    out << "rotation: ";
    rosidl_generator_traits::value_to_yaml(msg.rotation, out);
    out << ", ";
  }

  // member: normal
  {
    out << "normal: ";
    rosidl_generator_traits::value_to_yaml(msg.normal, out);
    out << ", ";
  }

  // member: box_collision
  {
    out << "box_collision: ";
    rosidl_generator_traits::value_to_yaml(msg.box_collision, out);
    out << ", ";
  }

  // member: init_pos
  {
    out << "init_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.init_pos, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const UrdfRobot & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }

  // member: urdf_path
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "urdf_path: ";
    rosidl_generator_traits::value_to_yaml(msg.urdf_path, out);
    out << "\n";
  }

  // member: robot_description
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_description: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_description, out);
    out << "\n";
  }

  // member: relative_path_prefix
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "relative_path_prefix: ";
    rosidl_generator_traits::value_to_yaml(msg.relative_path_prefix, out);
    out << "\n";
  }

  // member: translation
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "translation: ";
    rosidl_generator_traits::value_to_yaml(msg.translation, out);
    out << "\n";
  }

  // member: rotation
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rotation: ";
    rosidl_generator_traits::value_to_yaml(msg.rotation, out);
    out << "\n";
  }

  // member: normal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "normal: ";
    rosidl_generator_traits::value_to_yaml(msg.normal, out);
    out << "\n";
  }

  // member: box_collision
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "box_collision: ";
    rosidl_generator_traits::value_to_yaml(msg.box_collision, out);
    out << "\n";
  }

  // member: init_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "init_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.init_pos, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const UrdfRobot & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, webots_ros2_msgs::msg::UrdfRobot>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).name,
    std::forward<T>(msg).urdf_path,
    std::forward<T>(msg).robot_description,
    std::forward<T>(msg).relative_path_prefix,
    std::forward<T>(msg).translation,
    std::forward<T>(msg).rotation,
    std::forward<T>(msg).normal,
    std::forward<T>(msg).box_collision,
    std::forward<T>(msg).init_pos);
}

}  // namespace msg

}  // namespace webots_ros2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<webots_ros2_msgs::msg::UrdfRobot>()
{
  return "webots_ros2_msgs::msg::UrdfRobot";
}

template<>
constexpr const char * name<webots_ros2_msgs::msg::UrdfRobot>()
{
  return "webots_ros2_msgs/msg/UrdfRobot";
}

template<>
struct has_fixed_size<webots_ros2_msgs::msg::UrdfRobot>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<webots_ros2_msgs::msg::UrdfRobot>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<webots_ros2_msgs::msg::UrdfRobot>
  : std::true_type {};

template<>
struct MessageTraits<webots_ros2_msgs::msg::UrdfRobot>
{
  static constexpr std::size_t member_count = 9;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "name",
    "urdf_path",
    "robot_description",
    "relative_path_prefix",
    "translation",
    "rotation",
    "normal",
    "box_collision",
    "init_pos",
  };
};

}  // namespace rosidl_generator_traits

#endif  // WEBOTS_ROS2_MSGS__MSG__DETAIL__URDF_ROBOT__TRAITS_HPP_
