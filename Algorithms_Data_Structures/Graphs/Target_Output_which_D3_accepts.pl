links_data = [
		{ target: "project", source: "fluent" , strength: 0.7 },
		{ target: "timesheet", source: "fluent" , strength: 0.7 },
	  { target: "task", source: "project" , strength: 0.7 },
	  { target: "set_title(project)", source: "project" , strength: 0.7 },
	  { target: "set_description(project)", source: "project" , strength: 0.7 },
	  { target: "log", source: "timesheet" , strength: 0.7 },
	  { target: "submit"  , source: "log", strength: 0.7 },
	  { target: "approve"  , source: "submit", strength: 0.7 },
	  { target: "verify"   , source: "approve" , strength: 0.1 },
	  { target: "verify"  , source: "set_title(project)" , strength: 0.1 },
	  { target: "verify"   , source: "set_description(project)" , strength: 0.1 },
		{ target: "asset"   , source: "fluent" , strength: 0.1 }
	]