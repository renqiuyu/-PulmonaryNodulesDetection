#!/bin/bash
set -e

# python prepare.py
cd detector
eps=100
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python main.py --model res18 -b 32 --epochs $eps --save-dir baseline_res18_bs24
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python main.py --model res18 -b 32 --resume baseline_res18_bs24/$eps.ckpt --test 1
cp results/res18/$eps.ckpt ../../model/detector.ckpt


cd classifier
python adapt_ckpt.py --model1  net_detector_3 --model2  net_classifier_3  --resume /home/rqy_local/codebase/DSB2017/training/detector/results/baseline_res18_bs24/100.ckpt
CUDA_VISIBLE_DEVICES=0,1,2,3 python main.py --model1  net_detector_3 --model2  net_classifier_3 -b 12 -b2 4 --save-dir net3 --resume ./results/start.ckpt --start-epoch 30 --epochs 130
CUDA_VISIBLE_DEVICES=0,1,2,3 python main.py --model1  net_detector_3 --model2  net_classifier_4 -b 16 -b2 4 --save-dir net4 --resume ./results/net3/130.ckpt --freeze_batchnorm 1 --start-epoch 121
cp results/net4/160.ckpt ../../model/classifier.ckpt
