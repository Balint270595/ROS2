// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from turtlebot3_msgs:srv/Dqn.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "turtlebot3_msgs/srv/dqn.h"


#ifndef TURTLEBOT3_MSGS__SRV__DETAIL__DQN__STRUCT_H_
#define TURTLEBOT3_MSGS__SRV__DETAIL__DQN__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Dqn in the package turtlebot3_msgs.
typedef struct turtlebot3_msgs__srv__Dqn_Request
{
  uint8_t action;
  bool init;
} turtlebot3_msgs__srv__Dqn_Request;

// Struct for a sequence of turtlebot3_msgs__srv__Dqn_Request.
typedef struct turtlebot3_msgs__srv__Dqn_Request__Sequence
{
  turtlebot3_msgs__srv__Dqn_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot3_msgs__srv__Dqn_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'state'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/Dqn in the package turtlebot3_msgs.
typedef struct turtlebot3_msgs__srv__Dqn_Response
{
  rosidl_runtime_c__float__Sequence state;
  float reward;
  bool done;
} turtlebot3_msgs__srv__Dqn_Response;

// Struct for a sequence of turtlebot3_msgs__srv__Dqn_Response.
typedef struct turtlebot3_msgs__srv__Dqn_Response__Sequence
{
  turtlebot3_msgs__srv__Dqn_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot3_msgs__srv__Dqn_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  turtlebot3_msgs__srv__Dqn_Event__request__MAX_SIZE = 1
};
// response
enum
{
  turtlebot3_msgs__srv__Dqn_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/Dqn in the package turtlebot3_msgs.
typedef struct turtlebot3_msgs__srv__Dqn_Event
{
  service_msgs__msg__ServiceEventInfo info;
  turtlebot3_msgs__srv__Dqn_Request__Sequence request;
  turtlebot3_msgs__srv__Dqn_Response__Sequence response;
} turtlebot3_msgs__srv__Dqn_Event;

// Struct for a sequence of turtlebot3_msgs__srv__Dqn_Event.
typedef struct turtlebot3_msgs__srv__Dqn_Event__Sequence
{
  turtlebot3_msgs__srv__Dqn_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot3_msgs__srv__Dqn_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TURTLEBOT3_MSGS__SRV__DETAIL__DQN__STRUCT_H_
