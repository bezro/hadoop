# Полагаем, что мы сейчас в папке collaborative_filtering (корневой папке проекта)

sudo docker cp ./ namenode://collaborative_filtering

sudo docker exec -it namenode bash /collaborative_filtering/run_hadoop.sh

mkdir data/output
rm -r data/output/final
sudo docker cp namenode://collaborative_filtering/data/output/final data/output
sudo chmod -R 777 data/output
