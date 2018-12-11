class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'hmdb51_dataset':
            # folder that contains class labels
            root_dir = '/home/mosthusne_jahan/project_most/hmdb51_dataset'

            # Save preprocess data into output_dir
            output_dir = '/home/mosthusne_jahan/project_most/hmdb51_preprocess'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        #training, if pretrained true
        #return '/home/mosthusne_jahan/project_most-new/c3d-pretrained.pth'
        #testing
        return '/Users/mosthusnejahan/Desktop/project_most/c3d-pretrained.pth'
