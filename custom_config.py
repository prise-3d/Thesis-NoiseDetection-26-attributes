from modules.config.attributes_config import *

# store all variables from global config
context_vars = vars()

# folders
## min_max_custom_folder           = 'custom_norm'
## correlation_indices_folder      = 'corr_indices'

# variables
features_choices_labels         = ['filters_statistics']

## models_names_list               = ["svm_model","ensemble_model","ensemble_model_v2","deep_keras"]
## normalization_choices           = ['svd', 'svdn', 'svdne']

# parameters
## keras_epochs                    = 500
## keras_batch                     = 32
## val_dataset_size                = 0.2