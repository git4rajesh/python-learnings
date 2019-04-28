import objectpath

book_data = 	{
	"store": {
		"book": [
			{
				"category": "reference",
				"author": "Nigel Rees",
				"title": "Sayings of the Century",
				"price": 8.95
			},
			{
				"category": "fiction",
				"author": "Evelyn Waugh",
				"title": "Sword of Honour",
				"price": 12.99
			},
			{
				"category": "fiction",
				"author": "Herman Melville",
				"title": "Moby Dick",
				"isbn": "0-553-21311-3",
				"price": 8.99
			},
			{
				"category": "fiction",
				"author": "J. R. R. Tolkien",
				"title": "The Lord of the Rings",
				"isbn": "0-395-19395-8",
				"price": 22.99
			}
		]
	}
}


print(type(book_data))
# # Create a Tree out of the Json response
json_tree = objectpath.Tree(book_data)
#
# # Pass the Object Path syntax to execute method and get the desired output.
# result = json_tree.execute('$.store.book[@.price is 12.99]')
# result1 = json_tree.execute('$.store.book[@.price is 12.99].(price,author)')
#
# # The output sometimes is a list and sometimes can be a generator or a chain.
# # So then cast the o/p to list.
# print(list(result))
# print(list(result1))
#
# result3 = json_tree.execute('$..price[@ > 8.99]')
# print(list(result3))

result = json_tree.execute('$..price')
print(list(result))


