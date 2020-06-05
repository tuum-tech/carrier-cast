FROM        ubuntu:xenial
MAINTAINER  tuum-tech

# update and install dependencies
RUN apt-get update && \
	apt-get install -f build-essential autoconf automake autopoint libtool flex bison libncurses5-dev cmake \
					   python3 python3-dev python3-pip libffi-dev -y 

RUN pip3 install ipcqueue gevent werkzeug tinyrpc					

# copy all the files to the container
COPY Elastos.NET.Carrier.Native.SDK Elastos.NET.Carrier.Native.SDK

RUN cd Elastos.NET.Carrier.Native.SDK \
		&& mkdir -p build/linux \
		&& cd build/linux \
		&& cmake ../.. \
		&& make \
		&& make install

COPY rpc_server.py rpc_server.py
COPY client_queue_reader.py client_queue_reader.py

# define the port number the container should expose
EXPOSE 5000