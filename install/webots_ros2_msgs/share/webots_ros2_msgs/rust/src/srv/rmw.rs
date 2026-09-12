#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__EmitterSendString_Request() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__srv__EmitterSendString_Request__init(msg: *mut EmitterSendString_Request) -> bool;
    fn webots_ros2_msgs__srv__EmitterSendString_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<EmitterSendString_Request>, size: usize) -> bool;
    fn webots_ros2_msgs__srv__EmitterSendString_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<EmitterSendString_Request>);
    fn webots_ros2_msgs__srv__EmitterSendString_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<EmitterSendString_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<EmitterSendString_Request>) -> bool;
}

// Corresponds to webots_ros2_msgs__srv__EmitterSendString_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct EmitterSendString_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub value: rosidl_runtime_rs::String,

}



impl Default for EmitterSendString_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__srv__EmitterSendString_Request__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__srv__EmitterSendString_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for EmitterSendString_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__EmitterSendString_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__EmitterSendString_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__EmitterSendString_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for EmitterSendString_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for EmitterSendString_Request where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/srv/EmitterSendString_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__EmitterSendString_Request() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__EmitterSendString_Response() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__srv__EmitterSendString_Response__init(msg: *mut EmitterSendString_Response) -> bool;
    fn webots_ros2_msgs__srv__EmitterSendString_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<EmitterSendString_Response>, size: usize) -> bool;
    fn webots_ros2_msgs__srv__EmitterSendString_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<EmitterSendString_Response>);
    fn webots_ros2_msgs__srv__EmitterSendString_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<EmitterSendString_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<EmitterSendString_Response>) -> bool;
}

// Corresponds to webots_ros2_msgs__srv__EmitterSendString_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct EmitterSendString_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub result: i64,

}



impl Default for EmitterSendString_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__srv__EmitterSendString_Response__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__srv__EmitterSendString_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for EmitterSendString_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__EmitterSendString_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__EmitterSendString_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__EmitterSendString_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for EmitterSendString_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for EmitterSendString_Response where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/srv/EmitterSendString_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__EmitterSendString_Response() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__GetBool_Request() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__srv__GetBool_Request__init(msg: *mut GetBool_Request) -> bool;
    fn webots_ros2_msgs__srv__GetBool_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetBool_Request>, size: usize) -> bool;
    fn webots_ros2_msgs__srv__GetBool_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetBool_Request>);
    fn webots_ros2_msgs__srv__GetBool_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetBool_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<GetBool_Request>) -> bool;
}

// Corresponds to webots_ros2_msgs__srv__GetBool_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetBool_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub ask: bool,

}



impl Default for GetBool_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__srv__GetBool_Request__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__srv__GetBool_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetBool_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__GetBool_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__GetBool_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__GetBool_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetBool_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetBool_Request where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/srv/GetBool_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__GetBool_Request() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__GetBool_Response() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__srv__GetBool_Response__init(msg: *mut GetBool_Response) -> bool;
    fn webots_ros2_msgs__srv__GetBool_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetBool_Response>, size: usize) -> bool;
    fn webots_ros2_msgs__srv__GetBool_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetBool_Response>);
    fn webots_ros2_msgs__srv__GetBool_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetBool_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<GetBool_Response>) -> bool;
}

// Corresponds to webots_ros2_msgs__srv__GetBool_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetBool_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub value: bool,

}



impl Default for GetBool_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__srv__GetBool_Response__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__srv__GetBool_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetBool_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__GetBool_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__GetBool_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__GetBool_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetBool_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetBool_Response where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/srv/GetBool_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__GetBool_Response() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SetString_Request() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__srv__SetString_Request__init(msg: *mut SetString_Request) -> bool;
    fn webots_ros2_msgs__srv__SetString_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SetString_Request>, size: usize) -> bool;
    fn webots_ros2_msgs__srv__SetString_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SetString_Request>);
    fn webots_ros2_msgs__srv__SetString_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SetString_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<SetString_Request>) -> bool;
}

// Corresponds to webots_ros2_msgs__srv__SetString_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetString_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub value: rosidl_runtime_rs::String,

}



impl Default for SetString_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__srv__SetString_Request__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__srv__SetString_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SetString_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SetString_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SetString_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SetString_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SetString_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SetString_Request where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/srv/SetString_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SetString_Request() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SetString_Response() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__srv__SetString_Response__init(msg: *mut SetString_Response) -> bool;
    fn webots_ros2_msgs__srv__SetString_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SetString_Response>, size: usize) -> bool;
    fn webots_ros2_msgs__srv__SetString_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SetString_Response>);
    fn webots_ros2_msgs__srv__SetString_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SetString_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<SetString_Response>) -> bool;
}

