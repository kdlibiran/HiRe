# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles/HiRe_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/HiRe_autogen.dir/ParseCache.txt"
  "HiRe_autogen"
  )
endif()
