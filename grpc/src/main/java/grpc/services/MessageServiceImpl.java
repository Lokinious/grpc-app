package grpc.services;

import message.Message;
import message.MessageResponse;
import message.MessageServiceGrpc;
import io.grpc.stub.StreamObserver;

public class MessageServiceImpl extends MessageServiceGrpc.MessageServiceImplBase {
    @Override
    public void sendMessage(Message request, StreamObserver<MessageResponse> responseObserver) {
        // Handle the message here. For example, just echo it back:
        MessageResponse response = MessageResponse.newBuilder()
            .setResponseMessage("Received: " + request.getContent())
            .build();

        // Send the response
        responseObserver.onNext(response);

        // Complete the RPC call
        responseObserver.onCompleted();
    }
}