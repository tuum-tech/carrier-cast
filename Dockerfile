FROM        ubuntu:xenial
MAINTAINER  alex

# set a directory for the app
WORKDIR /home

# copy all the files to the container
COPY . .

# update and install dependencies
RUN         apt-get update \
		&& apt-get install -y \
		 	build-essential \
			autoconf \
			automake \
			autopoint \
			libtool \
			flex \
			bison \
			libncurses5-dev \
			libncursesw5-dev \
			cmake \
                && apt-get install -y \
                    software-properties-common \
                    wget \
                && add-apt-repository -y ppa:ubuntu-toolchain-r/test \
                && apt-get update \
                && apt-get install -y \
                    make \
                    git \
                    curl \
                    vim \
                    vim-gnome \
                && apt-get install -y cmake=3.5.1-1ubuntu3 \
                && apt-get install -y \
                    gcc-4.9 g++-4.9 gcc-4.9-base \
                    gcc-4.8 g++-4.8 gcc-4.8-base \
                    gcc-4.7 g++-4.7 gcc-4.7-base \
                    gcc-4.6 g++-4.6 gcc-4.6-base \
                && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100 \
                && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 100 \
		&& apt-get install -y automake \
			libffi-dev \
			libssl-dev \
		 	autotools-dev \
		 	libtool \
		 	python3-pip \
		&& apt-get install -y nano\
		&& pip3 install ipcqueue \
		&& pip3 install gevent \
		&& pip3 install werkzeug \
		&& pip3 install tinyrpc \
		&& cd /home/Elastos.NET.Carrier.Native.SDK/build \
		&& mkdir linux \
		&& cd linux \
		&& cmake ../.. \
		&& make \
		&& make install \
		&& make dist


# define the port number the container should expose
EXPOSE 5000

# CMD ["/home/Elastos.NET.Carrier.Native.SDK/build/linux/apps/shell/elashell",""]
# CMD ["python3", "/home/Elastos.NET.Carrier.Native.SDK/apps/shell/rpc_server.py"]

