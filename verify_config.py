#!/usr/bin/env python3
"""
Quick configuration verification script.
Run this to see which models will be trained with current settings.
"""

import sys

# Simulate the configuration settings (copy from analysis.py)
TRAIN_LSTM = True
TRAIN_BILSTM = True
TRAIN_GRU = True
TRAIN_CNN_LSTM = True
TRAIN_XGBOOST = True
TRAIN_RANDOM_FOREST = True
TRAIN_GRADIENT_BOOSTING = True
TRAIN_SVM = False
TRAIN_MLP = False
TRAIN_PROPHET = False

TRAIN_REGULAR_HYBRIDS = True
TRAIN_LSTM_BILSTM = True
TRAIN_LSTM_GRU = True
TRAIN_PROPHET_LSTM = False
TRAIN_PROPHET_BILSTM = False
TRAIN_PROPHET_XGBOOST = False

TRAIN_ENHANCED_HYBRIDS = False
TRAIN_ENSEMBLE_HYBRIDS = True
TRAIN_DL_ENSEMBLE = True
TRAIN_TREE_ENSEMBLE = True
TRAIN_STACKED_ENSEMBLE = False
TRAIN_COMPREHENSIVE_ENSEMBLE = False

REDUCE_MODEL_UNITS = False
REDUCE_BATCH_SIZE = False
REDUCE_DENSE_UNITS = False

# Apply memory optimizations
if REDUCE_MODEL_UNITS:
    print("⚠️ Memory optimization: Model units will be reduced by 50%")

if REDUCE_BATCH_SIZE:
    print("⚠️ Memory optimization: Batch size will be reduced from 32 to 16")

if REDUCE_DENSE_UNITS:
    print("⚠️ Memory optimization: Dense units will be reduced by 50%")

# Count models
individual_models = []
if TRAIN_LSTM:
    individual_models.append("LSTM")
if TRAIN_BILSTM:
    individual_models.append("BiLSTM")
if TRAIN_GRU:
    individual_models.append("GRU")
if TRAIN_CNN_LSTM:
    individual_models.append("CNN-LSTM")
if TRAIN_XGBOOST:
    individual_models.append("XGBoost")
if TRAIN_RANDOM_FOREST:
    individual_models.append("RandomForest")
if TRAIN_GRADIENT_BOOSTING:
    individual_models.append("GradientBoosting")
if TRAIN_SVM:
    individual_models.append("SVM")
if TRAIN_MLP:
    individual_models.append("MLP")
if TRAIN_PROPHET:
    individual_models.append("Prophet")

hybrid_models = []
if TRAIN_REGULAR_HYBRIDS:
    if TRAIN_LSTM_BILSTM and 'LSTM' in individual_models and 'BiLSTM' in individual_models:
        hybrid_models.append("LSTM-BiLSTM")
    if TRAIN_LSTM_GRU and 'LSTM' in individual_models and 'GRU' in individual_models:
        hybrid_models.append("LSTM-GRU")
    if TRAIN_PROPHET_LSTM and 'Prophet' in individual_models and 'LSTM' in individual_models:
        hybrid_models.append("Prophet-LSTM")
    if TRAIN_PROPHET_BILSTM and 'Prophet' in individual_models and 'BiLSTM' in individual_models:
        hybrid_models.append("Prophet-BiLSTM")
    if TRAIN_PROPHET_XGBOOST and 'Prophet' in individual_models:
        hybrid_models.append("Prophet-XGBoost")

ensemble_models = []
if TRAIN_ENSEMBLE_HYBRIDS:
    if TRAIN_DL_ENSEMBLE and sum([m in individual_models for m in ['LSTM', 'BiLSTM', 'GRU', 'CNN-LSTM']]) >= 2:
        ensemble_models.append("DeepLearningEnsemble")
    if TRAIN_TREE_ENSEMBLE and sum([m in individual_models for m in ['XGBoost', 'RandomForest', 'GradientBoosting']]) >= 2:
        ensemble_models.append("TreeBasedEnsemble")
    if TRAIN_STACKED_ENSEMBLE and sum([m in individual_models for m in ['LSTM', 'XGBoost', 'RandomForest']]) >= 2:
        ensemble_models.append("StackedEnsemble")
    if TRAIN_COMPREHENSIVE_ENSEMBLE and len(individual_models) >= 3:
        ensemble_models.append("ComprehensiveEnsemble")

# Print results
print("\n" + "="*80)
print("TRAINING CONFIGURATION SUMMARY")
print("="*80)

print("\n📊 INDIVIDUAL MODELS (" + str(len(individual_models)) + "):")
for model in sorted(individual_models):
    print(f"  ✓ {model}")

print("\n🔗 HYBRID MODELS (" + str(len(hybrid_models)) + "):")
if hybrid_models:
    for model in sorted(hybrid_models):
        print(f"  ✓ {model}")
else:
    print("  (None)")

print("\n🎯 ENSEMBLE MODELS (" + str(len(ensemble_models)) + "):")
if ensemble_models:
    for model in sorted(ensemble_models):
        print(f"  ✓ {model}")
else:
    print("  (None)")

total = len(individual_models) + len(hybrid_models) + len(ensemble_models)
print("\n" + "-"*80)
print(f"TOTAL MODELS TO TRAIN: {total}")
print("-"*80)

# Estimate training time
if total <= 3:
    estimated_time = "2-5 minutes (LIGHT)"
elif total <= 10:
    estimated_time = "10-20 minutes (BALANCED)"
elif total <= 20:
    estimated_time = "20-40 minutes (HEAVY)"
else:
    estimated_time = "40+ minutes (VERY HEAVY)"

print(f"Estimated training time: {estimated_time}")
print(f"Configuration type: ", end="")
if total <= 3:
    print("🟢 LIGHT")
elif total <= 10:
    print("🟡 BALANCED")
else:
    print("🔴 HEAVY")

print("\nTo modify this configuration:")
print("  1. Edit the flags at the top of this script")
print("  2. Copy the same flag values into analysis.py (lines ~155-190)")
print("  3. Re-run this script to verify the changes")

# Memory estimate
print("\n" + "-"*80)
print("MEMORY REQUIREMENTS (Approximate):")
if REDUCE_MODEL_UNITS and REDUCE_BATCH_SIZE:
    print("  ⚠️ With aggressive memory optimization: ~2-4 GB peak")
elif REDUCE_BATCH_SIZE:
    print("  ⚠️ With batch size reduction: ~4-6 GB peak")
elif REDUCE_MODEL_UNITS:
    print("  ⚠️ With unit reduction: ~4-6 GB peak")
elif total <= 3:
    print("  ✓ Low memory: ~2-4 GB peak")
elif total <= 10:
    print("  ⚠️ Moderate memory: ~4-8 GB peak")
else:
    print("  🔴 High memory: 8+ GB peak (GPU recommended)")

print("="*80)
