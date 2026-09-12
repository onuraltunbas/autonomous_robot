// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from webots_ros2_msgs:srv/SpawnUrdfRobot.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "webots_ros2_msgs/srv/spawn_urdf_robot.hpp"


#ifndef WEBOTS_ROS2_MSGS__SRV__DETAIL__SPAWN_URDF_ROBOT__TRAITS_HPP_
#define WEBOTS_ROS2_MSGS__SRV__DETAIL__SPAWN_URDF_ROBOT__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "webots_ros2_msgs/srv/detail/spawn_urdf_robot__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'robot'
#include "webots_ros2_msgs/msg/detail/urdf_robot__traits.hpp"

namespace webots_ros2_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SpawnUrdfRobot_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot
  {
    out << "robot: ";
    to_flow_style_yaml(msg.robot, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SpawnUrdfRobot_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: robot
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot:\n";
    to_block_style_yaml(msg.robot, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SpawnUrdfRobot_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, webots_ros2_msgs::srv::SpawnUrdfRobot_Request>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).robot);
}

}  // namespace srv

}  // namespace webots_ros2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<webots_ros2_msgs::srv::SpawnUrdfRobot_Request>()
{
  return "webots_ros2_msgs::srv::SpawnUrdfRobot_Request";
}

template<>
constexpr const char * name<webots_ros2_msgs::srv::SpawnUrdfRobot_Request>()
{
  return "webots_ros2_msgs/srv/SpawnUrdfRobot_Request";
}

template<>
struct has_fixed_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Request>
  : std::integral_constant<bool, has_fixed_size<webots_ros2_msgs::msg::UrdfRobot>::value> {};

template<>
struct has_bounded_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Request>
  : std::integral_constant<bool, has_bounded_size<webots_ros2_msgs::msg::UrdfRobot>::value> {};

template<>
struct is_message<webots_ros2_msgs::srv::SpawnUrdfRobot_Request>
  : std::true_type {};

template<>
struct MessageTraits<webots_ros2_msgs::srv::SpawnUrdfRobot_Request>
{
  static constexpr std::size_t member_count = 1;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "robot",
  };
};

}  // namespace rosidl_generator_traits

namespace webots_ros2_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SpawnUrdfRobot_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SpawnUrdfRobot_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SpawnUrdfRobot_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, webots_ros2_msgs::srv::SpawnUrdfRobot_Response>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).success);
}

}  // namespace srv

}  // namespace webots_ros2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<webots_ros2_msgs::srv::SpawnUrdfRobot_Response>()
{
  return "webots_ros2_msgs::srv::SpawnUrdfRobot_Response";
}

template<>
constexpr const char * name<webots_ros2_msgs::srv::SpawnUrdfRobot_Response>()
{
  return "webots_ros2_msgs/srv/SpawnUrdfRobot_Response";
}

template<>
struct has_fixed_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<webots_ros2_msgs::srv::SpawnUrdfRobot_Response>
  : std::true_type {};

template<>
struct MessageTraits<webots_ros2_msgs::srv::SpawnUrdfRobot_Response>
{
  static constexpr std::size_t member_count = 1;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "success",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace webots_ros2_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SpawnUrdfRobot_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SpawnUrdfRobot_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SpawnUrdfRobot_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, webots_ros2_msgs::srv::SpawnUrdfRobot_Event>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).info,
    std::forward<T>(msg).request,
    std::forward<T>(msg).response);
}

}  // namespace srv

}  // namespace webots_ros2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<webots_ros2_msgs::srv::SpawnUrdfRobot_Event>()
{
  return "webots_ros2_msgs::srv::SpawnUrdfRobot_Event";
}

template<>
constexpr const char * name<webots_ros2_msgs::srv::SpawnUrdfRobot_Event>()
{
  return "webots_ros2_msgs/srv/SpawnUrdfRobot_Event";
}

template<>
struct has_fixed_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Event>
  : std::integral_constant<bool, has_bounded_size<service_msgs::msg::ServiceEventInfo>::value && has_bounded_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Request>::value && has_bounded_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Response>::value> {};

template<>
struct is_message<webots_ros2_msgs::srv::SpawnUrdfRobot_Event>
  : std::true_type {};

template<>
struct MessageTraits<webots_ros2_msgs::srv::SpawnUrdfRobot_Event>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "info",
    "request",
    "response",
  };
};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<webots_ros2_msgs::srv::SpawnUrdfRobot>()
{
  return "webots_ros2_msgs::srv::SpawnUrdfRobot";
}

template<>
constexpr const char * name<webots_ros2_msgs::srv::SpawnUrdfRobot>()
{
  return "webots_ros2_msgs/srv/SpawnUrdfRobot";
}

template<>
struct has_fixed_size<webots_ros2_msgs::srv::SpawnUrdfRobot>
  : std::integral_constant<
    bool,
    has_fixed_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Request>::value &&
    has_fixed_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Response>::value
  >
{
};

template<>
struct has_bounded_size<webots_ros2_msgs::srv::SpawnUrdfRobot>
  : std::integral_constant<
    bool,
    has_bounded_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Request>::value &&
    has_bounded_size<webots_ros2_msgs::srv::SpawnUrdfRobot_Response>::value
  >
{
};

template<>
struct is_service<webots_ros2_msgs::srv::SpawnUrdfRobot>
  : std::true_type
{
};

template<>
struct is_service_request<webots_ros2_msgs::srv::SpawnUrdfRobot_Request>
  : std::true_type
{
};

template<>
struct is_service_response<webots_ros2_msgs::srv::SpawnUrdfRobot_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // WEBOTS_ROS2_MSGS__SRV__DETAIL__SPAWN_URDF_ROBOT__TRAITS_HPP_
