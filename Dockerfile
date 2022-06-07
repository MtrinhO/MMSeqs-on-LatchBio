#Dockerfile

#(1): Base image / computer to layer functionality on top of. (Debian Linux machine)
FROM http://812206152185.dkr.ecr.us-west-2.amazonaws.com/latch-base:02ab-main

#(2) Install and Copy mmseqs to base computer (bin), makes it executable
RUN curl -L https://github.com/soedinglab/MMseqs2/releases/download/13-45111/mmseqs-linux-ppc64le-power9.tar.gz -o mmseqs-linux-ppc64le-power9.tar.gz &&\
    tar -xvzf mmseqs-linux-ppc64le-power9.tar.gz 

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