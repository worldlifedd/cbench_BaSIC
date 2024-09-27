from configs.class_builder import ClassBuilder, ParamSlot
from configs.import_utils import import_class_builder_from_module

from . import dist_cat_embedding as base_module

from cbench.modules.prior_model.prior_coder import EmbeddingStandardNormalPriorCategoricalDistributionPriorCoder

config = import_class_builder_from_module(base_module)\
    .update_class(EmbeddingStandardNormalPriorCategoricalDistributionPriorCoder)\
    .add_all_kwargs_as_param_slot()