// Corresponds to webots_ros2_msgs__srv__SetString_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetString_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for SetString_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__srv__SetString_Response__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__srv__SetString_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SetString_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SetString_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SetString_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SetString_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SetString_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SetString_Response where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/srv/SetString_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SetString_Response() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SpawnNodeFromString_Request() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__srv__SpawnNodeFromString_Request__init(msg: *mut SpawnNodeFromString_Request) -> bool;
    fn webots_ros2_msgs__srv__SpawnNodeFromString_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SpawnNodeFromString_Request>, size: usize) -> bool;
    fn webots_ros2_msgs__srv__SpawnNodeFromString_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SpawnNodeFromString_Request>);
    fn webots_ros2_msgs__srv__SpawnNodeFromString_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SpawnNodeFromString_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<SpawnNodeFromString_Request>) -> bool;
}

// Corresponds to webots_ros2_msgs__srv__SpawnNodeFromString_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpawnNodeFromString_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub data: rosidl_runtime_rs::String,

}



impl Default for SpawnNodeFromString_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__srv__SpawnNodeFromString_Request__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__srv__SpawnNodeFromString_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SpawnNodeFromString_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnNodeFromString_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnNodeFromString_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnNodeFromString_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SpawnNodeFromString_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SpawnNodeFromString_Request where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/srv/SpawnNodeFromString_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SpawnNodeFromString_Request() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SpawnNodeFromString_Response() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__srv__SpawnNodeFromString_Response__init(msg: *mut SpawnNodeFromString_Response) -> bool;
    fn webots_ros2_msgs__srv__SpawnNodeFromString_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SpawnNodeFromString_Response>, size: usize) -> bool;
    fn webots_ros2_msgs__srv__SpawnNodeFromString_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SpawnNodeFromString_Response>);
    fn webots_ros2_msgs__srv__SpawnNodeFromString_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SpawnNodeFromString_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<SpawnNodeFromString_Response>) -> bool;
}

// Corresponds to webots_ros2_msgs__srv__SpawnNodeFromString_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpawnNodeFromString_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for SpawnNodeFromString_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__srv__SpawnNodeFromString_Response__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__srv__SpawnNodeFromString_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SpawnNodeFromString_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnNodeFromString_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnNodeFromString_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnNodeFromString_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SpawnNodeFromString_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SpawnNodeFromString_Response where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/srv/SpawnNodeFromString_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SpawnNodeFromString_Response() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SpawnUrdfRobot_Request() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__srv__SpawnUrdfRobot_Request__init(msg: *mut SpawnUrdfRobot_Request) -> bool;
    fn webots_ros2_msgs__srv__SpawnUrdfRobot_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SpawnUrdfRobot_Request>, size: usize) -> bool;
    fn webots_ros2_msgs__srv__SpawnUrdfRobot_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SpawnUrdfRobot_Request>);
    fn webots_ros2_msgs__srv__SpawnUrdfRobot_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SpawnUrdfRobot_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<SpawnUrdfRobot_Request>) -> bool;
}

// Corresponds to webots_ros2_msgs__srv__SpawnUrdfRobot_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpawnUrdfRobot_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub robot: super::super::msg::rmw::UrdfRobot,

}



impl Default for SpawnUrdfRobot_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__srv__SpawnUrdfRobot_Request__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__srv__SpawnUrdfRobot_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SpawnUrdfRobot_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnUrdfRobot_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnUrdfRobot_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnUrdfRobot_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SpawnUrdfRobot_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SpawnUrdfRobot_Request where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/srv/SpawnUrdfRobot_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SpawnUrdfRobot_Request() }
  }
}


#[link(name = "webots_ros2_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SpawnUrdfRobot_Response() -> *const std::ffi::c_void;
}

#[link(name = "webots_ros2_msgs__rosidl_generator_c")]
extern "C" {
    fn webots_ros2_msgs__srv__SpawnUrdfRobot_Response__init(msg: *mut SpawnUrdfRobot_Response) -> bool;
    fn webots_ros2_msgs__srv__SpawnUrdfRobot_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SpawnUrdfRobot_Response>, size: usize) -> bool;
    fn webots_ros2_msgs__srv__SpawnUrdfRobot_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SpawnUrdfRobot_Response>);
    fn webots_ros2_msgs__srv__SpawnUrdfRobot_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SpawnUrdfRobot_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<SpawnUrdfRobot_Response>) -> bool;
}

// Corresponds to webots_ros2_msgs__srv__SpawnUrdfRobot_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpawnUrdfRobot_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for SpawnUrdfRobot_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !webots_ros2_msgs__srv__SpawnUrdfRobot_Response__init(&mut msg as *mut _) {
        panic!("Call to webots_ros2_msgs__srv__SpawnUrdfRobot_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SpawnUrdfRobot_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnUrdfRobot_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnUrdfRobot_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { webots_ros2_msgs__srv__SpawnUrdfRobot_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SpawnUrdfRobot_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SpawnUrdfRobot_Response where Self: Sized {
  const TYPE_NAME: &'static str = "webots_ros2_msgs/srv/SpawnUrdfRobot_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__webots_ros2_msgs__srv__SpawnUrdfRobot_Response() }
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


