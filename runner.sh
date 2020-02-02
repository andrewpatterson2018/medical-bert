#!/bin/bash
python medicalbert/ --experiment_name alsentzer1e5 --learning_rate 0.00001 --tokenizer /home/apatterson/pretrained_bert_tf/biobert_pretrain_output_disch_100000 --pretrained_model /home/apatterson/pretrained_bert_tf/biobert_pretrain_output_disch_100000 --train --eval --classifier bert-general;
python medicalbert/ --experiment_name general1e5 --learning_rate 0.00001 --train --eval --classifier bert-general;
python medicalbert/ --experiment_name random1e5 --learning_rate 0.00001  --train --eval --classifier bert-random;

python medicalbert/ --experiment_name alsentzer-mean-pool-tokens --learning_rate 0.00001 --tokenizer /home/apatterson/pretrained_bert_tf/biobert_pretrain_output_disch_100000 --pretrained_model /home/apatterson/pretrained_bert_tf/biobert_pretrain_output_disch_100000 --train --eval --classifier bert-mean-pool;
