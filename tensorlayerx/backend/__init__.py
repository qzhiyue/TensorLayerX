#! /usr/bin/python
# -*- coding: utf-8 -*-

from .ops import BACKEND
from .ops import BACKEND_VERSION
from .ops import padding_format
from .ops import preprocess_1d_format
from .ops import preprocess_2d_format
from .ops import preprocess_3d_format
from .ops import nchw_to_nhwc
from .ops import nhwc_to_nchw
from .ops import relu
from .ops import elu
from .ops import relu6
from .ops import leaky_relu
from .ops import sigmoid
from .ops import softmax
from .ops import gelu
from .ops import bias_add
from .ops import moments
from .ops import histogram
from .ops import flatten
from .ops import index_select
from .ops import dot

from .ops import ReLU
from .ops import ELU
from .ops import ReLU6
from .ops import LeakyReLU
from .ops import Softplus
from .ops import Tanh
from .ops import Sigmoid
from .ops import Softmax
from .ops import GeLU
from .ops import BiasAdd
from .ops import Floor
from .ops import Ceil

# load ops
from .ops import Variable
from .ops import matmul
from .ops import add
from .ops import dtypes
from .ops import minimum
from .ops import reshape
from .ops import concat
from .ops import convert_to_tensor
from .ops import convert_to_numpy
from .ops import sqrt
from .ops import reduce_mean
from .ops import reduce_min
from .ops import reduce_max
from .ops import pad
from .ops import stack
from .ops import meshgrid
from .ops import arange
from .ops import expand_dims
from .ops import tile
from .ops import cast
from .ops import transpose
from .ops import gather_nd
from .ops import clip_by_value
from .ops import split
from .ops import get_tensor_shape
from .ops import set_context
from .ops import resize
from .ops import floor
from .ops import gather
from .ops import linspace
from .ops import slice
from .ops import add_n
from .ops import ceil
from .ops import multiply
from .ops import divide
from .ops import identity
from .ops import triu
from .ops import tril
from .ops import abs
from .ops import acos
from .ops import acosh
from .ops import angle
from .ops import argmax
from .ops import argmin
from .ops import asin
from .ops import asinh
from .ops import atan
from .ops import atanh
from .ops import cos
from .ops import cosh
from .ops import count_nonzero
from .ops import cumprod
from .ops import cumsum
from .ops import equal
from .ops import exp
from .ops import floordiv
from .ops import floormod
from .ops import greater
from .ops import greater_equal
from .ops import is_inf
from .ops import is_nan
from .ops import l2_normalize
from .ops import less
from .ops import less_equal
from .ops import log
from .ops import log_sigmoid
from .ops import maximum
from .ops import negative
from .ops import not_equal
from .ops import pow
from .ops import real
from .ops import reciprocal
from .ops import reduce_prod
from .ops import reduce_std
from .ops import reduce_sum
from .ops import reduce_variance
from .ops import round
from .ops import rsqrt
from .ops import segment_max
from .ops import segment_mean
from .ops import segment_min
from .ops import segment_prod
from .ops import segment_sum
from .ops import sign
from .ops import sin
from .ops import sinh
from .ops import softplus
from .ops import square
from .ops import squared_difference
from .ops import subtract
from .ops import tan
from .ops import tanh
from .ops import any
from .ops import all
from .ops import logical_and
from .ops import logical_or
from .ops import logical_not
from .ops import logical_xor
from .ops import argsort
from .ops import bmm
from .ops import where
from .ops import ones_like
from .ops import zeros_like
from .ops import squeeze
from .ops import unsorted_segment_sum
from .ops import unsorted_segment_min
from .ops import unsorted_segment_mean
from .ops import unsorted_segment_max
from .ops import set_seed
from .ops import is_tensor
from .ops import tensor_scatter_nd_update
from .ops import diag
from .ops import mask_select
from .ops import eye
from .ops import einsum
from .ops import set_device
from .ops import get_device
from .ops import scatter_update
from .ops import to_device
from .ops import logsoftmax
from .ops import roll
from .ops import topk
from .ops import hardsigmoid
from .ops import hardswish
from .ops import numel
# dtype
from .ops import (
    DType, float16, float32, float64, int8, int16, int32, int64, uint8, uint16, uint32, uint64, bool, complex64,
    complex128
)
# initlizers
from .ops import (
    zeros, ones, constant, random_uniform, random_normal, truncated_normal, he_normal, he_uniform, xavier_normal, xavier_uniform
)
# backend
from .ops import Reshape
from .ops import ReduceSum
from .ops import ReduceMax
from .ops import ReduceMean
from .ops import OneHot
from .ops import L2Normalize
from .ops import EmbeddingLookup
from .ops import NCELoss
from .ops import NotEqual
from .ops import Cast
from .ops import ExpandDims
from .ops import CountNonzero
from .ops import FlattenReshape
from .ops import Transpose
from .ops import MatMul
from .ops import Tile
from .ops import Concat
from .ops import ZeroPadding1D
from .ops import ZeroPadding2D
from .ops import ZeroPadding3D
from .ops import Stack
from .ops import Unstack
from .ops import Sign
from .ops import Resize
from .ops import Pad
from .ops import Minimum
from .ops import Maximum
from .ops import Meshgrid
from .ops import BatchToSpace
from .ops import DepthToSpace

from tensorlayerx.backend import ops