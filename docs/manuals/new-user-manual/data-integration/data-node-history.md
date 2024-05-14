Among other functionalities, a data node keep track of the data editing history. Every time a
data is written using data node methods, a new entry is added on the head of the list of edits.
An `Edit` contains the timestamp of the edit, optional comments and the editor (a custom editor
id passed as a parameter when writing the data or a job id if the edit is done by a job).

# Data node history

## Python API
- Get a data node list of edits
- Get the last edit of a data node
- Write data with a custom editor id
- Write data with a job id
- Get the editor of an edit
- Get the job of an edit
- Get the comments of an edit
- Get the timestamp of an edit

## Data node history in the graphical interface


# Validity period



