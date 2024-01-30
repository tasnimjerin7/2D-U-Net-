
cfg = dict()
cfg['crop_coord']            =  {'x0':42, 'x1':194,
                                 'y0':29, 'y1':221,
                                 'z0':2,  'z1':146}
cfg['data_dir']              = '/path/to/data/'

cfg['table_data_shape']      =  (cfg["crop_coord"]['z1']-cfg["crop_coord"]['z0'],
                                 cfg["crop_coord"]['y1']-cfg["crop_coord"]['y0'], 
                                 cfg["crop_coord"]['x1']-cfg["crop_coord"]['x0'])

cfg['data_channels']         = 4
cfg['save_data_dir']         = './data/'

cfg['save_dir']        = './save/'
cfg['k_fold']                = 5
cfg['hdf5_dir']              = './data/data.hdf5'
cfg['brains_idx_dir']        = './data/fold0_idx.npy'
cfg['view']                  = 'axial'

cfg['batch_size']            = 16
cfg['val_batch_size']        = 32

cfg['hor_flip']              = True
cfg['ver_flip']              = True
cfg['rotation_range']        = 0
cfg['zoom_range']            = 0.
cfg['epochs']                = 100
cfg['lr']                    = 0.008
cfg['multiprocessing']       = False 
cfg['workers']               = 1
cfg['modified_unet']         = True 
cfg['levels']                = 3
cfg['start_chs']             = 64
cfg['load_model_dir']        = None 