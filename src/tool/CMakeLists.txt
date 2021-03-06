# Main CMake file for the Tool!
project( tool )
cmake_minimum_required( VERSION 2.8.3 )

# Make sure we can find the shared files
set( SHARE_DIR "${NBITES_DIR}/src/share/" )
set( MAN_DIR "${NBITES_DIR}/src/man" )
include_directories( ${MAN_DIR} )

# So that we can use find_package commands
set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${SHARE_DIR}/cmake/" )
mark_as_advanced( CMAKE_INSTALL_PREFIX )
mark_as_advanced( CMAKE_TOOLCHAIN_FILE )

set( CMAKE_CXX_FLAGS
  "${CMAKE_CXX_FLAGS} -pthread" )

set( CMAKE_C_FLAGS
  "${CMAKE_CXX_FLAGS}" )

# Enable C++11 features for bhuman
include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
if(COMPILER_SUPPORTS_CXX11)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
elseif(COMPILER_SUPPORTS_CXX0X)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
else()
    message(STATUS "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support. Please use a different C++ compiler.")
endif()

# Option to turn rebuilding our protobuf libs on/off
option( BUILD_PROTOBUF "Rebuild the protobuf libraries." OFF )
if( BUILD_PROTOBUF )
  # Only build them if the user wants to
  include( ${SHARE_DIR}/cmake/BuildProtobuf.cmake )
endif()

include ( ${SHARE_DIR}/cmake/BuildGTest.cmake )

include( ${SHARE_DIR}/cmake/DebugConfig.cmake)


# Configure the debug options
configure_file(
  "${SHARE_DIR}/cmake/DebugConfig.in"
  "${PROJECT_BINARY_DIR}/DebugConfig.h"
)

configure_file(
  "${CMAKE_CURRENT_LIST_DIR}/PathConfig.in"
  "${PROJECT_BINARY_DIR}/PathConfig.h"
)

configure_file(
  "${MAN_DIR}/cmake/RobotConfig.in"
  "${PROJECT_BINARY_DIR}/RobotConfig.h"
)


if (NOT CMAKE_BUILD_TYPE)
  message(STATUS "No build type selected, default to RelWithDebInfo")
  set(CMAKE_BUILD_TYPE "RelWithDebInfo")
endif()


include_directories( ${PROJECT_BINARY_DIR} )
include_directories( ${CMAKE_SOURCE_DIR} )

# Dependencies
find_package( Qt4 REQUIRED )

include( ${QT_USE_FILE} )
add_definitions( ${QT_DEFINITIONS} )

mark_as_advanced( QT_QMAKE_EXECUTABLE )

find_package( PROTOBUF REQUIRED )
include_directories( SYSTEM ${PROTOBUF_INCLUDE_DIR} )

# Our core includes come from here
include_directories( ${SHARE_DIR}/include )

# Compile portals into portals folder
add_subdirectory( ${SHARE_DIR}/portals ${CMAKE_CURRENT_BINARY_DIR}/portals )
include_directories( ${SHARE_DIR}/portals )

# Compile logshare into logshare folder
add_subdirectory( ${SHARE_DIR}/logshare ${CMAKE_CURRENT_BINARY_DIR}/logshare )
include_directories( ${SHARE_DIR}/logshare )

# Compile messages into messages folder
add_subdirectory( ${SHARE_DIR}/messages ${CMAKE_CURRENT_BINARY_DIR}/messages )
include_directories( ${CMAKE_CURRENT_BINARY_DIR}/messages )
include_directories( ${SHARE_DIR}/messages )

# If protobuf libs don't exist yet, make sure they build before man
if( BUILD_PROTOBUF )
add_dependencies(messages protobuf_libs)
endif()

# Man modules that we need to use
include_directories( ${MAN_DIR}/support )
add_subdirectory( ${MAN_DIR}/support ${CMAKE_CURRENT_BINARY_DIR}/man/support)

add_subdirectory( ${MAN_DIR}/balltrack ${CMAKE_CURRENT_BINARY_DIR}/man/balltrack)
add_subdirectory( ${MAN_DIR}/comm ${CMAKE_CURRENT_BINARY_DIR}/man/comm)
add_subdirectory( ${MAN_DIR}/sharedball ${CMAKE_CURRENT_BINARY_DIR}/man/sharedball)
add_subdirectory( ${MAN_DIR}/image ${CMAKE_CURRENT_BINARY_DIR}/man/image)
add_subdirectory( ${MAN_DIR}/localization ${CMAKE_CURRENT_BINARY_DIR}/man/localization)
add_subdirectory( ${MAN_DIR}/vision ${CMAKE_CURRENT_BINARY_DIR}/man/vision)

# Actual subdirectories!
add_subdirectory( ballview )
add_subdirectory( calibrator )
add_subdirectory( colorcreator )
add_subdirectory( common )
add_subdirectory( fieldview )
add_subdirectory( image )
add_subdirectory( logview )
add_subdirectory( playbook )
add_subdirectory( sharedview )
add_subdirectory( sim )
add_subdirectory( unlog )
add_subdirectory( vision_offline )
add_subdirectory( worldview )

## SOURCES ##

# Full QTool
set( tool_srcs main.cpp
  ToolDiagram.cpp
  DataSelector.cpp
  Tool.cpp
  ${MAN_DIR}/DiagramThread.cpp # Needed for worldview
  )

set( tool_headers
  ToolDiagram.h
  DataSelector.h

  Tool.h
)

# LocTool
set( loc_srcs loc_main.cpp
  EmptyTool.cpp
  ToolDiagram.cpp
  DataSelector.cpp
  ${MAN_DIR}/DiagramThread.cpp # Needed for worldview

  LocTool.cpp
  )

