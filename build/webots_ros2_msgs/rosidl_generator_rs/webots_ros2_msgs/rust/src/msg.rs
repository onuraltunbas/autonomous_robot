#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to webots_ros2_msgs__msg__BoolStamped

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct BoolStamped {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub data: bool,

}



impl Default for BoolStamped {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::BoolStamped::default())
  }
}

impl rosidl_runtime_rs::Message for BoolStamped {
  type RmwMsg = super::msg::rmw::BoolStamped;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        data: msg.data,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      data: msg.data,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      data: msg.data,
    }
  }
}


// Corresponds to webots_ros2_msgs__msg__FloatStamped

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct FloatStamped {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub data: f64,

}



impl Default for FloatStamped {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::FloatStamped::default())
  }
}

impl rosidl_runtime_rs::Message for FloatStamped {
  type RmwMsg = super::msg::rmw::FloatStamped;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        data: msg.data,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      data: msg.data,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      data: msg.data,
    }
  }
}


// Corresponds to webots_ros2_msgs__msg__StringStamped

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct StringStamped {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub data: std::string::String,

}



impl Default for StringStamped {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::StringStamped::default())
  }
}

impl rosidl_runtime_rs::Message for StringStamped {
  type RmwMsg = super::msg::rmw::StringStamped;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        data: msg.data.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        data: msg.data.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      data: msg.data.to_string(),
    }
  }
}


// Corresponds to webots_ros2_msgs__msg__CameraRecognitionObject

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CameraRecognitionObject {

    // This member is not documented.
    #[allow(missing_docs)]
    pub id: i32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: geometry_msgs::msg::PoseStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub bbox: vision_msgs::msg::BoundingBox2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub colors: Vec<std_msgs::msg::ColorRGBA>,


    // This member is not documented.
    #[allow(missing_docs)]
    pub model: std::string::String,

}



impl Default for CameraRecognitionObject {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::CameraRecognitionObject::default())
  }
}

impl rosidl_runtime_rs::Message for CameraRecognitionObject {
  type RmwMsg = super::msg::rmw::CameraRecognitionObject;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        id: msg.id,
        pose: geometry_msgs::msg::PoseStamped::into_rmw_message(std::borrow::Cow::Owned(msg.pose)).into_owned(),
        bbox: vision_msgs::msg::BoundingBox2D::into_rmw_message(std::borrow::Cow::Owned(msg.bbox)).into_owned(),
        colors: msg.colors
          .into_iter()
          .map(|elem| std_msgs::msg::ColorRGBA::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
        model: msg.model.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      id: msg.id,
        pose: geometry_msgs::msg::PoseStamped::into_rmw_message(std::borrow::Cow::Borrowed(&msg.pose)).into_owned(),
        bbox: vision_msgs::msg::BoundingBox2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.bbox)).into_owned(),
        colors: msg.colors
          .iter()
          .map(|elem| std_msgs::msg::ColorRGBA::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
        model: msg.model.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      id: msg.id,
      pose: geometry_msgs::msg::PoseStamped::from_rmw_message(msg.pose),
      bbox: vision_msgs::msg::BoundingBox2D::from_rmw_message(msg.bbox),
      colors: msg.colors
          .into_iter()
          .map(std_msgs::msg::ColorRGBA::from_rmw_message)
          .collect(),
      model: msg.model.to_string(),
    }
  }
}


// Corresponds to webots_ros2_msgs__msg__CameraRecognitionObjects

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CameraRecognitionObjects {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub objects: Vec<super::msg::CameraRecognitionObject>,

}



impl Default for CameraRecognitionObjects {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::CameraRecognitionObjects::default())
  }
}

impl rosidl_runtime_rs::Message for CameraRecognitionObjects {
  type RmwMsg = super::msg::rmw::CameraRecognitionObjects;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        objects: msg.objects
          .into_iter()
          .map(|elem| super::msg::CameraRecognitionObject::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        objects: msg.objects
          .iter()
          .map(|elem| super::msg::CameraRecognitionObject::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      objects: msg.objects
          .into_iter()
          .map(super::msg::CameraRecognitionObject::from_rmw_message)
          .collect(),
    }
  }
}


// Corresponds to webots_ros2_msgs__msg__UrdfRobot

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct UrdfRobot {

    // This member is not documented.
    #[allow(missing_docs)]
    pub name: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub urdf_path: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub robot_description: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub relative_path_prefix: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub translation: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub rotation: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub normal: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub box_collision: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub init_pos: std::string::String,

}



impl Default for UrdfRobot {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::UrdfRobot::default())
  }
}

impl rosidl_runtime_rs::Message for UrdfRobot {
  type RmwMsg = super::msg::rmw::UrdfRobot;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        name: msg.name.as_str().into(),
        urdf_path: msg.urdf_path.as_str().into(),
        robot_description: msg.robot_description.as_str().into(),
        relative_path_prefix: msg.relative_path_prefix.as_str().into(),
        translation: msg.translation.as_str().into(),
        rotation: msg.rotation.as_str().into(),
        normal: msg.normal,
        box_collision: msg.box_collision,
        init_pos: msg.init_pos.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        name: msg.name.as_str().into(),
        urdf_path: msg.urdf_path.as_str().into(),
        robot_description: msg.robot_description.as_str().into(),
        relative_path_prefix: msg.relative_path_prefix.as_str().into(),
        translation: msg.translation.as_str().into(),
        rotation: msg.rotation.as_str().into(),
      normal: msg.normal,
      box_collision: msg.box_collision,
        init_pos: msg.init_pos.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      name: msg.name.to_string(),
      urdf_path: msg.urdf_path.to_string(),
      robot_description: msg.robot_description.to_string(),
      relative_path_prefix: msg.relative_path_prefix.to_string(),
      translation: msg.translation.to_string(),
      rotation: msg.rotation.to_string(),
      normal: msg.normal,
      box_collision: msg.box_collision,
      init_pos: msg.init_pos.to_string(),
    }
  }
}


// Corresponds to webots_ros2_msgs__msg__PenInkProperties
/// Set the ink properties of a pen device.
/// See https://www.cyberbotics.com/doc/reference/pen#wb_pen_set_ink_color for more details

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct PenInkProperties {
    /// Ink color in hexadecimal format
    pub color: i32,

    /// Ink density (similar in context to alpha of rgba)
    pub density: f32,

}



impl Default for PenInkProperties {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::PenInkProperties::default())
  }
}

impl rosidl_runtime_rs::Message for PenInkProperties {
  type RmwMsg = super::msg::rmw::PenInkProperties;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        color: msg.color,
        density: msg.density,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      color: msg.color,
      density: msg.density,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      color: msg.color,
      density: msg.density,
    }
  }
}


