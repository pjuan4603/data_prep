## Data pre-processing for Amazon datasets
These are the code used for preprocessing the data from Amazon datasets
### Python codes:

**shared_users.py** : Extract the shared users from two domains.  
**remove_bus_under_3.py** :	Remove the busnisesses that has less than three reviews.  
**remove_user_under_3.py** : Remove the users that has given less than three reviews.	  
**rename_users_business.py** : Reindex the users and businesses.  
  
_The following code are for BPMF implementataion_  
**form_final_dataset.py** :	Form a JSON dataset from the processed data for the use of BPMF implementation.  
**from_json_to_mat.py** : Output the desired .mat files for the Matlab BPMF implemetation.   
  
### Recommended Steps: 

1. shared_users.py
2. remove_bus_under_3.py
3. remove_user_under_3.py
4. rename_users_business.py

_The following steps are for BPMF implementataion_  

5. form_final_dataset.py
6. from_json_to_mat.py
