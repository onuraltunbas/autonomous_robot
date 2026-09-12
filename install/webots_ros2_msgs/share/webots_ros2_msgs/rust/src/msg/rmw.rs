#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__BoolStamped() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__msg__BoolStamped__init(msg: *mut BoolStamped) -> bool;
    fn webots_ros2_msgs__msg__BoolStamped__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<BoolStamped>, size: usize) -> bool;
    fn webots_ros2_msgs__msg__BoolStamped__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<BoolStamped>);
    fn webots_ros2_msgs__msg__BoolStamped__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<BoolStamped>, out_seq: *mut rosidl_runtime_rs::Sequence<BoolStamped>) -> bool;
}

// Corresponds to webots_ros2_msgs__msg__BoolStamped
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct BoolStamped {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub data: bool,

}



impl Default for BoolStamped {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__msg__BoolStamped__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__msg__BoolStamped__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for BoolStamped {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__BoolStamped__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__BoolStamped__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__BoolStamped__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for BoolStamped {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for BoolStamped where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/msg/BoolStamped";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__BoolStamped() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__FloatStamped() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__msg__FloatStamped__init(msg: *mut FloatStamped) -> bool;
    fn webots_ros2_msgs__msg__FloatStamped__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<FloatStamped>, size: usize) -> bool;
    fn webots_ros2_msgs__msg__FloatStamped__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<FloatStamped>);
    fn webots_ros2_msgs__msg__FloatStamped__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<FloatStamped>, out_seq: *mut rosidl_runtime_rs::Sequence<FloatStamped>) -> bool;
}

// Corresponds to webots_ros2_msgs__msg__FloatStamped
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct FloatStamped {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub data: f64,

}



impl Default for FloatStamped {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__msg__FloatStamped__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__msg__FloatStamped__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for FloatStamped {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__FloatStamped__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__FloatStamped__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__FloatStamped__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for FloatStamped {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for FloatStamped where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/msg/FloatStamped";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__FloatStamped() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__StringStamped() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__msg__StringStamped__init(msg: *mut StringStamped) -> bool;
    fn webots_ros2_msgs__msg__StringStamped__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<StringStamped>, size: usize) -> bool;
    fn webots_ros2_msgs__msg__StringStamped__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<StringStamped>);
    fn webots_ros2_msgs__msg__StringStamped__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<StringStamped>, out_seq: *mut rosidl_runtime_rs::Sequence<StringStamped>) -> bool;
}

// Corresponds to webots_ros2_msgs__msg__StringStamped
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct StringStamped {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub data: rosidl_runtime_rs::String,

}



impl Default for StringStamped {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__msg__StringStamped__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__msg__StringStamped__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for StringStamped {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__StringStamped__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__StringStamped__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__StringStamped__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for StringStamped {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for StringStamped where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/msg/StringStamped";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__StringStamped() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__CameraRecognitionObject() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__msg__CameraRecognitionObject__init(msg: *mut CameraRecognitionObject) -> bool;
    fn webots_ros2_msgs__msg__CameraRecognitionObject__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<CameraRecognitionObject>, size: usize) -> bool;
    fn webots_ros2_msgs__msg__CameraRecognitionObject__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<CameraRecognitionObject>);
    fn webots_ros2_msgs__msg__CameraRecognitionObject__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<CameraRecognitionObject>, out_seq: *mut rosidl_runtime_rs::Sequence<CameraRecognitionObject>) -> bool;
}

// Corresponds to webots_ros2_msgs__msg__CameraRecognitionObject
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CameraRecognitionObject {

    // This member is not documented.
    #[allow(missing_docs)]
    pub id: i32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: geometry_msgs::msg::rmw::PoseStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub bbox: vision_msgs::msg::rmw::BoundingBox2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub colors: rosidl_runtime_rs::Sequence<std_msgs::msg::rmw::ColorRGBA>,


    // This member is not documented.
    #[allow(missing_docs)]
    pub model: rosidl_runtime_rs::String,

}



