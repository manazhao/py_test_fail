load("@build_stack_rules_proto//python:python_proto_library.bzl", "python_proto_library")

package(
    default_visibility = ["//:__subpackages__"],
)

proto_library(
    name = "test_proto",
    srcs = ["test.proto"],
)

python_proto_library(
    name = "python_test_proto",
    deps = [":test_proto"],
)

py_library(
    name = "lib",
    srcs = ["lib.py"],
    deps = [":python_test_proto"],
)

py_test(
    name = "lib_test",
    srcs = ["lib_test.py"],
    deps = [":lib"],
)
