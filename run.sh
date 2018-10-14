/research/ksleung5/wlsong/hadoop/hadoop-3.1.1/bin/hadoop jar hadoop-streaming-3.1.1.jar \
 -input ./ml-20m/ratings.csv \
 -output ./output \
 -mapper 'python mapper.py' \
 -reducer 'python reducer.py' \
 -file ./mapper.py \
 -file ./reducer.py
