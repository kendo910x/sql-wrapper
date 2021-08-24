From python

ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
RUN pip install Flask
RUN pip install mysqlclient
COPY app.py /
CMD python -u /app.py
