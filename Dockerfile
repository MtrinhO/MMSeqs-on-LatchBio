#Dockerfile

#(1): Base image / computer to layer functionality on top of. (Debian Linux machine)
FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/latch-base:02ab-main

#(2) Install and Copy mmseqs to base computer (bin), makes it executable
RUN curl -L https://mmseqs.com/latest/mmseqs-linux-avx2.tar.gz && tar xvfz mmseqs-linux-avx2.tar.gz && export PATH=$(pwd)/mmseqs/bin/:$PATH

COPY mmseqs/bin/mmseqs /bin/mmseqs

# STOP HERE:
# The following lines are needed to ensure your build environement works
# correctly with latch.
COPY wf /root/wf

#Dependencies for Latch
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
RUN  sed -i 's/latch/wf/g' flytekit.config
RUN python3 -m pip install --upgrade latch
WORKDIR /root