import re

ALLOWED_FUNCS = ["clean_up",
                 "build_id",
                 "validate_password",
                 "create_unique",
                 "create_short_address",
                 "validate_pcode",
                 "ids_addrs",
                 "main",
                 "split",
                 "append",
                 "lower",
                 "len",
                 "ord",
                 "isdigit",
                 "str",
                 "int",
                 "open",
                 "close",
                 "read",
                 "write",
                 "range"
                ]


with open("assignment1.py", "r", encoding="utf-8") as f:
    file_content = f.read()

    # check for function usage
    raw_pattern = r"[\s]*([\w]+)\("
    pattern = re.compile(raw_pattern)
    results = re.finditer(pattern, file_content)

    disallowed_funcs = []
    for result in results:
        # print(result, "--->", result.group(1))
        func_name = result.group(1)
        if func_name not in ALLOWED_FUNCS:
            disallowed_funcs.append(func_name.lower())

    # remove occurences that appear in the skeleton code in main()
    disallowed_funcs.remove("input") # this appears in main
    for _ in range(10):
        disallowed_funcs.remove("print")

    if len(disallowed_funcs) > 0:
        print("DISALLOWED FUNCTIONS:")
        for func in set(disallowed_funcs):
            num_occurences = disallowed_funcs.count(func)
            if num_occurences > 1:
                print(f"{func}: {num_occurences} occurences")
            elif num_occurences == 1:
                print(f"{func}: {num_occurences} occurence")
    else:
        print("Looks good - no disallowed functions!")