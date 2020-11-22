config = {'datapath':'/home/rqy_local/data/DSB3/stage2/stage2',
          'preprocess_result_path':'./prep_result/',
          'outputfile':'prediction.csv',
          
          'detector_model':'net_detector',
         # 'detector_param':'./training/detector/results/baseline_res18_bs24/100.ckpt',
         'detector_param':'./model/detector.ckpt',
         'classifier_model':'net_classifier',
         # 'classifier_param':'./training/classifier/results/net4/160.ckpt',
         'classifier_param':'./model/classifier_state_dict.ckpt',
         'n_gpu':1,
         'n_worker_preprocessing':None,
         'use_exsiting_preprocessing':True,
         'skip_preprocessing':False,
         'skip_detect':False}
