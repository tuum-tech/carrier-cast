FROM        ubuntu:xenial
MAINTAINER  tuum-tech

# update and install dependencies
RUN apt-get update && \
	apt-get install -f build-essential autoconf automake autopoint libtool flex bison libncurses5-dev cmake \
					   python3 python3-dev python3-pip libffi-dev \
					   supervisor -y 

RUN pip3 install ipcqueue gevent werkzeug tinyrpc					

ENV SRC_DIR /carrier-cast
ENV RELEASE release-v5.6.0

ADD https://github.com/elastos/Elastos.NET.Carrier.Native.SDK/archive/${RELEASE}.tar.gz ${SRC_DIR}/

WORKDIR ${SRC_DIR}

RUN tar -xzvf ${RELEASE}.tar.gz && \
	mv Elastos.NET.Carrier.Native.SDK-${RELEASE} Elastos.NET.Carrier.Native.SDK

# copy all the files to the container
COPY app/* Elastos.NET.Carrier.Native.SDK/apps/shell/

RUN cd ${SRC_DIR}/Elastos.NET.Carrier.Native.SDK \
		&& mkdir -p build/linux \
		&& cd build/linux \
		&& cmake ../.. && \
		make && \
		make install

RUN mkdir -p /var/log/supervisor /etc/supervisor/conf.d

COPY rpc_helper/* ${SRC_DIR}/
COPY supervisor.conf /etc/supervisor.conf     

# define the port number the container should expose
EXPOSE 5000

CMD ["supervisord", "-c", "/etc/supervisor.conf"]