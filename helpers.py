# returns a list of the invalid fips given a list of fips codes
def invalid_fips(fips):
    return [code for code in fips if float(code) <= 0.0 or type(code) == float or len(code) != 5]


# removes all columns from a dataset that are not contained within the keep_cols list. Removal is done by dropping the columns inplace and with an axis = 1

def remove_cols(dataset, keep_cols):
    for col in dataset.columns:
        if not col in keep_cols:
            dataset.drop(col, inplace = True, axis = 1)
