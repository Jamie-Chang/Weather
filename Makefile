protofile:
	echo "Making the proto files"
	python -m grpc_tools.protoc -I. \
		--python_out=client_example \
		--python_grpc_out=client_example \
		proto/weather.proto
	python -m grpc_tools.protoc -I. \
		--python_out=weather_service \
		--python_grpc_out=weather_service \
		proto/weather.proto