set( loc_headers
  EmptyTool.h
  ToolDiagram.h
  DataSelector.h

  LocTool.h
)

# WorldviewTool
set( worldview_srcs worldview_main.cpp
  EmptyTool.cpp
  ToolDiagram.cpp
  DataSelector.cpp
  ${MAN_DIR}/DiagramThread.cpp # Needed for worldview

  WorldviewTool.cpp
  )

set( worldview_headers
  EmptyTool.h
  ToolDiagram.h
  DataSelector.h

  WorldviewTool.h
)

#BallTool
set( ball_srcs ball_main.cpp
  EmptyTool.cpp
  ToolDiagram.cpp
  DataSelector.cpp

  BallTool.cpp
)

set( ball_headers
  EmptyTool.h
  ToolDiagram.h
  DataSelector.h

  BallTool.h
)

# VisionTool
set( vision_srcs vision_main.cpp
  EmptyTool.cpp
  ToolDiagram.cpp
  DataSelector.cpp

  VisionTool.cpp
  )

set( vision_headers
  EmptyTool.h
  ToolDiagram.h
  DataSelector.h

  VisionTool.h
)

# CalibrationTool
set( calibrate_srcs calibrate_main.cpp
  EmptyTool.cpp
  ToolDiagram.cpp
  DataSelector.cpp

  CalibrationTool.cpp
  )

set( calibrate_headers
  EmptyTool.h
  ToolDiagram.h
  DataSelector.h

  CalibrationTool.h
)

# Playbook
set( playbook_srcs playbook_main.cpp

  PlaybookTool.cpp
  )

set( playbook_headers

  PlaybookTool.h
)

# SimTool
set( sim_srcs sim_main.cpp
  EmptyTool.cpp
  ToolDiagram.cpp
  DataSelector.cpp

  SimTool.cpp
  )

set( sim_headers
  EmptyTool.h
  ToolDiagram.h
  DataSelector.h

  SimTool.h
)

set( installer_srcs
  installer_main.cpp
  Installer.cpp
  )

set( installer_headers
  Installer.h
  )

# Qt4 goodness (aka moc the headers)
Qt4_wrap_cpp( tool_headers_moc ${tool_headers} )
Qt4_wrap_cpp( loc_headers_moc ${loc_headers} )
Qt4_wrap_cpp( worldview_headers_moc ${worldview_headers} )
Qt4_wrap_cpp( ball_headers_moc ${ball_headers} )
Qt4_wrap_cpp( vision_headers_moc ${vision_headers} )
Qt4_wrap_cpp( calibrate_headers_moc ${calibrate_headers} )
Qt4_wrap_cpp( playbook_headers_moc ${playbook_headers} )
Qt4_wrap_cpp( sim_headers_moc ${sim_headers} )
Qt4_wrap_cpp( installer_headers_moc ${installer_headers} )

## EXECUTABLES ##

# The QTool executable
add_executable( tool
  ${tool_srcs}
  ${tool_headers_moc} )

target_link_libraries(
  tool
  portals
  messages
  unlog
  logview
  image_display
  image # man image
  vision # man vision
  comm # man comm
  sharedball # man sharedball
  fieldview
  sharedview
  tool_common
  colorcreator
  vision_offline
  worldview
  playbook
  ${QT_LIBRARIES}
  )

# The LocTool executable
add_executable( loc_tool
  ${loc_srcs}
  ${loc_headers_moc} )

target_link_libraries(
  loc_tool
  portals
  messages
  unlog
  image_display
  logview
  sharedball
  sharedview
  fieldview
  worldview
  tool_common
  localization
  ${QT_LIBRARIES}
  )

# The WorldView executable
add_executable( worldview_tool
  ${worldview_srcs}
  ${worldview_headers_moc} )

target_link_libraries(
  worldview_tool
  portals
  messages
  unlog
  image_display
  logview
  # sharedball
  # sharedview
  fieldview
  worldview
  tool_common
  localization
  ${QT_LIBRARIES}
  )

# The BallTool executable
add_executable( ball_tool
  ${ball_srcs}
  ${ball_headers_moc} )

target_link_libraries(
  ball_tool
  portals
  messages
  unlog
  logview
  ballview
  tool_common
  image_display
  balltrack
  ${QT_LIBRARIES}
  )

# The VisionTool executable
add_executable( vision_tool
  ${vision_srcs}
  ${vision_headers_moc} )

target_link_libraries(
  vision_tool
  portals
  messages
  unlog
  logview
  image_display
  image # man image
  fieldview
  sharedview
  tool_common
  colorcreator
  vision_offline
  ${QT_LIBRARIES}
  )

# The CalibrationTool executable
add_executable( calibrate_tool
  ${calibrate_srcs}
  ${calibrate_headers_moc}
)

target_link_libraries(
  calibrate_tool
  portals
  messages
  unlog
  logview
  image_display
  calibrator
  ${QT_LIBRARIES}
)

# The PlaybookTool executable
add_executable( playbook_tool
  ${playbook_srcs}
  ${playbook_headers_moc}
)

target_link_libraries(
  playbook_tool
  playbook
  ${QT_LIBRARIES}
)

# The SimTool executable
add_executable( sim_tool
  ${sim_srcs}
  ${sim_headers_moc}
)

target_link_libraries(
  sim_tool
  unlog
  logview
  image_display
  portals
  messages
  visionsim
  ${QT_LIBRARIES}
)

# The InstallerTool executable
add_executable( installer_tool
  ${installer_srcs}
  ${installer_headers_moc}
)

target_link_libraries(
  installer_tool
  ${QT_LIBRARIES}
)

