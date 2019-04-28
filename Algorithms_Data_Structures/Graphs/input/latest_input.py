input_data = {
	"links": [{
			"testcases": [],
			"target": "standard_verify(data_import)",
			"strength": "0",
			"source": "standard_import_file(data_import)"
		},
			{
			"testcases": [],
			"target": "udf_verify(data_import)",
			"strength": "0",
			"source": "udf_import_file(data_import)"
		},
			{
			"testcases": [],
			"target": "both_verify(data_import)",
			"strength": "0",
			"source": "both_import_file(data_import)"
		},
			{
			"testcases": [],
			"target": "udf_populate_dynamic_data_for_non_ssa_fields(data_import)",
			"strength": "0",
			"source": "include_only_udf_fields(data_import)"
		}, {
			"testcases": [],
			"target": "standard_populate_dynamic_data_for_non_ssa_fields(data_import)",
			"strength": "0",
			"source": "include_only_standard_fields(data_import)"
		}, {
			"testcases": [],
			"target": "data_import()",
			"strength": "0",
			"source": "Fluent()"
		}, {
			"testcases": [],
			"target": "project()",
			"strength": "0",
			"source": "Fluent()"
		}, {
			"testcases": [],
			"target": "create_for_entity(data_import)",
			"strength": "0",
			"source": "data_import()"
		}, {
			"testcases": [],
			"target": "set_title(project)",
			"strength": "0",
			"source": "project()"
		}, {
			"testcases": [],
			"target": "set_description(project)",
			"strength": "0",
			"source": "project()"
		}, {
			"testcases": [],
			"target": "where_field_mapping_is(data_import)",
			"strength": "0",
			"source": "create_for_entity(data_import)"
		}, {
			"testcases": [],
			"target": "verify_title(project)",
			"strength": "0",
			"source": "set_title(project)"
		}, {
			"testcases": [],
			"target": "verify_desc(project)",
			"strength": "0",
			"source": "set_description(project)"
		}, {
			"testcases": [],
			"target": "cond_standard_and_udf(data_import)",
			"strength": "0",
			"source": "where_field_mapping_is(data_import)"
		},
			{
			"testcases": [],
			"target": "include_both_standard_and_udf_fields(data_import)",
			"strength": "0",
			"source": "cond_standard_and_udf(data_import)",
			"label": {"name": "Yes"}
		},
			{
			"testcases": [],
			"target": "cond_standard_or_udf(data_import)",
			"strength": "0",
			"source": "cond_standard_and_udf(data_import)",
			"label": {"name": "No"}
		},
			{
			"testcases": [],
			"target": "include_only_standard_fields(data_import)",
			"strength": "0",
			"source": "cond_standard_or_udf(data_import)",
			"label": {"name": "Yes"}
		}, {
			"testcases": [],
			"target": "include_only_udf_fields(data_import)",
			"strength": "0",
			"source": "cond_standard_or_udf(data_import)",
			"label": {"name": "No"}
		}, {
			"testcases": [],
			"target": "both_populate_dynamic_data_for_non_ssa_fields(data_import)",
			"strength": "0",
			"source": "include_both_standard_and_udf_fields(data_import)"
		}, {
			"testcases": [],
			"target": "standard_import_file(data_import)",
			"strength": "0",
			"source": "standard_populate_dynamic_data_for_non_ssa_fields(data_import)"
		},
			{
			"testcases": [],
			"target": "udf_import_file(data_import)",
			"strength": "0",
			"source": "udf_populate_dynamic_data_for_non_ssa_fields(data_import)"
		},
			{
			"testcases": [],
			"target": "both_import_file(data_import)",
			"strength": "0",
			"source": "both_populate_dynamic_data_for_non_ssa_fields(data_import)"
		}
	],
	"nodes": [{
			"type": ["Atom"],
			"sequence": 1,
			"label": "import_file",
			"id": "standard_import_file(data_import)"
		}, {
			"type": ["Atom"],
			"sequence": 2,
			"label": "include_only_udf_fields",
			"id": "include_only_udf_fields(data_import)"
		}, {
			"type": ["Atom"],
			"sequence": 3,
			"label": "include_only_standard_fields",
			"id": "include_only_standard_fields(data_import)"
		}, {
			"type": ["Atom"],
			"sequence": 4,
			"label": "verify",
			"id": "standard_verify(data_import)"
		}, {
			"type": ["Atom"],
			"sequence": 5,
			"label": "verify",
			"id": "verify_title(project)"
		}, {
			"type": ["Entity"],
			"sequence": 76,
			"label": "Fluent",
			"id": "Fluent()",
			"args": [{"name": "request"}]
		}, {
			"type": ["Entity"],
			"sequence": 77,
			"label": "data_import",
			"id": "data_import()"
		}, {
			"type": ["Entity"],
			"sequence": 78,
			"label": "project",
			"id": "project()"
		}, {
			"type": ["Atom"],
			"sequence": 79,
			"label": "create_for_entity",
			"id": "create_for_entity(data_import)",
			"args": [{"str": "PROGRAM"}]
		}, {
			"type": ["Atom"],
			"sequence": 80,
			"label": "set_title",
			"id": "set_title(project)",
			"args": [{"str": "My_project_name"}]
		}, {
			"type": ["Atom"],
			"sequence": 81,
			"label": "set_description",
			"id": "set_description(project)",
			"args": [{"str": "My_description"}]
		}, {
			"type": ["Atom"],
			"sequence": 82,
			"label": "where_field_mapping_is",
			"id": "where_field_mapping_is(data_import)",
			"args": [{"str": "SAME"}]
		}, {
			"type": ["Atom"],
			"sequence": 83,
			"label": "include_both_standard_and_udf_fields",
			"id": "include_both_standard_and_udf_fields(data_import)"
		}, {
			"type": ["Atom"],
			"sequence": 95,
			"label": "populate_dynamic_data_for_non_ssa_fields",
			"id": "standard_populate_dynamic_data_for_non_ssa_fields(data_import)"
		},
			{
			"type": ["Condition"],
			"sequence": 96,
			"label": "standard_and_udf",
			"id": "cond_standard_and_udf(data_import)"
		},
			{
			"type": ["Condition"],
			"sequence": 97,
			"label": "standard_or_udf",
			"id": "cond_standard_or_udf(data_import)"
		},
			{
			"label": "import_file",
			"id": "udf_import_file(data_import)",
			"sequence": 98,
			"type": ["Atom"]
		},
			{
			"label": "import_file",
			"id": "both_import_file(data_import)",
			"sequence": 99,
			"type": ["Atom"]
		},
			{
			"type": ["Atom"],
			"sequence": 100,
			"label": "populate_dynamic_data_for_non_ssa_fields",
			"id": "udf_populate_dynamic_data_for_non_ssa_fields(data_import)"
		},
			{
			"type": ["Atom"],
			"sequence": 101,
			"label": "populate_dynamic_data_for_non_ssa_fields",
			"id": "both_populate_dynamic_data_for_non_ssa_fields(data_import)"
		},
			{
			"type": ["Atom"],
			"sequence": 102,
			"label": "verify",
			"id": "udf_verify(data_import)"
		},
			{
			"type": ["Atom"],
			"sequence": 103,
			"label": "verify",
			"id": "both_verify(data_import)"
		},
			{
			"type": ["Atom"],
			"sequence": 104,
			"label": "verify",
			"id": "verify_desc(project)"
		}
	]
}
