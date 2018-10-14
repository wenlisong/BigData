hadoop jar hadoop-streaming-3.1.1.jar \
-input ml-20m/ratings.csv \
-output ./output \
-mapper 'python mapper.py' -file mapper.py \
-reducer 'python reducer.py' -file reducer.py