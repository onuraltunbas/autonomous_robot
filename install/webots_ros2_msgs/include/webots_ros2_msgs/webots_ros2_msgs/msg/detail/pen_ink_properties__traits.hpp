// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from webots_ros2_msgs:msg/PenInkProperties.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "webots_ros2_msgs/msg/pen_ink_properties.hpp"


#ifndef WEBOTS_ROS2_MSGS__MSG__DETAIL__PEN_INK_PROPERTIES__TRAITS_HPP_
#define WEBOTS_ROS2_MSGS__MSG__DETAIL__PEN_INK_PROPERTIES__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "webots_ros2_msgs/msg/detail/pen_ink_properties__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace webots_ros2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const PenInkProperties & msg,
  std::ostream & out)
{
  out << "{";
  // member: color
  {
    out << "color: ";
    rosidl_generator_traits::value_to_yaml(msg.color, out);
    out << ", ";
  }

  // member: density
  {
    out << "density: ";
    rosidl_generator_traits::value_to_yaml(msg.density, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PenInkProperties & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: color
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "color: ";
    rosidl_generator_traits::value_to_yaml(msg.color, out);
    out << "\n";
  }

  // member: density
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "density: ";
    rosidl_generator_traits::value_to_yaml(msg.density, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PenInkProperties & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, webots_ros2_msgs::msg::PenInkProperties>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).color,
    std::forward<T>(msg).density);
}

}  // namespace msg

}  // namespace webots_ros2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<webots_ros2_msgs::msg::PenInkProperties>()
{
  return "webots_ros2_msgs::msg::PenInkProperties";
}

template<>
constexpr const char * name<webots_ros2_msgs::msg::PenInkProperties>()
{
  return "webots_ros2_msgs/msg/PenInkProperties";
}

template<>
struct has_fixed_size<webots_ros2_msgs::msg::PenInkProperties>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<webots_ros2_msgs::msg::PenInkProperties>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<webots_ros2_msgs::msg::PenInkProperties>
  : std::true_type {};

template<>
struct MessageTraits<webots_ros2_msgs::msg::PenInkProperties>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "color",
    "density",
  };
};

}  // namespace rosidl_generator_traits

#endif  // WEBOTS_ROS2_MSGS__MSG__DETAIL__PEN_INK_PROPERTIES__TRAITS_HPP_
