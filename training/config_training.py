config = {'stage1_data_path':'/home/rqy_local/data/DSB3/stage1/stage1',
          'luna_raw':'/home/rqy_local/data/LUNA16', 
          'luna_segment':'/home/rqy_local/data/LUNA16/seg-lungs-LUNA16',
          
          'luna_data':'/home/rqy_local/data/luna/allset',
          'preprocess_result_path':'/home/rqy_local/data/preprocess/',       
          
          'luna_abbr':'./detector/labels/shorter.csv',
          'luna_label':'./detector/labels/lunaqualified.csv',
          'stage1_annos_path':['./detector/labels/label_job5.csv',
                './detector/labels/label_job4_2.csv',
                './detector/labels/label_job4_1.csv',
                './detector/labels/label_job0.csv',
                './detector/labels/label_qualified.csv'],
          'bbox_path':'../detector/results/res18_mylabel/bbox/',
          'preprocessing_backend':'python'
         }
