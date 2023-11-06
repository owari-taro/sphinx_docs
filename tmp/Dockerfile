FROM ubuntu:22.04
RUN apt update && apt -y upgrade && apt install -y wget
WORKDIR /app
RUN mkdir ./miniconda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ./miniconda3/miniconda.sh \
    && bash ./miniconda3/miniconda.sh -b -u -p ./miniconda3 \
    && rm -rf ./miniconda3/miniconda.sh
ENV PATH=./miniconda3/bin:$PATH 
RUN  ./miniconda3/bin/conda init bash && ./miniconda3/bin/conda init zsh
RUN  conda install -c conda-forge gdal requests 
RUN conda update --all
COPY . .
CMD ["python" , "script.py"]


#/bin/sh /app/miniconda3/bin/conda 