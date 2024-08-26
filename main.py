import syng_bts_imports.python.Experiments_new as syng_bts

syng_bts.PilotExperiment(dataname = "SKCMPositive_4", pilot_size = [100],
                model = "VAE1-10", batch_frac = 0.1, 
                learning_rate = 0.0005, pre_model = None,
                epoch = None,  off_aug = None, early_stop_num = 30,
                AE_head_num = 2, Gaussian_head_num = 9)

