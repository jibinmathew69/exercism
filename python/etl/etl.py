def transform(legacy_data):
    # data = {}
    # for k,v in legacy_data.items():
    #     for items in v:
    #         data[items.lower()] = k
    #
    # return data
    return {c.lower(): k for k, v in ld.items() for c in v}