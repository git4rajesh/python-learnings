SELECT_XID = """SELECT xid 
FROM [dbpath]ext_struc_key_map 
WHERE structure_code='%s'"""

SELECT_PROJECT_DETAILS = """
SELECT *
FROM [dbpath]custom_data
WHERE planning_code = '%s'
"""

SELECT_PROJECT_DESCRIPTION = """
SELECT line_text
FROM [dbpath]long_text
WHERE key2 = '%s'
"""

SELECT_PROJECT_NAME = """
 SELECT description
FROM [dbpath]structure
WHERE structure_code= '%s'
"""
