#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to webots_ros2_msgs__srv__EmitterSendString_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct EmitterSendString_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub value: std::string::String,

}



impl Default for EmitterSendString_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::EmitterSendString_Request::default())
  }
}

impl rosidl_runtime_rs::Message for EmitterSendString_Request {
  type RmwMsg = super::srv::rmw::EmitterSendString_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        value: msg.value.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        value: msg.value.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      value: msg.value.to_string(),
    }
  }
}


// Corresponds to webots_ros2_msgs__srv__EmitterSendString_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct EmitterSendString_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub result: i64,

}



impl Default for EmitterSendString_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::EmitterSendString_Response::default())
  }
}

impl rosidl_runtime_rs::Message for EmitterSendString_Response {
  type RmwMsg = super::srv::rmw::EmitterSendString_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        result: msg.result,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      result: msg.result,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      result: msg.result,
    }
  }
}


// Corresponds to webots_ros2_msgs__srv__GetBool_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetBool_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub ask: bool,

}



impl Default for GetBool_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetBool_Request::default())
  }
}

impl rosidl_runtime_rs::Message for GetBool_Request {
  type RmwMsg = super::srv::rmw::GetBool_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        ask: msg.ask,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      ask: msg.ask,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      ask: msg.ask,
    }
  }
}


// Corresponds to webots_ros2_msgs__srv__GetBool_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetBool_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub value: bool,

}



impl Default for GetBool_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetBool_Response::default())
  }
}

impl rosidl_runtime_rs::Message for GetBool_Response {
  type RmwMsg = super::srv::rmw::GetBool_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        value: msg.value,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      value: msg.value,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      value: msg.value,
    }
  }
}


// Corresponds to webots_ros2_msgs__srv__SetString_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetString_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub value: std::string::String,

}



impl Default for SetString_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SetString_Request::default())
  }
}

impl rosidl_runtime_rs::Message for SetString_Request {
  type RmwMsg = super::srv::rmw::SetString_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        value: msg.value.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        value: msg.value.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      value: msg.value.to_string(),
    }
  }
}


// Corresponds to webots_ros2_msgs__srv__SetString_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetString_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for SetString_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SetString_Response::default())
  }
}

impl rosidl_runtime_rs::Message for SetString_Response {
  type RmwMsg = super::srv::rmw::SetString_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
    }
  }
}


// Corresponds to webots_ros2_msgs__srv__SpawnNodeFromString_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpawnNodeFromString_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub data: std::string::String,

}



impl Default for SpawnNodeFromString_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SpawnNodeFromString_Request::default())
  }
}

impl rosidl_runtime_rs::Message for SpawnNodeFromString_Request {
  type RmwMsg = super::srv::rmw::SpawnNodeFromString_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        data: msg.data.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        data: msg.data.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      data: msg.data.to_string(),
    }
  }
}


// Corresponds to webots_ros2_msgs__srv__SpawnNodeFromString_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpawnNodeFromString_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for SpawnNodeFromString_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SpawnNodeFromString_Response::default())
  }
}

impl rosidl_runtime_rs::Message for SpawnNodeFromString_Response {
  type RmwMsg = super::srv::rmw::SpawnNodeFromString_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
    }
  }
}


// Corresponds to webots_ros2_msgs__srv__SpawnUrdfRobot_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpawnUrdfRobot_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub robot: super::msg::UrdfRobot,

}



impl Default for SpawnUrdfRobot_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SpawnUrdfRobot_Request::default())
  }
}

impl rosidl_runtime_rs::Message for SpawnUrdfRobot_Request {
  type RmwMsg = super::srv::rmw::SpawnUrdfRobot_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        robot: super::msg::UrdfRobot::into_rmw_message(std::borrow::Cow::Owned(msg.robot)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        robot: super::msg::UrdfRobot::into_rmw_message(std::borrow::Cow::Borrowed(&msg.robot)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      robot: super::msg::UrdfRobot::from_rmw_message(msg.robot),
    }
  }
}


// Corresponds to webots_ros2_msgs__srv__SpawnUrdfRobot_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpawnUrdfRobot_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for SpawnUrdfRobot_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SpawnUrdfRobot_Response::default())
  }
}

impl rosidl_runtime_rs::Message for SpawnUrdfRobot_Response {
  type RmwMsg = super::srv::rmw::SpawnUrdfRobot_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
    }
  }
}






#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__webots_ros2_msgs__srv__EmitterSendString() -> *const std::ffi::c_void;
}

// Corresponds to webots_ros2_msgs__srv__EmitterSendString
#[allow(missing_docs, non_camel_case_types)]
pub struct EmitterSendString;

impl rosidl_runtime_rs::Service for EmitterSendString {
    type Request = EmitterSendString_Request;
    type Response = EmitterSendString_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__webots_ros2_msgs__srv__EmitterSendString() }
    }
}




#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__webots_ros2_msgs__srv__GetBool() -> *const std::ffi::c_void;
}

// Corresponds to webots_ros2_msgs__srv__GetBool
#[allow(missing_docs, non_camel_case_types)]
pub struct GetBool;

impl rosidl_runtime_rs::Service for GetBool {
    type Request = GetBool_Request;
    type Response = GetBool_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__webots_ros2_msgs__srv__GetBool() }
    }
}




#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__webots_ros2_msgs__srv__SetString() -> *const std::ffi::c_void;
}

// Corresponds to webots_ros2_msgs__srv__SetString
#[allow(missing_docs, non_camel_case_types)]
pub struct SetString;

impl rosidl_runtime_rs::Service for SetString {
    type Request = SetString_Request;
    type Response = SetString_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__webots_ros2_msgs__srv__SetString() }
    }
}




#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__webots_ros2_msgs__srv__SpawnNodeFromString() -> *const std::ffi::c_void;
}

// Corresponds to webots_ros2_msgs__srv__SpawnNodeFromString
#[allow(missing_docs, non_camel_case_types)]
pub struct SpawnNodeFromString;

impl rosidl_runtime_rs::Service for SpawnNodeFromString {
    type Request = SpawnNodeFromString_Request;
    type Response = SpawnNodeFromString_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__webots_ros2_msgs__srv__SpawnNodeFromString() }
    }
}




#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__webots_ros2_msgs__srv__SpawnUrdfRobot() -> *const std::ffi::c_void;
}

// Corresponds to webots_ros2_msgs__srv__SpawnUrdfRobot
#[allow(missing_docs, non_camel_case_types)]
pub struct SpawnUrdfRobot;

impl rosidl_runtime_rs::Service for SpawnUrdfRobot {
    type Request = SpawnUrdfRobot_Request;
    type Response = SpawnUrdfRobot_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__webots_ros2_msgs__srv__SpawnUrdfRobot() }
    }
}


