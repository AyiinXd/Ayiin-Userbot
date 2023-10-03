#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#
# Izzy Ganteng

FROM ayiinxd/ayiin:xd

RUN git clone -b Ayiin-Userbot https://github.com/AyiinXd/Ayiin-Userbot /home/ayiinuserbot/ \
    && chmod 777 /home/ayiinuserbot \
    && mkdir /home/ayiinuserbot/bin/

#COPY ./sample.env ./.env* /home/ayiinuserbot/

WORKDIR /home/ayiinuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
