# Import the base image 
FROM python:3.8

RUN pip install fairseq


RUN pip install transformers



#RUN pip install parlai

# Copy requirements
COPY requirements.txt /requirements.txt

# Install requirements
RUN pip install -r /requirements.txt
RUN pip install 'git+https://github.com/rsennrich/subword-nmt.git#egg=subword-nmt'

# Copy files
COPY . /blender_issd/

# Set working directory
WORKDIR /blender_issd/



# Setup parlai
RUN python setup.py develop

# Run chatbot
CMD parlai interactive_web --host 0.0.0.0 --port 8081 -mf zoo:blenderbot2/blenderbot2_400M/model --task blended_skill_talk --query-generator-model-file zoo:sea/bart_sq_gen/model --search_server $HTTP --knowledge-access-method $METHOD --memory-key full_text


 