impl Default for CameraRecognitionObject {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__msg__CameraRecognitionObject__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__msg__CameraRecognitionObject__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for CameraRecognitionObject {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__CameraRecognitionObject__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__CameraRecognitionObject__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__CameraRecognitionObject__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for CameraRecognitionObject {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for CameraRecognitionObject where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/msg/CameraRecognitionObject";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__CameraRecognitionObject() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__CameraRecognitionObjects() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__msg__CameraRecognitionObjects__init(msg: *mut CameraRecognitionObjects) -> bool;
    fn webots_ros2_msgs__msg__CameraRecognitionObjects__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<CameraRecognitionObjects>, size: usize) -> bool;
    fn webots_ros2_msgs__msg__CameraRecognitionObjects__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<CameraRecognitionObjects>);
    fn webots_ros2_msgs__msg__CameraRecognitionObjects__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<CameraRecognitionObjects>, out_seq: *mut rosidl_runtime_rs::Sequence<CameraRecognitionObjects>) -> bool;
}

// Corresponds to webots_ros2_msgs__msg__CameraRecognitionObjects
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CameraRecognitionObjects {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub objects: rosidl_runtime_rs::Sequence<super::super::msg::rmw::CameraRecognitionObject>,

}



impl Default for CameraRecognitionObjects {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__msg__CameraRecognitionObjects__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__msg__CameraRecognitionObjects__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for CameraRecognitionObjects {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__CameraRecognitionObjects__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__CameraRecognitionObjects__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__CameraRecognitionObjects__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for CameraRecognitionObjects {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for CameraRecognitionObjects where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/msg/CameraRecognitionObjects";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__CameraRecognitionObjects() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__UrdfRobot() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__msg__UrdfRobot__init(msg: *mut UrdfRobot) -> bool;
    fn webots_ros2_msgs__msg__UrdfRobot__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<UrdfRobot>, size: usize) -> bool;
    fn webots_ros2_msgs__msg__UrdfRobot__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<UrdfRobot>);
    fn webots_ros2_msgs__msg__UrdfRobot__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<UrdfRobot>, out_seq: *mut rosidl_runtime_rs::Sequence<UrdfRobot>) -> bool;
}

// Corresponds to webots_ros2_msgs__msg__UrdfRobot
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct UrdfRobot {

    // This member is not documented.
    #[allow(missing_docs)]
    pub name: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub urdf_path: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub robot_description: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub relative_path_prefix: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub translation: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub rotation: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub normal: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub box_collision: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub init_pos: rosidl_runtime_rs::String,

}



impl Default for UrdfRobot {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__msg__UrdfRobot__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__msg__UrdfRobot__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for UrdfRobot {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__UrdfRobot__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__UrdfRobot__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__UrdfRobot__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for UrdfRobot {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for UrdfRobot where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/msg/UrdfRobot";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__UrdfRobot() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__PenInkProperties() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__msg__PenInkProperties__init(msg: *mut PenInkProperties) -> bool;
    fn webots_ros2_msgs__msg__PenInkProperties__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<PenInkProperties>, size: usize) -> bool;
    fn webots_ros2_msgs__msg__PenInkProperties__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<PenInkProperties>);
    fn webots_ros2_msgs__msg__PenInkProperties__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<PenInkProperties>, out_seq: *mut rosidl_runtime_rs::Sequence<PenInkProperties>) -> bool;
}

// Corresponds to webots_ros2_msgs__msg__PenInkProperties
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// Set the ink properties of a pen device.
/// See https://www.cyberbotics.com/doc/reference/pen#wb_pen_set_ink_color for more details

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct PenInkProperties {
    /// Ink color in hexadecimal format
    pub color: i32,

    /// Ink density (similar in context to alpha of rgba)
    pub density: f32,

}



impl Default for PenInkProperties {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__msg__PenInkProperties__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__msg__PenInkProperties__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for PenInkProperties {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__PenInkProperties__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__PenInkProperties__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__msg__PenInkProperties__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for PenInkProperties {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for PenInkProperties where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/msg/PenInkProperties";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__msg__PenInkProperties() }
  }
}


