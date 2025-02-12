# **2Psinapod** - *extraction of auditory neural response features from two-photon recordings.*

The 2PSinaPod analysis pipeline is designed to extract key neural response properties from two-photon recordings, focusing on auditory neuronal feature information. This comprehensive pipeline caters to various steps from raw data processing to feature extraction and interactive data visualization, using a range of external tools and custom Jupyter Notebooks.
 

## Analysis Notebooks:

Feature extraction and analysis code is contained in Jupyter notebooks.  Each notebook covers a particular neuronal property or group of properties, e.g. response bandwidth or best frequency.  

They are all designed to start from the same point, taking the formatted and normalized neuronal response dictionaries for a full response cohort (e.g. post-psilocybin administration).  They are set up to analyze all animals together but containing 
the ID's in dictionaries allows you to select particular animals, or run mixed effects models. 





## External Tools Employed: 
The full pipeline uses a number of tools that help us get from TIFF files to neuronal tuning properties. These are:

**Suite2P** - A powerful tool (Python) that aids in motion correction, ROI identification and calcium signal extraction from raw data.  You can either download and use the GUI, or directly clone from the Github if you want to make changes yourself. 

https://github.com/MouseLand/suite2p

**ROIMatchPub** - An opensource tool in MATLAB that significantly speeds up the matching of neuronal ROI's across recordings, allowing for longitudinal analysis. 

https://github.com/ransona/ROIMatchPub

**TDTBin2Mat** - MATLAB package to convert TDT sound presentation hardware file types to more workable format for Python. 

https://www.tdt.com/docs/sdk/offline-data-analysis/offline-data-matlab/


## Author Contributions:

Conor Lane: Development and implementation of the analysis pipeline.

Veronica Tarka: Contributions to the analysis and validation of results.

For more information, contact Conor Lane at **conor.lane1995@gmail.com**.






Key Features:
End-to-End Analysis: From raw two-photon TIFF files to detailed neuronal tuning properties.
Custom Jupyter Notebooks: Specialized notebooks for different neuronal properties such as response bandwidth and best frequency.
Integration with External Tools: Utilizes powerful tools including Suite2P for motion correction and calcium signal extraction, ROIMatchPub for longitudinal analysis, and TDTBin2Mat for data conversion.
Technologies and Tools:
Languages: Jupyter Notebook (97.8%), Python (2.2%)
Suite2P: Motion correction, ROI identification, and signal extraction.
ROIMatchPub: Efficient matching of neuronal ROIs across recordings.
TDTBin2Mat: Conversion of TDT hardware file types for analysis.
Impact and Applications:
The pipeline is instrumental in studying the effects of various treatments on neural responses, enabling detailed and accurate analysis of neuronal data over time. Its robust design and integration with advanced tools make it a valuable resource for researchers in the field of neuroimaging.

Author Contributions:
Conor Lane: Development and implementation of the analysis pipeline.
Veronica Tarka: Contributions to the analysis and validation of results.
For more information, contact Conor Lane at conor.lane1995@gmail.com.