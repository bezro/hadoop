INPUT="/collaborative_filtering/data/input"
OUTPUT="/collaborative_filtering/data/output"
HADOOP_STREAMING_PATH="${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar"
FILENAME="ratings.csv"

hdfs dfs -rm -r /collaborative_filtering
hdfs dfs -copyFromLocal /collaborative_filtering /
hdfs dfs -rm -r ${OUTPUT}

echo "------Запускаем 1-ю часть задания------"
hadoop jar ${HADOOP_STREAMING_PATH} \
-D mapred.map.tasks=4 \
-D mapred.reduce.tasks=8 \
-files collaborative_filtering/src \
-mapper "python3 src/mapper_1.py" \
-reducer "python3 src/reducer_1.py" \
-input ${INPUT}/${FILENAME} \
-output ${OUTPUT}/stage_1

echo "------Запускаем 2-ю часть задания------"
hadoop jar ${HADOOP_STREAMING_PATH} \
-D mapred.map.tasks=4 \
-D mapred.reduce.tasks=8 \
-files collaborative_filtering/src \
-mapper "python3 src/mapper_2.py" \
-reducer "python3 src/reducer_2.py" \
-input ${OUTPUT}/stage_1/part-00000,\
${OUTPUT}/stage_1/part-00001,\
${OUTPUT}/stage_1/part-00002,\
${OUTPUT}/stage_1/part-00003,\
${OUTPUT}/stage_1/part-00004,\
${OUTPUT}/stage_1/part-00005,\
${OUTPUT}/stage_1/part-00006,\
${OUTPUT}/stage_1/part-00007 \
-output ${OUTPUT}/stage_2

echo "------Запускаем 3-ю часть задания------"
hadoop jar ${HADOOP_STREAMING_PATH} \
-D mapred.map.tasks=4 \
-D mapred.reduce.tasks=8 \
-files collaborative_filtering/src \
-D mapreduce.map.memory.mb=1024 \
-D mapreduce.reduce.memory.mb=2048 \
-mapper "python3 src/mapper_3.py" \
-reducer "python3 src/reducer_3.py" \
-input ${OUTPUT}/stage_2/part-00000,\
${OUTPUT}/stage_2/part-00001,\
${OUTPUT}/stage_2/part-00002,\
${OUTPUT}/stage_2/part-00003,\
${OUTPUT}/stage_2/part-00004,\
${OUTPUT}/stage_2/part-00005,\
${OUTPUT}/stage_2/part-00006,\
${OUTPUT}/stage_2/part-00007,\
${INPUT}/${FILENAME} \
-output ${OUTPUT}/stage_3

echo "------Запускаем 4-ю часть задания------"
hadoop jar ${HADOOP_STREAMING_PATH} \
-D mapred.map.tasks=4 \
-D mapred.reduce.tasks=8 \
-files collaborative_filtering/src \
-D mapreduce.map.memory.mb=2048 \
-D mapreduce.reduce.memory.mb=2048 \
-mapper "python3 src/mapper_4.py" \
-reducer "python3 src/reducer_4.py" \
-input ${OUTPUT}/stage_3/part-00000,\
${OUTPUT}/stage_3/part-00001,\
${OUTPUT}/stage_3/part-00002,\
${OUTPUT}/stage_3/part-00003,\
${OUTPUT}/stage_3/part-00004,\
${OUTPUT}/stage_3/part-00005,\
${OUTPUT}/stage_3/part-00006,\
${OUTPUT}/stage_3/part-00007 \
-output ${OUTPUT}/stage_4

echo "------Запускаем 5-ю часть задания------"
hadoop jar ${HADOOP_STREAMING_PATH} \
-D mapred.map.tasks=4 \
-D mapred.reduce.tasks=8 \
-files collaborative_filtering/src,${INPUT}/movies.csv \
-D mapreduce.map.memory.mb=2048 \
-D mapreduce.reduce.memory.mb=2048 \
-mapper "python3 src/mapper_5.py" \
-reducer "python3 src/reducer_5.py" \
-input ${OUTPUT}/stage_4/part-00000,\
${OUTPUT}/stage_4/part-00001,\
${OUTPUT}/stage_4/part-00002,\
${OUTPUT}/stage_4/part-00003,\
${OUTPUT}/stage_4/part-00004,\
${OUTPUT}/stage_4/part-00005,\
${OUTPUT}/stage_4/part-00006,\
${OUTPUT}/stage_4/part-00007,\
${INPUT}/${FILENAME} \
-output ${OUTPUT}/final

rm -r ${OUTPUT}
mkdir ${OUTPUT}
hdfs dfs -copyToLocal ${OUTPUT}/final ${OUTPUT}