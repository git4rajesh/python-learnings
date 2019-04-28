from urllib.parse import urlsplit, parse_qs, urlencode, urlunsplit


def set_query_parameter(url, **kwargs):

    scheme, netloc, path, query_string, fragment = urlsplit(url)
    print(path, query_string)
    query_params = parse_qs(query_string)

    for p_key, p_value in kwargs['kwargs'].items():
        query_params[p_key] = p_value

    new_query_string = urlencode(query_params, doseq=True)

    return urlunsplit((scheme, netloc, path, new_query_string, fragment))

if __name__ == '__main__':
    query_params = {'env': 'x',
                    'db_name': 'y',
                    'ext_env': 'z'}

    print(set_query_parameter("/projectplace", kwargs=query_params))