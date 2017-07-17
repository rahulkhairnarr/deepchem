"""
Gathers all models in one place for convenient imports
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from deepchem.models.models import Model
from deepchem.models.sklearn_models import SklearnModel
from deepchem.models.xgboost_models import XGBoostModel
from deepchem.models.tf_new_models.multitask_classifier import MultitaskGraphClassifier
from deepchem.models.tf_new_models.multitask_regressor import MultitaskGraphRegressor, DTNNMultitaskGraphRegressor

from deepchem.models.tf_new_models.support_classifier import SupportGraphClassifier
from deepchem.models.multitask import SingletaskToMultitask
from deepchem.models.sequential import Sequential

from deepchem.models.tensorflow_models.fcnet import TensorflowMultiTaskRegressor
from deepchem.models.tensorflow_models.fcnet import TensorflowMultiTaskClassifier
from deepchem.models.tensorflow_models.fcnet import TensorflowMultiTaskFitTransformRegressor
from deepchem.models.tensorflow_models.fcnet import TensorGraphMultiTaskRegressor
from deepchem.models.tensorflow_models.fcnet import TensorGraphMultiTaskClassifier
from deepchem.models.tensorflow_models.fcnet import TensorGraphMultiTaskFitTransformRegressor
from deepchem.models.tensorflow_models.robust_multitask import RobustMultitaskRegressor
from deepchem.models.tensorflow_models.robust_multitask import RobustMultitaskClassifier
from deepchem.models.tensorflow_models.lr import TensorflowLogisticRegression
from deepchem.models.tensorflow_models.progressive_multitask import ProgressiveMultitaskRegressor
from deepchem.models.tensorflow_models.progressive_joint import ProgressiveJointRegressor
from deepchem.models.tensorflow_models.IRV import TensorflowMultiTaskIRVClassifier
from deepchem.models.tensorgraph.tensor_graph import TensorGraph
from deepchem.models.tensorgraph.models.graph_models import WeaveTensorGraph, DTNNTensorGraph, DAGTensorGraph, GraphConvTensorGraph
from deepchem.models.tensorgraph.models.symmetry_function_regression import BPSymmetryFunctionRegression, ANIRegression
