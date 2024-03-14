import os
import subprocess

def run_protoc(proto_file, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    command = ["protoc", "--java_out=" + output_dir, proto_file]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error running protoc: {stderr.decode()}")
    else:
        print(f"Successfully ran protoc on {proto_file}: {stdout.decode()}")

# Replace these with your actual .proto file and output directory
run_protoc("./proto/message.proto", "./grpc/src/main/java/grpc")