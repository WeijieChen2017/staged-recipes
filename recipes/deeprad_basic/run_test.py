import tensorflow
import keras
import nibabel
import seaborn

# def install(package):
#     if hasattr(pip, 'main'):
#         pip.main(['install', package])
#     else:
#         pip._internal.main(['install', package])
# 
# # Example
# if __name__ == '__main__':
#     install('argh')

from pip._internal import main as pipmain
pipmain(['install', 'git+https://github.com/keras-team/keras-contrib'])
