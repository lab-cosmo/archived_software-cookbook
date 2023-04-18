"""
Computing a Structure Selection over a dataset
==============================================

.. start-body

In this tutorial we compute a structure selection with FPS.

We first import all necessary packages.
"""


import sklearn
import numpy as np
from time import time

import ase
from ase.io import read, write

import skmatter
from skmatter.sample_selection import CUR, FPS
import rascal
from rascal.models import Kernel, train_gap_model, compute_KNM, KRR
from rascal.representations import SphericalInvariants
from rascal.utils import from_dict, to_dict, CURFilter, FPSFilter, dump_obj, load_obj, get_score




# %%
# Dataset
# -------
#
# Load the structures
# We read the first 100 structures of the data set using
# `ASE https://wiki.fysik.dtu.dk/ase/`_.

datasets_dir = './dataset/'
input_file = 'input-fps.xyz'

data_file = datasets_dir + input_file


dataset = read(data_file,':100', format='extxyz')
N_dataset = len(dataset)
for frame in dataset: 
    frame.wrap(eps=1.0e-12)

# %%
#
# Compute SOAP
# ------------
#
# We construct the descriptor training data with a SOAP powerspectrum using

hypersbaseline = dict(
              soap_type="PowerSpectrum",
              interaction_cutoff=6.0, 
              max_radial=8,
              max_angular=6,
              gaussian_sigma_constant=0.3,
              gaussian_sigma_type="Constant",
              cutoff_function_type="RadialScaling",
              cutoff_smooth_width=0.5,
              cutoff_function_parameters=
                    dict(
                            rate=1,
                            scale=3.5,
                            exponent=4
                        ),
              radial_basis="GTO",
              normalize=True,
              optimization=
                    dict(
                            Spline=dict(
                               accuracy=1.0e-05
                            )
                        ),
              compute_gradients=False
              )

repr_bas = SphericalInvariants(**hypersbaseline)

start = time()
managers = repr_bas.transform(dataset)
feat_vector = managers.get_features(repr_bas)

# %%
#
# Feature Selection
# -----------------
# 
# feature selection and sparse enviroment



n_sparse_feat = 200
feat_compressor = FPSFilter(repr_bas, n_sparse_feat, act_on='feature')
feat_sparse_parameters = feat_compressor.select_and_filter(managers)
feat_sparse_parameters.keys()


hypersbaseline['coefficient_subselection'] = feat_sparse_parameters['coefficient_subselection']
repr_bas_fsparse = SphericalInvariants(**hypersbaseline)


managers_sparsefeat = repr_bas_fsparse.transform(dataset)

feat_vector_sparsefeat = managers_sparsefeat.get_features(repr_bas_fsparse)

feat_vector_sparsefeat.shape


# %%
#
# Compute the mean descriptor
# ---------------------------
#
# compute the mean-per structure descriptor

feat_vector_sparsefeat = feat_vector_sparsefeat.reshape((50, n_atoms, n_sparse_feat))

feat_vector_sparsefeat = np.mean(feat_vector_sparsefeat, axis = 1)
print('feature vector descriptor', feat_vector_sparsefeat.shape)


# %%
# 
# Atomic structure sample selection FPS and CUR
# ---------------------------------------------
#
# Compute the sample selection with FPS and CUR
#

n_samples = 15
cur = CUR(n_to_select=n_samples)
cur.fit(feat_vector_sparsefeat)
cur_idxs = cur.fit(feat_vector_sparsefeat).selected_idx_

fps = FPS(n_to_select=n_samples, initialize=11)
fps.fit(feat_vector_sparsefeat)
fps_idxs = fps.fit(feat_vector_sparsefeat).selected_idx_

print(cur_idxs)
print(fps_idxs)

