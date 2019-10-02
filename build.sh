#!/bin/bash

python -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. --python_grpc_out=. proto/grpc_madmin/*.proto
