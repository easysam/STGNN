# STGNN
The pytorch implementation of Traffic Flow Prediction via Spatial Temporal Graph Neural Network

## Dependencies
`pandas=1.0.5`, `torch`, `tqdm`, `pytables`<br>
commands to install the above packages:<br>
`conda install pandas=1.0.5 tqdm pytables`<br>
`conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c conda-forge`

## Problem
**input:** 12 sampling (sampling frequency: 5 min), i.e., 1 hour<br>
**forecasting horizon:** 12, i.e., 1 hour

## Method Details

